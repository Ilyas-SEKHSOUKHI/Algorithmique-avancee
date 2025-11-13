print("---------------------------Ratios Boursiers---------------------------")
'''
1. PER (Price Earnings Ratio)
Formule : PER = Prix de l'action / Bénéfice par action (BPA)
Ce que ça mesure : Combien les investisseurs payent pour 1 unité de bénéfice.
Interprétation :
  - PER > 20 : action chère ou forte croissance attendue
  - PER 10-20 : action normalement valorisée
  - PER < 10 : action bon marché ou croissance faible
Valeurs à entrer : Prix de l'action, Bénéfice par action
'''
def PER(): #PER Function
    print("---------------PER Price Earnings Ratio---------------")
    print("Valeurs à entrer : Prix de l'action, Bénéfice par action")
    print("Ce que ça mesure : Combien les investisseurs payent pour 1 unité de bénéfice.")
    Prix_de_laction = float(input("Entrez le prix de l'action : "))
    bpa = float(input("Entrez le benefice par action : "))
    per = Prix_de_laction/bpa
    print("Price_Earning_Ratio --> ",per)
    if per>20:
        print("action chère ou forte croissance attendue")
    elif per>10 and per<20:
        print("action normalement valorisée")
    else:
        print("action bon marché ou croissance faible")
'''
2. ROE (Return on Equity)
Formule : ROE (%) = Résultat net / Capitaux propres * 100
Ce que ça mesure : Rentabilité des capitaux propres.
Interprétation :
  - ROE > 15% : très rentable
  - ROE 10-15% : rentable
  - ROE < 10% : peu rentable
Valeurs à entrer : Résultat net, Capitaux propres
'''
def ROE(): #Return on Equity
    print("---------------ROE (Return on Equity)---------------")
    print("Valeurs à entrer : Résultat net, Capitaux propres")
    print("Ce que ça mesure : Rentabilité des capitaux propres.")
    Resultat_net = float(input("Entrez Resultat Net : "))
    Capitaux_propres = float(input("Entrez Capitaux Propres : "))
    roe = Resultat_net/Capitaux_propres*100 
    print("Return on Equity --> ",roe)
    if roe > 15:
        print("très rentable")
    elif roe>10 and roe<15:
        print("rentable")
    else:
        print("peu rentable")
'''
3. ROA (Return on Assets)
Formule : ROA (%) = Résultat net / Total des actifs * 100
Ce que ça mesure : Efficacité de l'entreprise à utiliser ses actifs pour générer du profit.
Interprétation :
  - ROA > 10% : bonne utilisation des actifs
  - ROA 5-10% : moyenne
  - ROA < 5% : faible efficacité
Valeurs à entrer : Résultat net, Total des actifs
'''
def ROA():
    print("---------------Return on Assets---------------")
    print("Valeurs à entrer : Résultat net, Total des actifs")
    print("Ce que ça mesure : Efficacité de l'entreprise à utiliser ses actifs pour générer du profit.")
    Resultat_net = float(input("Entrez Resultat Net : "))
    Total_des_actifs = float(input("Entrez Total des actifs : "))
    roa = Resultat_net / Total_des_actifs * 100
    print("Return on Assets --> ",roa)
    if roa>10:
        print("bonne utilisation des actifs")
    elif roa>5 and roa<10:
        print("moyenne")
    else:
        print("faible efficacité")
'''
4. Ratio d'endettement
Formule : Ratio d'endettement = Dettes totales / Capitaux propres
Ce que ça mesure : Niveau de dettes par rapport au capital propre.
Interprétation :
  - Ratio < 1 : entreprise peu endettée, faible risque
  - Ratio ≈ 1 : équilibre dettes/capitaux
  - Ratio > 2 : entreprise très endettée, risque élevé
Valeurs à entrer : Dettes totales, Capitaux propres
'''
def Ratio_endettement():
    print("---------------Ratio d'endettement---------------")
    print("Valeurs à entrer : Dettes totales, Capitaux propres")
    print("Ce que ça mesure : Niveau de dettes par rapport au capital propre.")
    Dettes_totales = float(input("Entrez Dettes totales : "))
    Capitaux_propres = float(input("Entrez Capitaux propres : "))
    Ratio_endettement = Dettes_totales / Capitaux_propres
    print("Ratio_endettement --> ",Ratio_endettement)
    if Ratio_endettement<1:
        print("entreprise peu endettée, faible risque")
    elif Ratio_endettement>2:
        print("entreprise très endettée, risque élevé")
    else:
        print("équilibre dettes/capitaux")
'''
5. Ratio de liquidité
Formule : Liquidité = Actifs circulants / Dettes à court terme
Ce que ça mesure : Capacité de l'entreprise à payer ses dettes à court terme.
Interprétation :
  - Ratio > 1 : solvable à court terme
  - Ratio ≈ 1 : juste capable de payer
  - Ratio < 1 : risque de manque de liquidité
Valeurs à entrer : Actifs circulants, Dettes à court terme
'''
def Ratio_de_liquidite():
    print("---------------Ratio de liquidité---------------")
    print("Valeurs à entrer : Actifs circulants, Dettes à court terme")
    print("Ce que ça mesure : Capacité de l'entreprise à payer ses dettes à court terme.")
    Actifs_circulants = float(input("Entrez Actifs circulants : "))
    Dettes_a_court_terme = float(input("Entrez Dettes a court terme : "))
    Ratio_de_liquidite = Actifs_circulants/Dettes_a_court_terme
    print("Ratio_de_liquidite --> ",Ratio_de_liquidite)
    if Ratio_de_liquidite>1:
        print("solvable à court terme")
    elif Ratio_de_liquidite<1:
        print("risque de manque de liquidité")
    else:
        print("juste capable de payer")

'''
PER()
ROE()
ROA()
Ratio_endettement()
Ratio_de_liquidite()
'''
def menu():
    print("\nChoisissez un ratio à calculer :")
    print("1. PER")
    print("2. ROE")
    print("3. ROA")
    print("4. Ratio d'endettement")
    print("5. Ratio de liquidité")
    print("0. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        PER()
    elif choix == "2":
        ROE()
    elif choix == "3":
        ROA()
    elif choix == "4":
        Ratio_endettement()
    elif choix == "5":
        Ratio_de_liquidite()
    elif choix == "0":
        print("Fin du programme.")
        exit()
    else:
        print("Choix invalide.")

while True:
    menu()
