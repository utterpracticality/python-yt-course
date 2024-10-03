# Myers-Briggs Personality Test in Python 

print("Welcome to the Myers-Briggs Personality Test!\n")

# Initialize scores
extroversion = 0
introversion = 0
sensing = 0
intuition = 0
thinking = 0
feeling = 0
judging = 0
perceiving = 0

# Question 1
print("When you are at a party, do you:")
print("1. Interact with many, including strangers")
print("2. Interact with a few, known to you")
answer = input("Enter the number of your choice: ")
if answer == "1":
    extroversion += 1
else:
    introversion += 1

# Question 2
print("\nAre you more:")
print("1. Realistic than speculative")
print("2. Speculative than realistic")
answer = input("Enter the number of your choice: ")
if answer == "1":
    sensing += 1
else:
    intuition += 1

# Question 3
print("\nIs it worse to:")
print("1. Have your head in the clouds")
print("2. Be in a rut")
answer = input("Enter the number of your choice: ")
if answer == "1":
    intuition += 1
else:
    sensing += 1

# Question 4
print("\nAre you more impressed by:")
print("1. Principles")
print("2. Emotions")
answer = input("Enter the number of your choice: ")
if answer == "1":
    thinking += 1
else:
    feeling += 1

# Question 5
print("\nAre you more drawn toward the:")
print("1. Convincing")
print("2. Touching")
answer = input("Enter the number of your choice: ")
if answer == "1":
    thinking += 1
else:
    feeling += 1

# Question 6
print("\nDo you prefer to work:")
print("1. To deadlines")
print("2. Just whenever")
answer = input("Enter the number of your choice: ")
if answer == "1":
    judging += 1
else:
    perceiving += 1

# Question 7
print("\nDo you tend to choose:")
print("1. Rather carefully")
print("2. Somewhat impulsively")
answer = input("Enter the number of your choice: ")
if answer == "1":
    judging += 1
else:
    perceiving += 1



# Determine personality type
personality_type = ""

if extroversion > introversion:
    personality_type += "E"  
else:
    personality_type += "I"
 
if sensing > intuition: 
    personality_type += "S"
else: 
    personality_type += "N"

if thinking > feeling:
    personality_type += "T"  
else:
    personality_type += "F"

if judging > perceiving:
    personality_type += "J"  
else:
    personality_type += "P"

print(f"\nYour Myers-Briggs personality type is: {personality_type}")
