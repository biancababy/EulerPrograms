# Python Program largest prime factor of the number 600851475143


# function to find largest prime factor
def primefact(n):
    i = 1
    while i <= n:
        count = 0
        if n % i == 0:
            j = 1
            while j <= i:
                if i % j == 0:
                    count = count + 1
                j = j + 1
            if count == 2:
                print(" {} is a Prime Factor of {}".format(i, n))
                large = i
                # arr.append(i)  #storing in a list the values
        i = i + 1
    print("Largest prime factor of {} is {}".format(n, large))


# main program
if __name__ == "__main__":
    num = int(input(" Please Enter any Number: "))
    primefact(num)
