try:
   x = 1/0
     
except ZeroDivisionError:
    print("zero division erroe")
except NameError:
    print("y is not defined")    



def inputAlphabetOnly(name):
    while True:
        user_input = input(name)
        if user_input.isnumeric():
            return user_input
        else:
            print("invalid input, please enter alphabets only")
name = inputAlphabetOnly("enter your name: ") 
print(f"hellp,{name}!")          
