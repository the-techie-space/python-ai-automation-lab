
# >> simple class method create a instance object(i.e., name) and store in obj1 the class (i.e., student) and print name from class.

class Student():
    name = 'chandra'
obj1 = Student()
print(obj1.name)

# >> A simple code to print a name that we write in console.

person = input('Enter your name: ')
print('hello variant', person)

>> To create a class and constuctor and instance methods and get count of employees.

class Employee:
   'Common base class for all employees'
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print("Total Employee: ", Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
emp1 = Employee("sunny", 2000)
emp2 = Employee("sony", 2000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee: ", Employee.empCount)

# >>To get a unique numbers from a list.
    
numbers = [1,1,2,3,4]

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(get_unique_numbers(numbers))

# >> To get a particular item from list

List = [1,2,'sunny','xyz']
print("Value available at index 2 : ")
print (List[2])

# >> update a value from list

List = [1,2,'sunny','xyz']
print("Value available at index 2 : ")
print (List[2])
List[2] = 2001 #updating the index 2 value sunny to 2001
print ("New value available at index 2 : ")
print (List[2])

# >> append a string to list
List = [1,2,'sunny','xyz']
List.append('Appended Value')
print(List)

#>> if else

a = 20
b = 20

if a<b:
    print("{} is less than {}".format(a,b))
elif a == 20:
    print("{} is equal to {}".format(a,b))
else:
    print("{} is greater than {}".format(a,b))


#>> Give me each number in a list squared
  
my_list = [1,2,3,4,5,6,7,8,9,10]

squares = [num*num for num in my_list]
print(squares)


# >> Print 2 table using while(eg: while loop)
i =1
n= 2
while i<=10:
    print(i,"*",n,"=",n*i)
    i = i+1

>> Intel Interview
class Shoper:
    item=[]
    count=0
    def __init__(self, item1, item2):
        self.item1= item1
        self.item2= item2
        Shoper.count += 1
    def addItem(self, item1, item2):
        print(item1,"+",item2,"=",item1+item2)
        
    def displayItem(self):
        print("Item1: ", self.item1, "Item2: ", self.item2)
        
    def displayCount(self):
        print("The total Count is: ", Shoper.count)
        
a=Shoper("pant",200)
b=Shoper("shirt", 300)
a.displayItem()
b.displayItem()
a.addItem("pant","shirt")
print("The total Count is: ", Shoper.count)

>> how to find common elements between three lists in python
list1 = [1,2,3,4]
list2 = [2,3,4,5]
list3 = [2,5,6,7]

list1_as_set = set(list1)

intersection = list1_as_set.intersection(list2,list3)

intersection_as_list = list(intersection)

print(intersection_as_list)

#>> how to find least common elements between three lists in python

from collections import Counter
list1 = [1,2,3,4]
list2 = [2,3,4,5]
list3 = [2,3,5,6,7]

list1_as_set = set(list1)

intersection = list1_as_set.intersection(list2,list3)

print(Counter(intersection).most_common()[0][0])

#>> How to print the elements in same line (end='') 
a= [1, 2, 3, 'sunny', 2, 'a2']
for i in range(6):
    print(a[i], end=',')

#>> mutable and immutable differences in program
my_tuple = ('sara', 1, 2, 3)
my_list = ['sara', 1, 2, 3]
print(my_tuple[0])
print(my_list[0])
my_tuple[0] = 'ansh'
my_list[0] = 'ansh'
print(my_tuple[0])
print(my_list[0])


#>> Pass statement
def my_emptyfun():
    pass
my_emptyfun()

#>> How to use Break,continue in program
pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
for p in pat:
    pass
    if (p==0):
        current=p
        break
    elif (p % 2 == 0):
        continue
    print(p, end=' ')
print(current)
    
#>> Slicing Concept

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1 :7: 1])

#>> Check a leap year

def check_leap_year(year): 
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."
 
year_to_check = 2024
returned_value = check_leap_year(year_to_check)
print(returned_value) # 2024 is not a leap year.


# >> Python String .format() 
msg1 = 'Fred scored {} out of {} points.'
msg1.format(3, 10)
# o/p:- => 'Fred scored 3 out of 10 points.'
 
msg2 = 'Fred {verb} a {adjective} {noun}.'
msg2.format(adjective='fluffy', verb='tickled', noun='hamster')
# o/p:- => 'Fred tickled a fluffy hamster.'

print(msg1.format(3, 10))
print(msg2.format(adjective='fluffy', verb='tickled', noun='hamster'))

#>> String Method .join()

x = "-".join(["Codecademy", "is", "awesome"])
 
print(x) 
# Prints: Codecademy-is-awesome


## Python advanced programs
#Building lists
# to print a even numbes from 0 to 100

randstr = [i for i in range(100) if i % 2 == 0]
print(randstr)


# To print odd numbers from 0 to 100

randstr = [i for i in range(100) if i % 2 != 0]
print(randstr)


# to print even_squares of list from 1 to 12

even_squares = [ x ** 2 for x in range(1, 12) if x % 2 == 0]

print even_squares

# print the square numbers between 30 to 70 using lambda

squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)


