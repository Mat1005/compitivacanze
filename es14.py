
coppia = int(input("Di quante coppie di numeri vuoi vedere la somma o la differenza?"))
for n in range(1,coppia + 1):
    a = int(input("inserisci il valore di a"))
    b = int(input("inserisci il valore di b"))
    if a*b > 10:
        if a < b:
            print("la differenza è ",b-a)
        else:
            print("la differenza è ",a-b)
    if a*b <= 10:
        print("la somma è ",a+b)
