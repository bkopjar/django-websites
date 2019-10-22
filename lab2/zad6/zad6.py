string = input("Input new string: ")
string = str(string)
reverse = string[::-1]

if(reverse == string):
        print("It is a palindrome")
else:
    print("It is not a palindrome")