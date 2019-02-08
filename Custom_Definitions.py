#gives the probability a coin will flip heads every time when input
#the total number of flips
def prob(number):
    n = 1/(2**int(number))
    print(n)

#takes a string of any length and prints it in reverse order
def reverse_any_string(string):
    new_string = ""
    for letter in string:
        new_string = letter + new_string
    print(new_string)

#calculates the distance in km between the user and lightning when input
#the time in seconds between the lightning flash and the thunder.
def distance(seconds):
    speed_of_sound = 340.29
    dist = (float(speed_of_sound) * float(seconds)) / 1000
    print(dist)

