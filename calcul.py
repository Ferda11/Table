reponse='o'
while(reponse=='o'or reponse=='O'):
    try:
        nombre=int(input("antre yon nonb ki jwenn li ant 1 ak 10 :"))
        while(nombre<1 or nombre>10):
            print("Le nombre doit être compris entre 1 et 10")
            nombre=int(input("Entrer un nombre compris entre 1 et 10 :"))
        print("la table de multiplication de "+str(nombre)+" est:")
        n=[1,2,3,4,5,6,7,8,9,10]
        for i in n:
            produit=int(nombre)*i
            print(str(nombre)+"x "+str(i)+"="+str(produit))
    
        reponse=input("Voulez-vous continuer?O/o pour oui/N/n pour non :")
    except ValueError:
        print("Entrer un nombre entre 1 et 10")
    
    while(reponse!='o'and reponse!='n'and reponse!='N'and reponse!='O'):
        reponse=str(input("la reponse doit-être O/o pour oui/N/n pour non : "))
    if(reponse=='n'or reponse=='N'):
        print("***Fin de programme...Merci!!***")
        exit
    
    
    
    
    