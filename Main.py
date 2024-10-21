print("Hello World")

myList = ["Curtis", "Bouthayna", "Andrei", "yes", "michaeljackson"]
myListNumber = [34, 2555, 100]
myMixedList = [ "Mariza", 500, [6,7,8] ]

print(len(myList))
print(myMixedList[0])
print(myMixedList[1])
print(myMixedList[2])

print(myList[0][2])

print(myList)
myList.append("Mariza")
print(myList)
#this is how you add stuff to the list, it will added it at the end, so in order


myList.remove("Andrei")
print(myList)
#if it doesnt exist, it will give an error

print(myList.pop(0))
#this is how you pop/show

myList.insert(0, 'name')
print(myList)
#this is to add things to the list

myMixedList[:2] = [24]
print(myMixedList)
#this is how you replace stuff from the list

print( sorted(myList, key=len) )
#this puts the list in order of length from shortest to longest

print( sorted(myList, reverse=True) )
#this reverses the order, alphabetically but inverse

if "yes" in myList:
    print("item in list")
else:
    print("not in list")
print("=========================================")

for i in myListNumber:
    print(i, end=" ")

print(" ")
print("=========================================")


for i in range(5,10,2):
    print(i)
print(" ")
print("=========================================")

lisFromLoop = []
for i in range(10):
    lisFromLoop.append(i**2)

print(lisFromLoop)

print(" ")
print("=========================================")

lisFromLoop = []
for i in range(10):
    lisFromLoop.append(i%3)

print(lisFromLoop)

print(" ")
print("=========================================")

lisFromLoop = []
for i in range(10):
    lisFromLoop.append(i%3)
listComprehension = [ i**3 for i in range(10)]

print(listComprehension)

print(" ")
print("=========================================")

for i in myList:
    if i == "Andrei":
        print("I found it")

print( )
print("=========================================")

counter = 0
while counter < 5:
    print("Hello")
    print(counter)
    if counter == 3:
        break
    counter += 1
else:
    print("i finished counting")