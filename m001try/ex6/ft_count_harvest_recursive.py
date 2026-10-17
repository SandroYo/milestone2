def ft_recursive(n):
    if n > 0:
        ft_recursive(n - 1)
        print(f"Day {n}")


def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    ft_recursive(day)
    print("Harvest time!")
