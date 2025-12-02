## What is python


## Literals


## Functions

## Operator

## Variables
# we assign value of one variable ot other variable it will copy the variabl value not reference like list, object etc.



## Input
#- Value of input function always string
#- A program that doesn't use any input funtion, is called a deaf program 

your_age = 5
# your_age = input('How old are you?')
print(f'Your are {your_age} year old')

#Type Casting
# if isinstance(your_age, str):
#   print('The variable is an string')

# if isinstance(your_age, int):
#   print('The variable is an integer')

# your_age = int(your_age)
# if isinstance(your_age, int):
#   print('The variable is an integer now')

# your_age = str(your_age)
# if isinstance(your_age, str):
#   print('The variable is an string now')

# your_age = float(your_age)
# if isinstance(your_age, float):
#   print(f'The variable is an float now {your_age}')

## Comparison Operators

## Conditional Statments

if ( 10 > 11):
  print('10 is greater than 11')
elif( 11> 10):
  print('')
else:
  print('')


# While loops

secret_number = 4

# guess = int(input('Guess a number: '))

# while guess != secret_number :
#   guess = int(input('Guess a number: '))
# else:
#   print('Congratulations, you got it!')


## for loop
# for item in iterables:

# for i in range(5): 
#   print(i)


# for i in range(100):
#   if(i==22):
#     break
#   print('i is: ', i)

for i in range(11, 21):
  if(i==17):
    continue
  print('i is: ', i)



######### Logical operator

# and(&&), or(||), not(!) 

######### print binory 

print(bin(5))

########## Biwise Operators 
# &, |, ~, ^, >>, <<

num1 = 15
num2 = 22

print(bin(num1))
print(bin(num2))

print(bin(num1 & num2)) 
print(num1 & num2)# 1 & 1 = 1

print(bin(num1 | num2)) 
print(num1 | num2)# 1 & 0 = 1, 1 & 1 = 1

print(bin(num1 ^ num2)) 
print(num1 ^ num2)# 1 & 0 = 1

print(bin(num1)) 
print(~num1)# 1 = 0, 0 = 1

##### Bit Shifting 
## >>, <<

print(22 << 1)
print(22 << 2)
print(22 >> 1)
print(22 >> 2)


print(22*2) # for referece it work like same above bitwise operator
print(22 * 4)
print(22//2)
print(22//4)


#### Lists

name_list = ['raj', 'ram', 'rakesh']
print(name_list)
#print by index nagative index also work
print(name_list[1])
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])
# asign new value
name_list[0] = 'ajay'
print(name_list)
# get length
print(len(name_list))
# delete value
del name_list[2]
print(name_list)

# append new value
name_list.append('pintu')
name_list.append('bittu')
print(name_list)

# insert value on particular index, not delete any value
name_list.insert(1, 'Tata Namak')
print(name_list)

# swap value
name_list[0], name_list[1] = name_list[1], name_list[0] # Swap value with different index
print(name_list)

number_list = [4, 65, 23, 89, 22, 26, 46]
print(number_list)

# sort
number_list.sort()
print(number_list)

# reverse
number_list.reverse()
print(number_list)

# iterate the list
total = 0
for number in number_list:
  total += number
print(total)

# We can assign to list to other vairable both reference to same list not assign new list to other variable
number_list2 = number_list

#slice List
# list[start:end]
# create new list and assing not add reference
number_list3 = number_list[0:2]
print(number_list)
print(number_list3)
number_list3 = number_list[0:]
number_list.append(55)
print(number_list)
print(number_list3)
number_list3 = number_list[3:5]
print(number_list)
print(number_list3)
number_list3 = number_list[3:-1]
print(number_list)
print(number_list3)
number_list3 = number_list[:]
print(number_list)
print(number_list3)
del number_list[0:5]
print(number_list)
print(number_list3)

#Finding element in list
print(65 in number_list3)
print(54 in number_list3)

print(65 not in number_list3)
print(54 not in number_list3)


##### Nested List 2D

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid)
print(grid[2][2])

##### Nested List 3D

