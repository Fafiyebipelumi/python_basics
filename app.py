birth_year = input("Enter your birth year: ")   
age = 2022 - int(birth_year)  
print(age)  

#Receiving input
name = input("Enter your name: ")
print("Hello " + name)

# Basic math
first = input("First number: " )
second = input("Second number: ")
sum = float(first) + float(second)   
print(sum)  

# If statement
temperature = 30
if temperature > 37: 
    print("It's a hot day")
    print("Drink plenty of water") 
elif temperature > 20:
    print("It's a nice day") 
elif temperature > 10:
    print("It's a bit cold")  
else:
    print("It's cold")  


mass = int(input("Enter your mass: ")) 
unit = input("(Kg) or (g): ") 
if unit.upper() == "Kg":
    converted = mass / 1000
    print("Mass in Kg: " + str(converted))  
else:
    converted = mass * 1000
    print("Mass in g: " + str(converted))  


x = int(input("Enter a number: ")) 
if x % 2 == 0:
    print("Even number") 
elif x % 2 != 0:
    print("Odd number")
else:
    print("Try again") 

x = int(input("Enter a number: ")) 

if x > 0:
    for i in range(2, x):
        if x % 2 == 0:
            print("Not a prime number")
            break 
        else: 
            print("Prime number")
            break 
else:
    print("Give a positive number") 

x = int(input("Enter your first number: ")) 
y = int(input("Enter your second number: "))
if x > y:
    print("Greater") 
elif x == y:
    print("Equal")
else:
    print("Smaller") 

x = int(input("Enter a number: "))
if x > 0 and x < 10:
    if x < 5:
        print("It's lesser than 5")
    elif x == 5:
        print("It's equal to 5") 
    else:
        print("It's greater than 5") 
elif x > 10:
    print("It's greater than 10") 
elif x == 10:
    print("It's equal to 10") 
else:
    print("Try again")  

mass = int(input("Mass: "))
unit = input("(K)g or (g)s: ") 
if unit.upper() == "K":
    converted = mass * 1000
    print("Mass in gs: " + str(converted))
else:
    converted = mass / 1000
    print("Mass in Kgs: " + str(converted)) 

name = input("Enter your name: ")
print("Hello " + name)
print("Welcome to your 2nd term examination")
exam = input("Are you ready for this exam?: ") 
if exam == "Yes":
    print("Good luck") 
else:
    print("Log out and study your book very well and come back") 

name = input("Type your name: ")
course = input("Department: ")
subjects = ["Biology", "Chemistry", "Physics", "Agricultural science", "Economics"] 
subjects2 = ["Financial Accounting", "Office practice", "Economics", "Commerce", "insurance"] 
subjects3 = ["Government", "Literature-in-English", "Religion studies", "One Nigerian language e.g (Yoruba, Igbo or Hausa)", "History"] 
if course == "science":
    print("Here are your subjects in science class ")
    print(subjects)    
elif course == "commercial":
    print("Here are your subject in commercial class ")
    print(subjects2)
else:
    print("Here are your subjects in art class ") 
    print(subjects3) 

amount = int(input("Enter amount: ")) 
unit = input("($)s or (#)n: ")
if unit.upper() == "$":
    converted = amount * 480
    print("Amount in #: " + str(converted))  

else:
    converted = amount / 480
    print("Amount in $s: " + str(converted)) 

grade = 50
if grade >= 70:
    print("A") 
elif grade >= 61:
    print("B")
elif grade >= 51:
    print("C")
elif grade >= 41:
    print("D")
elif grade >= 31:
    print("E")
else:
    print("F") 


# Question 1
score = 0
question1 = input("What is the addition of 1 and 1? \na. 3 \nb. 2 \nc. 4 \nAnswer: ") 
if question1 == "b" or question1 == "2":
    print("\n")  

question2 = input("What is the subtraction of 10 and 7? \na. 3 \nb. 4 \nc. 5 \nAnswer: ") 
if question2 == "a" or question2 == "3":
    print("\n") 

question3 = input("What is the mulitiplication of 2 and 2? \na. 2 \nb. 3 \nc. 4 \nAnswer: ") 
if question3 == "c" or question3 == "4":
    print("\n") 

if question1 == "b" or question1 == "2":
    score += 1
if question2 == "a" or question2 == "3":
    score += 1
if question3 == "c" or question3 == "4":
    score += 1 
if score <= 1:
    print("Your score is", score, "\nYou suck!")
elif score == 2:
    print("Your score is", score, "\nYou went ok.")
else:
    print("Your score is", score, "\nYou are awesome!")   
