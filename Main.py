#Unit 1 Challange 1 Basic Datypes
#Letter counter app
#Taking a users name, a message, and letter returns the number of times that letter appears in the message


print("Welcome to the Letter Counter App")
username = input("What is your name: ")

print("Hello " + username + "!")
print("I will count the number of times that a specific letter occurs in a message.")

message = input("Please enter a message: ")
letter = input("Which letter would you like to count the occourences of: ")

#Make sure that boht capital, and lowercase of each letter is counted as the same
letter.lower()
message.lower()
#Get number of occourences
number = message.count(letter)
number = str(number)
print(username + " your message has " + number + " " + letter + "'s in it.")

