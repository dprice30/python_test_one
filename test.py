#Indentation Practice with if Statements

#Task One: Code Correction
weather = "sunny"
if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

# #Task Two: Your Mood Today
answer = input("User, how do you feel today? ")
if(answer == "happy"):
    print("That's great to hear!")
elif(answer == "sad"):
    print("I hope your day gets better!")
else:
    print("Interesting!")

#Task Three: Spotting Indentation Errors
mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!")

#Task One: Create a Poem using Comments

# Python, oh Python, so clear and so neat
# With every new challenge, you're hard to beat.
# Too busy debugging, I can't leave my seat
# In the technical interviews, I plan to bring the heat
# Github stores my Python programs, they'll never delete

'''
Python, in the realm of code you shine,
With simplicity and grace, you're truly divine.
From react to flask , you can easily intertwine
With various technologies, it all work just fine
Creating the logic of programs, line by line 
...
'''

#Task One: Python Naming Convention Practice

pi_value = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

#Task One: Python Data Types and type() Function

variable_a = "Hello, World!"
print(type(variable_a))

variable_b = 23
print(type(variable_b))

variable_c = 3.14
print(type(variable_c))

variable_d = True
print(type(variable_d))

#Task One: Python Dynamic Typing Practice

dynamic_variable = "This is a string"
print(type(dynamic_variable))

dynamic_variable = 100
print(type(dynamic_variable))

dynamic_variable = 25.5
print(type(dynamic_variable))

#Arithmetic Operations in Daily Life
#Task 1: Grocery Store Math

price_apples, price_oranges, price_bananas = 5.99, 6.75, 4.99
print("Grocery Total = $", price_apples + price_oranges + price_bananas)

#Task 2: Bank Interest
initial_amount = 1200
yearly_interest = 0.45
print("Balance: $", initial_amount + (initial_amount * yearly_interest))

#Task 3: Area and Perimeter
length = 10
width = 15

area = length * width
perimeter = (2 * length) + (2 * width)

print("Area =", area)
print("Perimeter =", perimeter)

#Understanding Assignments and Comparisons
#Task One: Value Swapping

print("Before swap..")

num_one = 25

num_two = 35
print("First number: " , num_one)
print("Second number: ",num_two)
temp = num_two

num_two = num_one
num_one = temp
print("After swap..")

print("First number: " , num_one)
print("Second number: ", num_two)

#Task Two: Perfect Square Checker
num = 4
if(num**(1/2) == int(num**(1/2))):
    print("Pefect Square")
else:
    print("Not a Pefect Square")

#Exploring Logical Operations and Precedence
#Task One: Simple Logic Puzzles
window_up = True
door_open = False

if window_up and not door_open or not window_up and not door_open:
    print("Driver can accelerate!")
else:
    print("Please keep foot on break!")

#Task Two: Validating Calculations
equation_no_paren = 4 * 10 / 7 + 9 - 13
print("Equation without parentheses = ", equation_no_paren)
equation_with_paren = (4 * 10) / (7 + 9) - 13
print("Equation with parentheses = ", equation_with_paren)

#Task Three: Mix and Match
#Prediction: True
num_one, num_two = 58, 29
if not (58 + 29) %  2 == 0 or (58 + 29) ** (1/2) and int((58 + 29) / 2):
    print(True)
else:
    print(False)
