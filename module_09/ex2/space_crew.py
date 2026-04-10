from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")

        ranks = [m.rank for m in self.crew]
        if Rank.commander not in ranks and Rank.captain not in ranks:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) < len(self.crew) * 0.5:
                raise ValueError("Long missions need 50% experienced crew")

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        space = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            launch_date=datetime(2024, 1, 1),
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Mission Command",
                    years_experience=10,
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.commander,
                    age=28,
                    specialization="Navigation",
                    years_experience=6,
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=37,
                    specialization="Engineering",
                    years_experience=15,
                ),
            ],
        )
        print("Valid mission created:")
        print(f"Mission: {space.mission_name}")
        print(f"ID: {space.mission_id}")
        print(f"Destination: {space.destination}")
        print(f"Duration: {space.duration_days} days")
        print(f"Budget: ${space.budget_millions}M")
        print(f"Crew size: {len(space.crew)}")
        print("Crew members:")
        for member in space.crew:
            print(f"- {member.name} ({member.rank.value}) -"
                  + f"{member.specialization}")

    except ValidationError as e:
        print(f"Error inesperado: {e}")

    print("\n=========================================")

    try:
        space = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            launch_date=datetime(2024, 1, 1),
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Mission Command",
                    years_experience=10,
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.commander,
                    age=28,
                    specialization="Navigation",
                    years_experience=6,
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=37,
                    specialization="Engineering",
                    years_experience=15,
                    is_active=False,
                ),
            ],
        )

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
