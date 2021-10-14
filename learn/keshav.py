def print_pattern(n):
    for row in range(n):
        for column in range(n):
            if ((row + column == n - 1 and row < n / 2) or (row == column and row < n / 2)):
                print("Keshav", end=" ")
            else:
                print(" "*5, end=" ")
        print()
print_pattern(9)