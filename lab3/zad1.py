grades = { "Pero": [2,3,3,4,3,5,3],
           "Djuro" : [4,4,4],
           "Marko" : [3,3,2,3,5,1]
           }
           
# Ispisi ime studenta koji ima najvisi prosjek. Zadatak treba proci kroz 
# sve studente, izracunati prosjek i ispisati ime studenta s navisim prosjekom.

# -- vas kod ide ispod -- #

def average(items):
    total = float(sum(items))
    return total/len(items)

max = 0
maxv = ""
br = 0
for key,values in grades.items():
    avg=0
    for element in values:
        avg += element
        br +=1
    avg = avg/br
    if max<avg:
        max=avg
        maxv=key
    br = 0
print(max, maxv)