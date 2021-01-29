# Here are a couple of important notes about using random.random() and rounding. (Create this function without using random.randInt() -- we are trying to build that method ourselves for this assignment!)

# random.random() returns a random floating number between 0.000 and 1.000
# random.random() * 50 returns a random floating number between 0.000 and 50.000
# random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
# round(num) returns the rounded integer value of num
# Here's a little bit of code to get you started, with some test cases and expected outputs. Test each function call one at a time and a few times each to make sure you're getting the correct range.

# Complete the randInt function
# BONUS: account for any edge cases (eg. min > max, max < 0)

#Question
#import random
#def randInt(min= , max=   ):
#    num = random.random()
#    return num
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

#Answer
def randInt(min=0, max=100):
    import random
    num = random.random()*(max-min) + min
    return(int(num))

print(randInt())
print(randInt(min=0, max=50))
print(randInt(min=50, max=100))
print(randInt(min=50, max=500))