# task 01

def multipleElement(tab):
    res = 1
    for element in tab:
        res *= element
    return res

print(multipleElement([2,4,6]))

# task 02

print([x + 10 for x in [3, 2, 6, 7, 1, 4]]) # add 10 to each element

# task 03

print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))) # add square numbers to each element1

# task 04

def minMaxTab(tab):
    return (min(tab), max(tab))
    
print(minMaxTab([12,89,76,3,1029]))

# task 05

def displayAllElementSmallerThan7(tab):
    for element in tab:
        if element < 7:
            print(element)

print(displayAllElementSmallerThan7([12,8,9,1,4,10]))

# task 06

def sortDescending(tab: list):
    tab.sort(reverse=True)
    return tab

print(sortDescending([78,1,3,56,29,13,7]))

# task 07 

[x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]] # Si l'element est divisible par deux alors l'element est divisé par deux sinon on applique une multiplication de 2 sur l'élément

# task 08 

list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])) # On filtre la liste en fonction d'une condition, si l'element est supérieur a 10 il reste dans la liste

# task 09

print([*enumerate([42, 3, 4, 18, 3, 10])]) # Pour le tableau, pour chaque element, on transforme en un tuple avec en premier un id qui s'incrémente a chaque élement, et en second la valeur de l'élément

# task 10

first_name = [ " Jackie " , " Bruce " , " Arnold " , " Sylvester " ]
last_name = [ " Stallone " , " Schwarzenegger " , " Willis " , " Chan " ]
magic = [* zip ( first_name , last_name [:: -1]) ]
print ( magic [0])
print ( magic [3])
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])

# Cette méthode transforme en un tuple et prend et par du début élement par élement, le second argument en partant de la fin 

