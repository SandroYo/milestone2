def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    i = 1

    while i <= day:
        print(f"Day {i}")
        if i == day:
            print("Harvest time!")
        i = i + 1
