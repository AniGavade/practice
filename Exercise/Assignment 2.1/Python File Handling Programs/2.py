# Python program to read character by character from a file

file = open('exercise.txt', 'r')

while 1:
    char = file.read(1)
    if not char:
        break
    print(char)
file.close()

