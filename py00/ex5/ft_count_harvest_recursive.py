def ft_count_harvest_recursive(days=None):
    is_start = days is None
    if is_start:
        days = int(input("Days until harvest: "))
    if days > 0:
        ft_count_harvest_recursive(days - 1)
        print(f"Day {days}")
    if is_start:
        print("Harvest time!")
