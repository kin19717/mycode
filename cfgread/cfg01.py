#!/usr/bin/env python3
count = 0
with open(input("Which file you want to load: "), 'rU')as cfgfile:
    cfglist = cfgfile.readlines()
    print(cfglist)

for i in cfglist:
    count +=1
    print(i, end="")
print("the number of lines: ", count)




#with open("vlanconfig.cfg", "r") as cfgfile:
#    print(cfgfile.read())
#count = 0
#with open("vlanconfig.cfg", "r") as cfgfile:
#    cfglist = cfgfile.readlines()
#    print(cfglist)
#
#for i in cfglist:
#    count +=1
#    print(i, end="")
#print("the number of lines: ", count)
#for i in cfglist:
    #print(i.strip())

