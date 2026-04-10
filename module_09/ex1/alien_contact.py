from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validation(self) -> "AlienContact":

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\"")

        if self.contact_type == ContactType.physical:
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError(
                    "Strong signals must include received messages")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: \'{alien.message_received}\'")

    except ValidationError as e:
        print(f"Error inesperado: {e}")

    print("\n======================================")

    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=45,
            witness_count=1,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
