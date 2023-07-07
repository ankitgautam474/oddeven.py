numbers = tuple(map(int, input("Enter a series of numbers (space-separated): ").split()))

even_count = 0
odd_count = 0

# iterate through the numbers using a while loop
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    index += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
