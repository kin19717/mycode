#/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)


list = [0, 3, 5, 7, 9, 3, 9]
print(list)
list.insert(2,4) #insert 4 in the list in the third position
print(list)
list.remove(9) #remove the interger 9
print(list)
list.pop(2) #pop out the third postion in th list
print(list)
list.reverse() #reverse order
print(list)
list2 = list.copy() #copy list 1 to list 2
print("this is list2", list2)
print(list2.count(3)) #print how many 3s in the list
