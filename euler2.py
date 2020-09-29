# sum of  the even fibonacci series whose values do not exceed four million


# function to find the sum of  the even fibonacci series <4000000
def fibo(n):
    total = 0
    x, y = 0, 1
    fiblist = []
    while y < n:
        x, y = y, x + y
        fiblist.append(y)
        if y % 2:
            continue
        total += y

    # list of fibonacci numbers
    print(fiblist)
    # sum of even fibonacci series
    print(total)


# main program
if __name__ == "__main__":
    fibo(4000000)
