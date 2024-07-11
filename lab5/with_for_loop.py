def half_pyramid(height: int = 5):
    for i in range(0, height):
        for j in range(0, i + 1):
            print("* ", end="")
        print("")


def half_pyramid_inverted(height: int = 5):
    for i in range(height - 1):
        for j in range(height - i - 1):
            print("* ", end="")
        print("")


def half_pyramid_reversed(height: int = 5):
    for i in range(0, height):
        print("* " * (height - i))


def centered_pyramid(height: int = 5):
    for i in range(height):
        print(" " * (height - i - 1), end="")
        for j in range(i + 1):
            print("* ", end="")
        print("")


def centered_pyramid_inverted(height: int = 5):
    for i in range(height - 1):
        print(" " * (i + 1), end="")
        for j in range(height - i - 1):
            print("* ", end="")
        print("")


if __name__ == "__main__":
    height = int(input("Enter height pyramid: "))

    # Half
    half_pyramid(height)
    print("-" * 15)
    half_pyramid_inverted(height)
    print("-" * 15)
    # Centered
    centered_pyramid(height)
    centered_pyramid_inverted(height)
    print("-" * 15)
    # Reversed
    half_pyramid_reversed(height)
