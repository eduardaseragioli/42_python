def  ft_count_harvest_recursive():
    last_day = int(input("Days until harvest: "))
    def count_day(i):
        if i <= last_day:
            print(f"Day {i}")
            count_day(i + 1)
        else:
            return
    count_day(1)