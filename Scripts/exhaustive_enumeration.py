# Find the cube root of a perfect cube
# x = int(input('enter a number: '))
# ans = 0
# while ans**3 < abs(x):
#     ans += 1
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is ', ans)

# write a program that asks the user to enter an integer and prints two integers, root and pwr, 
# such that 1 < pwr < 6 and root**pwr equal to the integer entered by the user. If no such pair exist
# print a message to that effect

num = int(input("Enter an integer: "))
found = False

    # Check powers from 2 to 5 (since 1 < pwr < 6)
for pwr in range(2, 6):
    # Try possible roots of the given number
    root = 1
    while root ** pwr <= num:
        if root ** pwr == num:
            print(f"A pair (root, pwr) that satisfies the conditions is: ({root}, {pwr})")
            found = True                
            break
        root += 1
        # If a pair is found, break out of the loop
        if found:
            break

    # If no pair is found, inform the user
if not found:
    print("No such pair of integers (root, pwr) exists for the given number.")

        


        