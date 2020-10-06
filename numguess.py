import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print("AHOY!  l'm thedread pirate roderts,and l have a secret!")
print("lt is a number from 1 to 99. l'11 give you 6 tries.")
while guess != secret  and tries < 6:
    guess = int(input("what's yer guess? "))
    if guess < secret: 
        print( "Too low, ye scurvydog!")
    elif guess > secret:
        print("Too high, landlubber!")

    tries =  tries + 1

if guess == secret:
    print("Avat! ye got it! found my secret, ye did!")
else:
    print("no more guesses! better luck next time,matey")
    print("the secret number was", secret)                
    