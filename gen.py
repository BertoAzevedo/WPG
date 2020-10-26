from random import randrange, choice

data = []
words = []

file = open('words.txt', 'r') 
data = file.readlines() 

for line in data:
    words.append(line.strip('\n'))

password = ""

password = str(randrange(20)) + "!" + choice(words) + choice(words).capitalize() + str(randrange(20))

print("Password: " + password)
print("Length: " + str(len(password)))
