# Let s be a string that contains a sequence of decimal numbers separated by commas, 
# e.g., s  = '1.23,3.4,3.123,4.56,5.6,4.678' 
# Write a program that prints the sum of the numbers in s

s  = '1.23,3.4,3.123,4.56,5.6,4.678' 

sum = 0
for c in s:
    for i in '123456789':
        if c==i:
            sum+=int(c)
print(sum)
    