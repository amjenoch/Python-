print("Remplissez ce formulaire pour connaitre votre offre")
Age=int(input("Quel est votre age (Ans) : "  ))
Permis=int(input("Depuis combien d'annees avez vous votre permis ? : "))
Accident=int(input("Combien de fois avez vous provoquer un accident ? :"))
fidelite=int(input("Nombres d'annees que vous etes assurer chez nous : "))
if Age<25:
    if Permis<2 and Accident==0 and fidelite<5:
     print("Votre tarif est rouge")
    elif Permis>2 and Accident==0 and fidelite<5:
        print("Votre tarif est orange")
    elif Permis>2 and Accident==1 and fidelite<5:
        print("Votre tarif est rouge")
    else:
        print("Conditions non requises pour etre assurer")

if Age>25:
    if Permis>2 and Accident==0 and fidelite<5:
     print("Votre tarif est vert")
    elif Permis > 2 and Accident == 1 and fidelite<5:
     print("Votre tarif est orange")
    elif Permis> 2 and Accident==2 and fidelite<5:
        print("Votre tarif est rouge")
    elif Permis<2 and Accident==0 and fidelite<5:
        print("Votre tarif est orange")
    elif Permis<2 and Accident==1 and fidelite<5:
        print("Votre tarif est rouge")
    else:
        print("Conditions non requises pour etre assurer")

if Age<25 and ((Permis < 2 and Accident == 0) or (Permis>2 and Accident==1)) and fidelite>5:
    print(" Pour vous remerciez de votre fidelite ,vous passez du tarif rouge au tarif orange :)")
if Age>25 and ((Permis> 2 and Accident==2) or (Permis<2 and Accident==1)) and fidelite>5:
    print(" Pour vous remerciez de votre fidelite ,vous passez du tarif rouge au tarif orange :)")
if Age<25 and (Permis>2 and Accident==0) and fidelite>5:
    print(" Pour vous remerciez de votre fidelite ,vous passez du tarif orange au tarif vert :)")
if Age>25 and ((Permis > 2 and Accident == 1) or (Permis<2 and Accident==0)) and fidelite>5:
    print(" Pour vous remerciez de votre fidelite ,vous passez du tarif orange au tarif vert :)")
if Age > 25 and (Permis>2 and Accident==0) and fidelite > 5:
    print(" Pour vous remerciez de votre fidelite ,vous passez du tarif vert au tarif bleu :)")

