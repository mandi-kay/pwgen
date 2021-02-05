import random, string
                            #importing libraries
                            #set variable, it needs to be an integer not a string. Must be numerical input response.
                            #asking for user input to return as a string, then convert to an integer
password_length = int(input("How long does your password need to be? Please tell me in numbers."))
                            #variable joining (or concatinating three imported strings)
password_characters = string.ascii_letters + string.digits +string.punctuation
                            #sets a blank list (of strings, individual characters, but strings)
password = []
                            #sets the script to run 'x' number of times based on the desired length input
for x in range(password_length):
                            #creates the password from zero (adds on to the end of the zero)
    password.append(random.choice(password_characters))
                            #prints the password, taking the list and merging it into a single string
print(''.join(password))

