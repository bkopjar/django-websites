

def max_of_three(a,b,c):
     max=0
     if a>b:
         max=a
         if a>c:
             max=a
         else:
             max=c
     else:
          if b>c:
             max=b
          else:
             max=c
     return max

print("Max is: " +str(max_of_three(300, 400, 200)))