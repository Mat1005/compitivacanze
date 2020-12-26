print("Salve, questo programma calcola il valore dell'incognita x di un equazione ax + b = 0")
a = int(input("inserire il valore di a"))
b = int(input("inserire il valore di b"))

if a == 0 and b == 0:
    print("L'equazione è indeterminata.")
if a == 0 and b>0 or b<0:
    print("L'equazione è impossibile.")
if a <0 or a>0 and b == 0:
    print("x=0")
if a <0 or a>0 and b>0 or b<0:
    print("x=",-b/a)