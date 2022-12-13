import random

# if True :
    # print ("la condition est vraie")
    # print ("ce code est executer")

# if False :
    # print ("la condition est faux")
    # print ("ce code n'est pas executer")

# condition_vente = True

# if condition_vente == True :
   # print ("l'utilisateur a accepté les conditon de vente")
# else :
    # print ("l'utilasateur na pas accepter les conditiont de vente") 

# if condition_vente != True :
   # print ("l'utilisateur n'a pas accepté les condition de vente")

# if not condition_vente :
    # print ("l'utilisateur n'a pas accepté les condition de vente")
# else :# if True :
    # print ("la condition est vraie")
    # print ("ce code est executer")

# if False :
    # print ("la condition est faux")
    # print ("ce code n'est pas executer")

# condition_vente = True

# if condition_vente == True :
   # print ("l'utilisateur a accepté les conditon de vente")
# else :
    # print ("l'utilasateur na pas accepter les conditiont de vente") 

# if condition_vente != True :
   # print ("l'utilisateur n'a pas accepté les condition de vente")

# if not condition_vente :
    # print ("l'utilisateur n'a pas accepté les condition de vente")
# else :
   # print ("l'utilisateur a accepté les conditon de vente")

emails = random.randint (0, 100)

# elif c'est la même chose que else if 
   
if emails == 1 : 
    print ("vous avez un nouveau mail")
elif emails > 1 :
    print (f"vous avez {emails} nouveau mail ")
else :
    print ("vous n'avez pas de nouveaux mail")
    

windows_closed = bool ( random.randint(0, 1))
electicity_off = bool ( random.randint(0, 1))

print (f'{windows_closed=}')  # String Formatting
print (f'{electicity_off=}')


if windows_closed and electicity_off :
    print ("les fenetre sont fermées")
    print ("l'electriciter est fermées")
elif not windows_closed and electicity_off : 
    print ("les fenetre sont pas fermées")
    print ("l'electriciter est fermées")
elif windows_closed and not electicity_off : 
    print ("les fenetre sont fermées")
    print ("l'electriciter n'ait pas  fermées")
else :
    print ("les fenetre sont pas fermées")
    print ("l'electriciter n'ait pas fremées")



if emails == 1 : 
    print ("vous avez un nouveau mail")
elif emails > 1 :
    print (f"vous avez {emails} nouveau mail ")
else :
    print ("vous n'avez pas de nouveaux mail")
    

windows_closed = bool ( random.randint(0, 1))
electicity_off = bool ( random.randint(0, 1))

print (f'{windows_closed=}')  # String Formatting
print (f'{electicity_off=}')


if windows_closed and electicity_off :
    print ("les fenetre sont fermées")
    print ("l'electriciter est fermées")
elif not windows_closed and electicity_off : 
    print ("les fenetre sont pas fermées")
    print ("l'electriciter est fermées")
elif windows_closed and not electicity_off : 
    print ("les fenetre sont fermées")
    print ("l'electriciter n'ait pas  fermées")
else :
    print ("les fenetre sont pas fermées")
    print ("l'electriciter n'ait pas fremées")

bank_card = bool(random.randint(0,1))
cash = bool(random.randint(0,1))

print(f'{bank_card = }')
print(f'{cash = }')

if bank_card or cash :
    print("on a un moyen de paiement")

    if bank_card :
        print("on a la carte")

    if cash :
        print("on a du cash")

else :
    print("on a aucun moyen de paiement")


ticket = bool(random.randint(0,1))
vip = bool(random.randint(0,1))
registration = bool(random.randint(0,1))

print(f'{ticket = }' ' ' f'{vip = }' ' ' f'{registration = }')

if (ticket or vip) and registration : 
    print("acces authorized")
else : 
    print("acces not authorized")