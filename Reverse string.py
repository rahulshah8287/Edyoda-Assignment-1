#reverse string :

user_input  = input("Enter the string : ") 
result = ''

for i in user_input:
    result = i + result

print (result)