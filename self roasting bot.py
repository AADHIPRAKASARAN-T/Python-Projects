import random
roasts=[
    "{name}, even your rfrlection roolws its eyes at you.",
    "{name}, you're the kind person who claps when the movie ends... at home.",
    "{name}, your debugginf technique is mostly cryin.",
    "{name},you're so good at procrastinating, you delay your dreams.",
    "{name}, even wi-fi avoids when you're in a zoom metting.",
    "{name}, you have a bright future—if the sun explodes.",
    "{name}, if you were a variable, you'd always be 'None'.",
    "{name}, you're the reason rubber ducks get confused.",
    "{name}, your typing speed is measured in geological time.",
    "{name}, even spell check gave up on you."
    ]
def generate_roast(name):
    roast=random.choice(roasts)
    return roast.format(name=name)
print("Welccome to Self-Roasting Bot!")
user_name=input("Enter your name:")
while True:
    print("\nGenerating roast....")
    print(generate_roast(user_name))
    again=input("\nRoast you again(yes or no):").lower()
    if again!='yes':
        print("\nBye, {name}! Remember:you are awesome even if your code says otherwise".format(name=user_name))
        break
    
