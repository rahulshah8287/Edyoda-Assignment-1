# number of odd and even numbers in the list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_number = 0
odd_number = 0
for x in numbers :
    if x%2 == 0:
        even_number+=1 
    else:
        odd_number += 1

print(f'Total number of even numbers are {even_number}')
print(f'Total number of odd numbers are {odd_number}')