# sum of all the multiples of 3 or 5 below 1000

# function to find the sum


def sum_square(n):
    total = 0
    for x in range(n):
        if (x % 3 == 0) or (x % 5 == 0):
            total = total + x
        else:
            pass
    print(total)


# main program
if __name__ == "__main__":
    sum_square(1000)
