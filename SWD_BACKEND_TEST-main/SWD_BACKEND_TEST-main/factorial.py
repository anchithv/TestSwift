def count_trailing_zeros_in_factorial(n):
    count = 0

    # Continue dividing n by 5 until it becomes zero
    while n >= 5:
        n //= 5
        count += n

    return count

# Example usage:
num = int(input("Enter a number to calculate its factorial and count trailing zeros: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

trailing_zeros = count_trailing_zeros_in_factorial(num)
print(f"{num}! = {factorial} has {trailing_zeros} zeros.")
