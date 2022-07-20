# fibonacci series
# 0, 1, 1, 2, 3, 5, , 8,... n

user_input = int(input('Enter the Last value until you want the series : '))
a = 0
b = 1
c = 0
print (a)
while c < user_input:
     a = b
     b = c
     c = a+ b
     print(c, end = " ")
