# task 01
def firstOne(tab):
    return tab[0]

print(firstOne([5,6,7,8,9]))

# task 02   

def lastOne(tab):
    return tab[len(tab)-1]

print (lastOne([5,6,7,8,9,]))

# task 03 

def appendTab(tab, nb):
    return tab.append(nb)

print(appendTab([5,6,8,9], 19))

# task 04

def displayList(tab):
    for element in tab: print(element)
    return None

print(displayList([5,6,90,8]))

# task 05

def removeElementLast(tab: list):
    tab.remove(tab[len(tab)-1])
    return tab

print(removeElementLast([5,6,6]))

#  task 06  

def addElementAtBeggining(tab: list, nb):
    tab.insert(0, nb)
    return tab

print(addElementAtBeggining([1,2,4],0))

# task 07

def displayFrom2To5(tab):
    return tab[2:6]

print(displayFrom2To5([1,2,3,4,5,6,7,8,9]))

# task 08   

def displayEndTab(tab:list):
    tab.reverse()
    for element in tab: print(element)
    return None

print(displayEndTab([12345,123456,1234567]))

# task 09

def oneOfTwo(tab):
    return tab[::2]

print(oneOfTwo([1,2,3,4,5,6,7,8]))

# task 10

def add17Elements(tab, elements):
    for element in elements: tab.append(element)
    return tab

print(add17Elements([0,12,24],[1,2,3,998,78,47,45,32,0,7985,146,369,745,478965,12,22]))

# task 11 

# The code add a element of a list into a list 