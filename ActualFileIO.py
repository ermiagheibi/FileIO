#long story short this is code hs but like megamind, so just take a look and mess around and you will understand it.
user = input("Do I have a deal for you, as long as you say yes, Ill show you all the info for this file! Tell me, yes or no? ") #asks user for yes or no and stores it
if user == "no":
    print("Thats a shame! ")
if user == "yes":
    code = open("Shrek.txt")
    print("Name of the file: ", code.name) #gives file name
    print("closed or not: ", code.closed) #shows if file is open or closed
    print("Opening Mode: ", code.mode) #shows the mode the file is in


user = input("Yo, you can  add whatever you want to the end of this shrek script!!! Just type what! ") #asks for input
said = user #transfers the variable "user" into a new one called "said" which is used in the if statement following this line
user = input("Ok, nice, are you ready to do it? Type yes or no! ") #makes new user essentially, asks and stores the users yes or no answer
if user == "yes":
    code = open("Shrek.txt", "a") #a is for append
    code.write(said) #its is write(then whatever the user said that is now in the said variable
    print ("Okay, after this code is over, ill add it!")


user = int(input("Ya wanna be a cool kid and read as much of the script as you like? Just tell me how many bytes and Ill make it happen! ")) #it is int() because the input by the user will be numbers
numbytes = user #transfers the variable "user" into a new one called "numbytes" which is used in the if statement following this line
user = input("Alrighty then, just confirm by saying yes and ill make sure tracy the turtle works fast to ensure you can read your desired amount of the script! You can also say no but dont: ")
if user == "no":
    print("Oh well, that wasn't great! Well go on ahead, next question")
if user == "yes":
    code = open("Shrek.txt", "r+")#r is for read, obviously
    read = code.read(numbytes); #makes variable "read" equal to however many bytes the user inputted that is being read and in the next line proceeds to print it out so the user can see
    print(read)


user = input("This is essentially a thanos snap, if you say yes, all of shrek dies, but if you say no, they all live happily ever after which is good so do that instead of yes. What is your choice: ")
if user == "yes":
    code = open("Shrek.txt", "w")#w is write
    code.write("Look what you've done, Fiona left Shrek, donkey got married to the dragon and you just messed up the whole story. Next time, I wont let you be the user of my code :( ")


#https://www.imsdb.com/scripts/Shrek.html                 -- is the link to the shrek script
#https://docs.google.com/presentation/d/1ExCW7I8Em44Cc64bLCT5bwJNJdmYjDGQkbw9w9t7iII/edit?usp=sharing                   -Slides link

