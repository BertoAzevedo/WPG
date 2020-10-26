#!/usr/bin/python

import sys, getopt
from random import randrange, choice

def main(argv):
    numberOfWords = 2
    numberOfPasswords = 5

    try:
        opts, args = getopt.getopt(argv,"h:w:p:")
    except getopt.GetoptError:
        print("test.py -w <number of words in the password> -p <number of passwords to generate>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == ("-h"):
            print("test.py -w <number of words in the password> -p <number of passwords to generate>")
            sys.exit()
        elif opt in ("-w"):
            numberOfWords = int(arg)
        elif opt in ("-p"):
            numberOfPasswords = int(arg)

    data = []
    words = []
    password = ""

    file = open('words.txt', 'r') 
    data = file.readlines() 

    for line in data:
        words.append(line.strip('\n'))

    for i in range(numberOfPasswords):
        password = ""
        password = str(randrange(20)) + "!"

        for i in range(numberOfWords):
            if(i == 0):
                password += choice(words)    
            else:
                password += choice(words).capitalize()

        print(password)

if __name__ == "__main__":
   main(sys.argv[1:])
