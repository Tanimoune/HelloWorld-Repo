mylist = {"Jake":10, "Brooke":20, "Chase":30, "CJ":40, "Bayan":50}
# add items
mylist["Sam"]=78
mylist["Marrie"]=92
mylist["Ria"]=88

#length
print(len(mylist))
print(mylist)

#average
average = sum(mylist.values()) / len(mylist)
print("The average is:", average)

#number of student above class average
above_average = 0
for value in mylist.values():
    if value > average:
        above_average += 1
print("The number of students with values above the average is:", above_average)

# Top student of the class
top_student = max(mylist, key=mylist.get)

print("The top student of the class is:", top_student)

#Udpate Sam' value to 95
mylist["Sam"] = 95
print(mylist)


