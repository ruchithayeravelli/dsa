# ######7-3-26
# python basics
# Find Largest of Two Numbers
# in FUnction
def largest(a,b):
    if a > b :
        return a
    return b
num1 = int(input("ENter the number:"))
num2 = int(input("ENter the number:"))
lar=largest(num1,num2)
print("The largest num is:",lar)

# Find Largest of Two Numbers
num1 = input("Enter the Number1:")
num2 = input("Enter the num2")
if num1 > num2:
    print(num1)
else:
    print(num2)