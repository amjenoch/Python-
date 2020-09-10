x=6
from random import randint
a=randint(1,100)
print("Devine le chiffre entre 1 et 100")
print("Tu as seulement 6 essais")
while x!=0:
   print(x,"essais")
   n=int(input("Devine? . "))
   x+=-1
   if n==a:   
     print("Tu as trouve...")
     print("Bien joue")
     restart=int(input("1=oui, 0=non \n "))
     if restart==1:
        x=6
        a=randint(1,100)
        print("___________\n   ")
     else:
        print("A bientot")
        break
   elif x==0:
     print("Tu as perdu")
     print("Le numero etait")
     print(a)
     print("Veux tu rejouer? ")
     restart=int(input("1=oui, 0=non \n "))
     if restart==1:
        x=6
        a=randint(1,100)
        print("___________\n   ")
     else:
        print("A bientot")
        break
   elif n<1 or n>100:
     print("Choisis un chiffre entre 1 et 100 seulement")
     x+=1
   elif n<a:
     print("Plus grand")
   elif n>a:
     print("Plus petit")