# 1 - import the random module
import random

# 2 - create subjects
subjects = [
    "Shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A mumbai Dog",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver From Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
     "at Red Fort",
     "in Hyderabad local train",
     "a plate of samosa",
     "inside parliament",
     "at Ganga ghat",
     "at gateway of india"
]

# 3 start the headline generation loop
while True:
    subjects = random.choice(subjects)
    actions = random.choice(actions)
    places_or_things = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subjects} {actions} {places_or_things}"
    
    print("\n" + headline)
    
    user_input = input("\n Do you want another headline ? (yes/no):").strip()
    if user_input == "no":
        break
    
# print the message
print("Thanks to using the fake news headline generator. Have a fun day!")