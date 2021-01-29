# Basic - Print all integers from 0 to 150.
for count in range(0,151):
    print(count)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for count in range(5,1000001,5):
    print(count)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sumOdd = 0
for number in range(0,500000+1):
    if number % 2 != 0:
        print("{0}".format(number))
        sumOdd = sumOdd + number
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, sumOdd))

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for count in range(2018,0,-4):
    print(count)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexibleCountdown(lowNum, highNum, mult):
    for i in range (lowNum, highNum):
        if i % mult == 0:
            print(i)