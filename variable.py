

# l'opérateur d'affectation = permet d'affecter une valeur dans une valeur 
my_text1 = "ceci est une chaîne de caractères"
my_text2 = 'ceci est aussi une chaîne de caractères'
my_text3 = "j'aime les pommes\nmais asssi les poires"

print(my_text1)
print(my_text2)
print(my_text3)

# integer, nombre entier 
my_number1 = 142
my_number2 = -65

print(my_number1 - my_number2)

# float, nombre a virgule flottante 
my_number3 = 3.14
my_number4 = -2.71
my_number5 = 0.0 

print(my_number3)
print(my_number4)
print(my_number5)

print(type(my_number5))

# les booleans 

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# valeur nulle 

my_none = None 
print(my_none)
print(type(my_none))

# permutation de la valeur des variables methode 1

a = 123 
b = 42
a, b = b, a 

print(a, b)

# permutation de la valeur des variables methode 2

a = 10
b = 2 

c = a 
a = b
b = c
print(a, b)

# ctrl K T = ouvrir la gestion des thèmes 

# cmd touch pour créer un fichier depuis le terminal 
# cmd mkdir pour créer un dossier depuis le terminal 


# le Transtypage : passer une variable d'un type a un autre (ex : un int en str)
test = 123
test = str(test)
print(type(test))

foo = 2.5 
a = int(foo)
b = foo - a 
print(a, b)