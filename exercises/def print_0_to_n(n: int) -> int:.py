def print_0_to_n(n: int) -> int:
    counter: int = 0
    while counter < n:
        print(counter)
        counter = counter + 1

    print(f"Final: {counter}")
    return counter


print(print_0_to_n(n=4))
