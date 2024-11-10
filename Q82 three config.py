# Function to categorize and print numbers
def categorize_numbers(start, end):
    evens = []
    odds = []
    divisible_by_5 = []

    for num in range(start, end + 1):
        if num % 2 == 0:
            evens.append(num)
        if num % 2 != 0:
            odds.append(num)
        if num % 5 == 0:
            divisible_by_5.append(num)


    print("Even numbers:", evens)
    print("Odd numbers:", odds)
    print("Numbers divisible by 5:", divisible_by_5)

# Example usage
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
categorize_numbers(start, end)
print("Program by Arnav Kharbanda, 0221BCA050")
