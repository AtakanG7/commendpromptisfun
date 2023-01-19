#I'm going to be solving questions I solved in Racket. Let's get started!

#Create a funtion called addToList which simply adds the given value to the end of the list.

def addToList(alist, input):
    a = alist.append(input)
    return alist

process= addToList([2,3,4], "Atakan")
print(process)