# if u want to print clean string without X using lambda function( filter out the X)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X" , garbled)
print message


# if u want to print names from list with index values ( trick by using enumerate )

names = ['sun', 'city', 'enterence', 'gate']

for index, name in enumerate(names):
    print(index, name)


## using Zip indexing the three list match ( python smart key to use i.e.., zip )

names = ['Peter Paraker', 'Clark Kent', 'Wade wilson', 'Bruce Wayne']
heros = ['Spyder Man', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']
 
for name, hero, universe in zip(names, heros, universes):
    print(f'{name} is actually a {hero} from {universe}')


## Use getpass built-in fn to hide password while entering the password ( smart trick to use ) 
   
from getpass import getpass

Username = input('Username: ')
Password = getpass('Password: ')
print('Logging in ......')

Mphasis
# what is args and kwargs?

In Python, *args and **kwargs let a function accept a flexible number of arguments.

They make your functions more dynamic.

*args collects any number of positional arguments into a tuple.

def demo(*args):
    print(args)

demo(1, 2, 3)

You can pass any count of arguments, even zero.

**kwargs collects any number of keyword arguments into a dictionary.

def demo(**kwargs):
    print(kwargs)

demo(name="John", age=30)

*args must come before **kwargs.

def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, name="Alice", age=25)

# Find an occurrence of 8 in given list ?

a_list = [3,5,8,2,6,8,5,9,10,2,4,8,11,8]

b_list = []

for i in a_list:
    if i == 8:
        b_list.append(i)

print(len(b_list))

simply you can do as below,

a_list = [3,5,8,2,6,8,5,9,10,2,4,8,11,8]

count_8 = a_list.count(8)
print(count_8)

# What is map function and how it is used?

The map() function in Python is used to apply a function to every item of an iterable (like a list, tuple, etc.) and return a map object (an iterator).

Example 1,

c_list = ["A","B","C"]

b_list = [8,2,6]

end = dict(map(lambda k, v: (k, v), c_list, b_list))

print(end)

Example 2,

map(function, iterable)

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))

## palindrome 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pali = [i.lower() for i in s if i.isalnum()]
        initial_name = "".join(pali)
        last_name = "".join(initial_name[::-1])
        if initial_name == last_name:
            return True
        else:
            return False

class_obj = Solution()

result = class_obj.isPalindrome(input("Enter inuput name here: "))

print(result)

Example inputs: Madam I'm Adam, A man, a plan, a canal: Panama


## virtusa

# in string s = "12345661781"
# if 1 ocurs then print in dict like {1: 2}
# here key is the obj and value is ocurance

from collections import Counter

s1 = "12345661781"

counter = Counter(s1)
print(counter)



print({1: s1.count('1')})


s1 = "12345661781"
l1 = list(s1)
dict1 = {}
i_count = 0
l2 = []

print(l1)

for i in l1:
    
    if i in l2:
        dict1[i] += 1
    else:
        l2.append(i)
        dict1[i] = 1
       
print(dict1)

# in a list l1 = [1,2,3,6,7] sort the given list in three different ways

l1 = [1, 2, 3, 6, 7]
sorted_l1 = sorted(l1)
print(sorted_l1)


l1 = [1, 2, 3, 6, 7]
l1.sort()
print(l1)


l1 = [1, 2, 3, 6, 7]
sorted_desc = sorted(l1, reverse=True)
print(sorted_desc)   # [7, 6, 3, 2, 1]


l1 = [1, 2, 3, 6, 7]
sorted_custom = sorted(l1, key=lambda x: -x)
print(sorted_custom)

1. Bubble sort (manual sorting algorithm)

l1 = [3, 1, 2]

for i in range(len(l1)):
    for j in range(0, len(l1) - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]

print(l1)   # [1, 2, 3]

2. Selection sort

l1 = [3, 1, 2]
sorted_list = []

while l1:
    m = min(l1)
    sorted_list.append(m)
    l1.remove(m)

print(sorted_list)   # [1, 2, 3]


3. Sort using heapq (heap sort)

import heapq

l1 = [3, 1, 2]
heapq.heapify(l1)
sorted_list = [heapq.heappop(l1) for _ in range(len(l1))]

print(sorted_list)   # [1, 2, 3]


# give me middle letter for given string

name = "Chandra"

string_length = list(name)

mid_index = len(string_length) // 2

middle_letter = string_length[mid_index]

print(middle_letter)

##for even length 

name = "Chandr"
length = len(name)

if length % 2 == 0:
    mid = length // 2
    print(name[mid - 1 : mid + 1])   # "ha"
