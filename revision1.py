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
# Find Minimum in a List
def min_list(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min
print(min_list([20,23,1,25,7,8])) 
# fabonacci series
a = 0
b = 1
for i  in range(0,8):
    print(a)
    temp = a
    a = b
    b = temp + b
# primenumber
for num in range(1,20):
    is_prime = True
    if num > 1:
      for i in range(2,num):
          if num % i == 0:
            is_prime = False
            break
      if is_prime:
          print(num)
# primenumber with function 
def prime_num(a):
    count = 0
    for i in range(2,a+1):
        if a % i == 0:
            count += 1
    if count == 2:
        print(a,"It's is a prime number")
    else:
        print(a,"It's is a not prime number")
prime_num(44)
# primenumber with function
def prime_num(num):
    for b in range(1,num+1):
        is_prime = True
        if b > 1 :
            for i in range(2,b):
                if b % i == 0:
                    is_prime= False
                    break
            if is_prime:
               print(b)
prime_num(20) 
# . Count Characters in String
text = "pjhgfdsdsdf"
count = 0
for char in text:
    count +=1
print(count)
print(len(text))
# Remove Duplicates from List
num = 1,2,3,3,2,1,3,4,5,45
print(set(num))
# Remove Duplicates from List
list = [1,2,2,3,3,2,44,5,5,4,7,7]
dup =[]
for  i in list:
    if i not in dup:
        dup.append(i)
print(sorted(dup,reverse=True))





# Simple caluculator
while True:
    a = int(input("Enter the number:"))
    b = int(input("enter the number:"))
    print("Enter the number:1-4")
    print("1.add,2.sub,3.MUltiplication,4.Division")
    choice = int(input("Enter the operation"))
    if choice == 1:
        print(a+b)
    elif choice == 2:
        print(a-b)
    elif choice == 3:
        print(a*b)
    elif choice == 4:
        if b != 0:
          print(a/b)
        else:
            print("not divisible")
    else:
        print("Invalid choice")
    again = input("DO you want enter (yes/No) ")
    if again.lower() != "yes":
        print("cal closed")
        break


# guesssing the numberrrrr
      
import random

# Computer chooses a random number between 1 and 20
number_to_guess = random.randint(1, 20)

print("Guess the number between 1 and 20!")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it correctly.")
        break  # Exit the loop when the user guesses correctly


# counting words
text = " hai i am ruchitha from cmrcet "
words=text.split()
count=len(words)
print(cout)