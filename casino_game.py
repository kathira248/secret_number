message = "Welcome to our casino"
print message

secret_number = 742
secret_number_int = int(secret_number)

guess_int = int(raw_input("Try to guess the secret number: "))

"""Alternativ in 2 Schritten um sicherzustellen dass es eine Ganzzahl ist
guess = raw_input("Guess a secret number: ")
guess_int = int(guess)"""

if guess_int <= (secret_number - 1):
    print "Sorry, this is not the correct number. Please try again. Hint: Try a higher number"

elif guess_int >= (secret_number + 1):
    print "Sorry, this is not the correct number. Please try again. Hint: Try a smaller number"

else:
    print "Congratulation, you nailed it!!"

"""
Alternativ:
if guess_int == secret_number:
    print "Congratulation, you nailed it"

if guess_int <= (secret_number - 1):
    print "Sorry, this is not the correct number. Please try again. Hint: Try a higher number"

if guess_int >= (secret_number + 1):
    print "Sorry, this is not the correct number. Please try again. Hint: Try a smaller number"
"""




