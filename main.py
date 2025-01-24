import random

# Getting choices
def perfect_guess():
    print("Welcome to The Perfect Guess!") 
    comp_choice = random.randint(0, 11)
    counter = 0
    while True:
        user_choice= int(input("Enter a number from 0-10 : "))
        counter += 1
      
        # validate the input
        if (user_choice<0 or user_choice>10) :
            print("Please guess a number between 0 and 10!")
            continue
        # condition execution
        if user_choice == comp_choice :
            print(f"Your guess was correct. You guessed the number in {counter} attempts.")
            break
        elif user_choice > comp_choice :
            print("Lower number please!")
        else :
            print("Higher number please!")
          
# Function call         
perfect_guess()
