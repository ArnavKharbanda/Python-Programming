def main():
    user_string = input("Enter string: ")
    if user_string == user_string[::-1]:
        print(f"User entered string is palindrome")
    else:
        print(f"User entered string is not a palindrome")
if __name__ == "__main__":
    main()

print("Program by Arnav Kharbanda, 0221BCA050")