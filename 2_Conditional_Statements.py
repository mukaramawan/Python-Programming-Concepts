#The Conditional Statements is used for Decision-Making.
# We have two types for Conditional Statements 1- IF-ELSE 2- Match-Case 

# Both use for Decision-Making and checking the Condition.

# 1- IF-ELSE

name = input("Enter your Name: ")
if name == "Mukaram":
    print(f"We already have your record: {name}")
else:
    print(f"Hi, {name}")



# 2- Match-Case

fruit = input("Enter a fruit (Apple, Banana, Grape, Orange) to know benefits of each fruit: ").lower()

# The lower() function converts the user input to lowercase, ensuring consistency for match-case decisions.

match fruit:
    case "apple":
        print("They are good for heart health and packed with fiber.")
    case "banana":
        print("They are a great source of potassium and help with digestion.")
    case "grape":
        print("They are rich in antioxidants and good for hydration.")
    case "orange":
        print("They are high in vitamin C and boost the immune system.")
    case _:
        print("Unknown fruit. Please enter apple, banana, grape, or orange.")