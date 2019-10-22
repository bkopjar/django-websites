a = int(input("How many Fibonnaci numbers do you want to generate?: "))

def fibonacci(a):
    
    if (a == 0 or a == 1 or a == 2):
        return(1)
    else:
        return fibonacci(a-1) + fibonacci(a-2) 

print(fibonacci(a))  