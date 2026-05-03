# Smart Number Analyzer

# Write a program that:

# Takes an integer input
# Prints:
# Whether it is prime
# Whether it is a palindrome
# Sum of its digits

# 👉 Example:
# Input: 131
# Output:

# Prime: Yes
# Palindrome: Yes
# Digit Sum: 5


num = int(input("Enter an Integer:"))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Prime: No")
            break
    else:
        print("Prime: Yes")


is_palindrome = str(num) == str(num)[::-1]

d_sum = sum(int(d) for d in str(num))


print("Palindrome:", "Yes" if is_palindrome else "No")
print("Digit Sum:", d_sum)