# ups: ispisi sve brojeve od 1 do 100 (uključujući i 1 i 100), svaki broj 
# u novi red, ali umjesto broja koji je djeljiv sa 3 ispiši "ups", a umjesto 
# broja koji sadrzi broj 3 ispisi hops
#
# Ukoliko broj i sadrži 3 i djeljiv je sa 3 (npr. broj 30), ispiši "upshops"

number = range(1,100)

for x in number:
    if x % 3 == 0 and '3' in str(x):
        print("upshops")
    elif x % 3 == 0:
        print("ups")
    elif '3' in str(x):
        print("hops")