else:
    print(name[length // 2]) 


##Write a python program to make only the vowels capital in a string.
Example:
strng = "Hi HeLLo HOw Are YoU"
ans : "hI hEllO hOw ArE yOU"

method1:

strng = "Hi HeLLo HOw Are YoU"
vowels = "aeiou"

list1 = []
for i in strng.lower():
    if i in vowels:
        list1.append(i.upper())
    else:
        list1.append(i)

print(''.join(list1))

method2:

strng = "Hi HeLLo HOw Are YoU"
vowels = "aeiou"

result = ""

for ch in strng:
    if ch.lower() in vowels:
        result += ch.upper()
    else:
        result += ch.lower()

print(result)

one line method3:

result = ''.join(
    ch.upper() if ch.lower() in "aeiou" else ch.lower()
    for ch in strng
)
print(result)


##consider an array where 0s are mixed in the list with some are consecutive zeros also, move all the zeros to end on the same array
lists= [4,0,5,0,0,6,0,3,2,7,0,0,1,0,9,0,0,8,1,0]
 
Ans : [4, 5, 6, 3, 2, 7, 1, 9, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

method1:

end_list = []
num_list = []

for item in lists:
    if item == 0:
        end_list.append(item)
    else:
        num_list.append(item)

final_list = num_list + end_list
print(final_list)


mehtod2:

lists = [x for x in lists if x != 0] + [0] * lists.count(0)

method3: (suggested by interviewer)

lists = [4,0,5,0,0,6,0,3,2,7,0,0,1,0,9,0,0,8,1,0]

# Index where next non-zero should go
pos = 0

# Move all non-zero elements forward
for i in range(len(lists)):
    if lists[i] != 0:		
        lists[pos] = lists[i]
        pos += 1

# Fill remaining positions with zeros
for i in range(pos, len(lists)):
    lists[i] = 0

print(lists)


# coforge services (company)

# Write a program which take input as integer and generates output like below "
# Input = 4
# output :
# 1
# 122 if 2 comes to iterate then append 122 (2 times two)
# 122333 (3 times 3)
# 1223334444 (4 times 4)

def pattern_fun(num):
    ch = ''
    for i in range(1, num+1):
        ch = ch + i*str(i)
        print(ch)

res = pattern_fun(int(input("Enter input : ")))

# sort an array in a ascending order
lst = [1,4,5,2,6]
# dd = sorted(lst, reverse=False)

# without inbuilt function sort in ascending order (bubbule sort)
n = len(lst)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j +1] = lst[j+1], lst[j]
print(lst)

# selection sort
 end_lst = []
 while lst:
     min_num = min(lst)
     end_lst.append(min_num)
     lst.remove(min_num)


# sum of an array
arr = [1,2,3,4]

sum = 0
for i in arr:
    sum = sum + i

print(sum)

def prime_number(num):
    is_prime = True
    if num <= 1:
        print("its not a prime number")
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    return is_prime

print(prime_number(5))

def reverse_without_builtin(name):
    rev = ''
    for ch in name:
        rev = ch + rev
    return rev


print(reverse_without_builtin("madam"))

def reverse_with_builtin_reveresed(name):
    rev = ''.join(reversed(name))
    print(rev)

reverse_with_builtin_reveresed("madam")

def reverse_with_slice_or_palindrome(name):
    cleaned_name = "".join([ch.lower() for ch in name if ch.isalnum()])
    print(cleaned_name)
    res = cleaned_name == cleaned_name[::-1]
    return res

print(reverse_with_slice_or_palindrome("Madam I'm Adam, A man, a plan, a canal: Panama"))

# largest number

def largest_num(num_list):
    largest = num_list[0]
    for i in range(len(num_list)):
        if num_list[i] > largest:
            largest = num_list[i]
    return largest

print(largest_num([1,2,5,3]))

# second largest number

def sec_largest_num_function(num_list):
    largest = sec_largest_num = float('-inf')
    for i in num_list:
        if i > largest:
            sec_largest_num = largest
            largest = i
        elif i > sec_largest_num and i != largest:
            sec_largest_num = i
    return sec_largest_num

print(sec_largest_num_function([1,2,5,3]))

# map function

c_list = ["A","B","C"]

b_list = [8,2,6]

map = dict(map(lambda k, v : (k,v), c_list, b_list)) # {'A': 8, 'B': 2, 'C': 6}
print(map)

# reverse without slicing
def reverse_without_slice_or_palindrome(name):
    cleaned_name = "".join(ch.lower() for ch in name if ch.isalnum())
    left, right = 0, len(cleaned_name) - 1

    while left < right:
        if cleaned_name[left] != cleaned_name[right]:
            return False
        left += 1
        right -= 1
    return True

print(reverse_without_slice_or_palindrome("Madam I'm Adam, A man, a plan, a canal: Panama"))


# bubble sort 
l1 = [3, 1, 2, 4, 7]

for i in range(len(l1)):
    for j in range(0, len(l1) - i -1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]

print(l1)

# pattern

def pattern_numbers(num):
    res = ''
    for ch in range(1, num + 1):
        res = res + str(ch) * ch
        print(res)

pattern_numbers(5)

# *
# **
# ***
# ****
# *****

def pattern1(n):
    for i in range(1, n+1):
        print("*" * i)

pattern1(5)

# *****
# ****
# ***
# **
# *

def pattern2(n):
    for i in range(n, 0, -1):
        print("*" * i)

pattern2(5)

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

def pattern4(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)

pattern4(5)


# ACL digital (service based company asked questions)

# revers the words (India love I )
sentence = "I love India"
new_s = ''
for word in sentence.split():
    new_s = word + ' ' + new_s
    
print(new_s)



