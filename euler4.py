# Python Program to find largest palindrome made from the product of two 3-digit numbers
# Answer :906609


# function to check if palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]


# function to check largest palindrome
def largest(bot, top):
    z = 0
    for x in range(top, bot, -1):
        for y in range(top, bot, -1):
            if is_palindrome(x * y):
                if x * y > z:
                    z = x * y
    return z


# main program
if __name__ == "__main__":
    print(largest(100, 999))
