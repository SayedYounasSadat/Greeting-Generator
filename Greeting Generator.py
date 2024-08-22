print("Hey there, welcome to my AI powered greeting generator machine. I will ask you some simple questions and generate a cool greeting for you! Would You like to?")

firstresponse = input("Do you want me to create this for you? ")

if firstresponse == "Yes":
    print("Here you go: Answer these questions to get started!")

name = input("What is your name? ")
hobby = input("What is your hobby? ")
repeat = input("How many times do you want me to print this for you? ")

greeting = "Hello Mr. " + name + ", and welcome to my site! Your " + hobby + " is amazing. I hope you enjoy it!\n"

for i in range(int(repeat)):
    print(greeting)