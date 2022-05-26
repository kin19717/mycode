with open("text.txt") as myfile:
    for line in myfile:
        print(line)


with open("newtxt.txt", "w") as myfile2:
    myfile2.write("Print this line too!\n")
