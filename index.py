# Multiples 
# Part ! - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

for i in range(1, 1000):
    if i % 2 != 0:
        print i
        
# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for j in range(5, 1000000):
    if j % 5 == 0:
        print j
        
# Sum List

list = [1, 2, 5, 10, 255, 3]
add = 0
for i in list:
    add += i
print add

# Average List

list = [1, 2, 5, 10, 255, 3]
add = 0
avg = 0
for i in list:
    add += i
    avg = add / len(list)
print avg