matrix_3d = [
    [  # First 2x3 matrix
        [1, 2, 3],  # First row of first matrix
        [4, 5, 6]   # Second row of first matrix
    ],
    [  # Second 2x3 matrix
        [7, 8, 9],  # First row of second matrix
        [10, 11, 12] # Second row of second matrix
    ]
]

# Accessing elements:
# Access the first matrix (index 0)
print(f"First matrix: {matrix_3d[0]}")

# Access the second row of the second matrix (index 1, then index 1)
print(f"Second row of second matrix: {matrix_3d[1][1]}")

# Access the element at row 0, column 2 of the first matrix (index 0, then index 0, then index 2)
print(f"Element at [0][0][2]: {matrix_3d[0][0][2]}")


###### Functions and method
# function : print(), input()
# method: .insert(), .append()

# def inputNumber():
#   return int(input('Input Number: '))

# print(inputNumber())

# functionArgument
#passArgumentValue(44) # we can't run function without declaring it first
def passArgumentValue(value):
  return print(value)

passArgumentValue(44)

#default Value to parameter
def default_paremter(num = 1):
  print(num)

default_paremter()

#function return


##### Scopes
#Variable declare inside function it's work inside function
# Local: decalre value inside scope available can't use outside
# Global: declare outside function or using global keyword 
# Enclosing(Nonlocal): value declare inside function can be use nested function also


### Tuples
# Tuples is imutable data type
tuple1 = (3, 4, 'string', ('tupel', 'also'))

#del tuple1[1] # will not work
#tuple1[1] = 5 # will not work
print(tuple1)
print(tuple1[3])

for value in tuple1:
  print(value)

tuple2 = 4, 5, 2,3
print(tuple2)

tuple3 = 3,
tuple4 = [3,]
print(tuple3)

#### Dictionary

dictionaryExample ={
  'key1' : 'Value1',
  "num1": 44,
  'age':33,
  "weight": 77
}

print(dictionaryExample)

print(dictionaryExample["num1"])

#key method

print(dictionaryExample.keys())

for key in dictionaryExample.keys():
  print(f"{key} - {dictionaryExample[key]}")

#value method
print(dictionaryExample.values())

# items method
print(dictionaryExample.items())

# asign new value
dictionaryExample['key1'] = 'ChangedKey'
print(dictionaryExample)

# delete value

del dictionaryExample['key1']

print(dictionaryExample)

# pop last item
dictionaryExample.popitem()
print(dictionaryExample)


#copy dictionary
newCopyDictionary = dictionaryExample.copy()
print(newCopyDictionary)
dictionaryExample['key2'] = "key2Value"
print(dictionaryExample)

print(newCopyDictionary)


#### Error(Exception)
# Exception is special type of data 

try:
  name = 'Raj'
  print('My Name is ' + naem)
except:
  print('Something went wrong')
print('All done')



# For specific exception

try: 
  x = int(input('Enter a number: '))
  y = 1/x
  print(y)
except ZeroDivisionError:
  print('You cannot divide with zero')
except ValueError:
  print('Please Enter an integer')
except:
  print('Something elese wend wrong')

print('all done!')

##### The hierarchy of Exceptions
# we have 63 exception where we can use general exception for specific exception ArthmeticError is parent of ZeroDivisionError, Exception is parent of ArhemeticeError
# Exception will run on sequence base which will work first it will run first

try: 
  x = int(input('Enter a number: '))
  y = 1/x
  print(y)
except ZeroDivisionError: # it will run first
  print('You cannot divide with zero')
except (ZeroDivisionError, ArithmeticError):
  print('Calculation Failed')
except ValueError:
  print('Please Enter an integer')
except:
  print('Something elese wend wrong')

print('all done!')


# Manualy Raise by "raise keyword"

def calculare_user_input():
  raise ZeroDivisionError

try:
  calculare_user_input()
except ZeroDivisionError:
  print('You cannot divide with zero')
except:
  print('Something went wrong')

# rasie without any name/Re-raise same exception

def divide_with_zero():
  try: 
    x = 0
    y = 1/x
    print(y)
  except:
    print('Something elese wend wrong')
    raise

try:
  divide_with_zero()
except ZeroDivisionError:
  print('you cannot divide with zero')
except:
  print('Something else went wrong')


# assert keyword
n = int(input('Enter a number for assert check: '))
assert n >= 0