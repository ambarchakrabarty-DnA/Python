# Python List Comprehension


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list1=[]

for i in range(x+1):
  for j in range(y+1):
     for k in range(z+1):
        if (i+j+k != n):
            list1.append([i,j,k])    
print(list1)

---------------------------------------------------------------------------
# Find the runner up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
        
arr = set(arr)
max_score = max(arr)
runner_up_score = -101

for score in arr:
    if score != max_score:
        runner_up_score = max(runner_up_score, score)
        
print(runner_up_score)

------------------------------------------------------------------------------
# Nested list for student scores
if __name__ == '__main__':
    
    students = []
    
    student_scores = []
    
    second_lowest_score_names = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        student_scores.append(score)
        
    student_scores = sorted(set(student_scores))
    
    second_lowest_score = student_scores[1]
    
    for student in students:
        if student[1] == second_lowest_score:
            second_lowest_score_names.append(student[0])
            
    second_lowest_score_names.sort()
    
    for names in second_lowest_score_names:
        print(names)
 ------------------------------------------------------------------------------------
 # Find the percentage marks
 
 if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average_marks = 0
    
    for student in student_marks:
        if student == query_name:
            average_marks = sum(student_marks[student]) / 3
            
    print(f'{average_marks:.2f}')
    
 -------------------------------------------------------------------------------------
 # String formatting
 
 def print_formatted(number):
    width = len(format(number,'b'))

    for i in range(1, number+1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
 
 ---------------------------------------------------------------------------------------
 # Print Rangoli
 
 def print_rangoli(size):
    alphabet_lst = list(map(chr, range(97, 123)))
    char_lst = alphabet_lst[:size]
    char_lst.reverse()
    print_str_lst = []
    place_holder = 4*size - 3
    for idx, char in enumerate(char_lst):
        side_chars_str = "-".join(char_lst[:idx])
        side_chars_str = side_chars_str + "-" if size > 1 else ""
        center_str = f"{side_chars_str}{char}{side_chars_str[::-1]}"
        print_str = center_str.center(place_holder, "-")
        print(print_str)
        print_str_lst.append(print_str)

    for idx, print_str in enumerate(print_str_lst[::-1]):
        if idx == 0:
            continue
        print(print_str)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

---------------------------------------------------------------------------------------
# Capitalize 

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
----------------------------------------------------------------------------------------
# Minion game
def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length-i
        else: 
            stuart_score += length-i
            
    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif stuart_score > kevin_score:
        print('Stuart', stuart_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
-----------------------------------------------------------------------------------------
# Merge the tools
def merge_the_tools(string, k):
    for t in range(0,len(string),k):
        u = set()
        for i in range(t,t+k):
            if string[i] not in u:
                u.add(string[i])
                print(string[i],end="")
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
--------------------------------------------------------------------------------------
#Validating credit card numbers

import re

n = int(input())
credit_cards = []

def validate_credit_card_numbers(credit_cards):
    pattern = r'^(?=[456])(?!.*(\d)(-?\1){3})\d{4}(-?\d{4}){3}$'
    
    for credit_card in credit_cards:
        if re.match(pattern, credit_card):
            print('Valid')
        else:
            print('Invalid')


for i in range(n):
    nums = input()
    credit_cards.append(nums)
    
validate_credit_card_numbers(credit_cards)

-----------------------------------------------------------------------------------------
# Validating postal codes

regex_integer_in_range = r"(?![100000-999999]{7,})[100000-999999]"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

-----------------------------------------------------------------------------------------
# Matrix Script
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_script = ''
for i in range(m):
    for j in range(n):
        decoded_script += matrix[j][i]

pattern = r'(?<=\w)([!@#$%&]+)(?=\w)|(?<=\W)([!@#$%&]+)(?=\w)'
decoded_script = re.sub(pattern, ' ', decoded_script)
print(decoded_script)

-----------------------------------------------------------------------------------------------
# Lists
def insert(i, e, arr):
    arr.insert(i, e)
    return arr
def prnt(arr):
    print(arr)
    return
def remove(e, arr):
    x = arr.index(e)
    arr.pop(x)
    return arr
def append(e, arr):
    arr.append(e)
    return arr
def sort(arr):
    return sorted(arr)
def pop(arr):
    arr.pop()
    return arr
def reverse(arr):
    return arr[::-1]


if __name__ == '__main__':
    N = int(input())
    array = []
    for _ in range(N):
        cmd = input().split()
        if (cmd[0] == "insert"):
            array = insert(int(cmd[1]), int(cmd[2]), array)
        if (cmd[0] == "print"):
            prnt(array)
        if (cmd[0] == "remove"):
            array = remove(int(cmd[1]), array)
        if (cmd[0] == "append"):
            array = append(int(cmd[1]), array)
        if (cmd[0] == "sort"):
            array = sort(array)
        if (cmd[0] == "pop"):
            array = pop(array)
        if (cmd[0] == "reverse"):
            array = reverse(array)
           
-------------------------------------------------------------------------------------------------
# Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(integer_list)
    result = hash(integer_tuple)
    print(result)
    
-------------------------------------------------------------------------------------------------
# Swap case 

def swap_case(word):
    swap_word=""
    for letter in word:
        if letter.islower():
            swap_word+= letter.upper()
        elif letter.isupper():
            swap_word+=letter.lower()
        else:
             swap_word += letter

    return swap_word 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
----------------------------------------------------------------------------------------------
# String split and join

def split_and_join(line):
    # write your code here
    s = line.replace(" ","-")
    return s
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
------------------------------------------------------------------------------------------------
# What's your name ?

def print_full_name(first, last):
    # Write your code here
    print("Hello {0} {1}! You just delved into python.".format(first,last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
-----------------------------------------------------------------------------------------------
# Mutations
def mutate_string(string, position, character):
   # return
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
-------------------------------------------------------------------------------------------------
# Find a string

def count_substring(string, sub_string):
    sum = 0
    sub_len = len(sub_string)
    for i in range(len(string)-sub_len+1):
        if string[i:i + sub_len] == sub_string:
            sum += 1
    return sum

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
--------------------------------------------------------------------------------------------------
# String validators

if __name__ == '__main__':
    s = input()
    d={'an':False,'a':False,'d':False,'l':False,'u':False}
    for i in s:
        if ord(i) in range(65,91):
            d['an']=d['a']=d['u']=True
        if ord(i) in range(97,123):
            d['an']=d['a']=d['l']=True
        if ord(i) in range(48,58):
            d['an']=d['d']=True
    for i,j in d.items():
        print(j)
        
------------------------------------------------------------------------------------------------
# Text allignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
------------------------------------------------------------------------------------------------------------
# text wrap 
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
----------------------------------------------------------------------------------------------------------
# Designer door mat 

n, m = [int(i) for i in input().split(' ')]

c = -1
items = []

for i in range(0, n//2):
    c += 2
    items.append(('.|.' * c).center(m, '-'))
    
for i in items: print(i)    
print('WELCOME'.center(m, '-'))
for i in items[::-1]: print(i)

--------------------------------------------------------------------------------------------------------
# Group() , groups() and groupdict()

import re
s = input()
pattern = '[a-zA-Z0-9]+'
m = re.search(pattern, s)
alnum = m.group()
for i in range(1,len(alnum)):
    if alnum[i-1] == alnum[i]:
        print(alnum[i])
        break
else:
    print(-1)
    
------------------------------------------------------------------------------------------------------
# Re.findall() & Re.finditer()

import re
S = input()
vowels = "AEIOUaeiou"
consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
pattern = rf'([{vowels}]{{2,}})(?=[{consonants}])'
result = re.findall(pattern,S)
if result == []:
    print (-1)
else:
    for i in result:
        print(i)

-------------------------------------------------------------------------------------------------------
# itertools.product() for nested for loops
from itertools import product

#taking inputs 
input1 = input() 
input2 = input()

#split and addind to a list
A = input1.split(" ")
B = input2.split(" ")

#convert into a tuple
int_lst_A = tuple(int(i) for i in A)
int_lst_B = tuple(int(i) for i in B)

#store the output in a variable as a list
result = (list(product(int_lst_A, int_lst_B)))

#printing the output as expected
for i in result:
    print(i, end=" ")
--------------------------------------------------------------------------------------------------------
# itertools.permutations(iterable[, r])
from itertools import permutations

s, k = input().split()
num_k = int(k)
result = permutations(sorted(list(s)),num_k)

for i in result:
    print(''.join(i))
-------------------------------------------------------------------------------------------------------
# itertools.combinations 

from itertools import combinations

def generate_combinations(input_str):
    parts = input_str.split()
    string = parts[0]
    max_length = int(parts[1])
    
    sorted_chars = sorted(string)
    
    result = []
    
    for length in range(1, max_length + 1):
        result.extend([''.join(comb) for comb in combinations(sorted_chars, length)])
    
    for item in result:
        print(item)

input_str = input()
generate_combinations(input_str)

--------------------------------------------------------------------------------------------------------
# itertools.combinations_with_replacement(iterable, r)

from itertools import combinations_with_replacement
s,k=input().split()
final=list()
k=int(k)
lst=(list(combinations_with_replacement(s,k)))

for i in range(len(lst)):
    inn=list(lst[i])
    inn.sort()
    nn='0'
    for j in inn:
        nn+=j
    final.append(nn[1:])
final.sort()
for i in range(len(final)):
    print(final[i])

---------------------------------------------------------------------------------------------






















