import time

#created a state list so the user will have to use something from this last
state_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', \
'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',\
'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',\
'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',\
'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

start_time = time.time()

states = input("Test your geographical skills! Name 5 US states.... ").split()

while not all(state in state_list for state in states):
    print("Please enter a US STATE.")
    states = input("Test your geographical skills! Name 5 US states: ").split() # This split is seperating the whitespace in an answer
#len is returning the length of the string
if len(states) != 5:
    print("You didnt enter five states!")
else:
    end_time = time.time()
    final_time = end_time - start_time

    if final_time > 15:
        print("Damn you're slow!")
    else:
        print("That was impressive!")

    print("It took you", final_time, "seconds.")



