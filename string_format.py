# net ninja #7 string formatting
num1 = 3.142432123454
num2 = 10.2903434

# previous
#print('num1 is', num1, 'and num2 is',num2)

# format method {0:.3} persision to 3 digits
# format method {0:.3f} presision to 3 digits
#print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1, num2))

# using f-strings
#print(f"num 1 is {num1} and num2 is {num2}")
# formatting with presision
print(f"num 1 is {num1:.4f} and num2 is {num2:.3f}")
