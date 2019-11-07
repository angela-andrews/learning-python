# Write my own flow game
# In progress

# Stop in Sephora

from sys import exit

def enter_sephora():
    print("starting the function")
    print("Grab a basket.")
    print("Is the new Fenty in Stock???: yes or no")
    
    choice = input("> ")

    if choice == 'yes':
        print("How much cash can you spend?")
        cash = int(input(">$ "))
        
        if cash <= 50:
            print("Tread lightly. Get a gloss or lippy and bounce.")
        else:
            print("Good to go! Let's cop that!")    
    elif choice == 'no':
        print("Do you have any points to use?")
        points = input("> ")

        if points == 'yes':
            print("Ok, keep browsing. Don't go crazy")
        else:
            print("Time to go!")
            done("Today is NOT your day.")
    else:
        print("Let's shop!")
        browsing()

def browsing():
    print("Just browsing.....")


def done(why):
    print(why, "Stack them points!")
    exit(0)

def start():
    print("You're walking in the mall and you pass a Sephora.")
    print("Do you need anything? yes or no")

    choice = input("> ")

    if choice == "yes":
        enter_sephora()
    elif choice == "no":
        print("That's OK. Just browse for a few minutes.")
        enter_sephora()
    else:
        done("Is that even an answer???")



start()

