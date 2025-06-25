# Check if a number is a palindrome

def is_palindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Example usage
# print(is_palindrome(121))   # True
# print(is_palindrome(-121))  # False
# print(is_palindrome(10))    # False
