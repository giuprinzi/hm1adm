#INTRODUCTION (all – total: 7)


#Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")


#Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0:
    print("Weird")
elif n%2==0:
    if n>=2 and n<=5:
        print("Not Weird")
    if n>=6 and n<=20:
        print("Weird")
    if n>20:
        print("Not Weird")


#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


#Loops
if __name__ == '__main__':
    n = int(input())
    b=0
    while b<n:
        print(b*b)
        b=b+1


#Write a function
def is_leap(year):
    leap = False
    if year%4==0 and year%100!=0:
        leap=True
    if year%100==0 and year%400==0:
        leap=True
        
    return leap


#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")



#DATA TYPES (all – total: 6)


#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    risultato=[[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!= n]
    print(risultato)


#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxn=max(arr)
    newlist=[number for number in arr if number!=maxn]
    print(max(newlist))


#Nested Lists
if __name__ == '__main__':
    nestedlist=[]
    scorelist=[]
    namelist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        newlist=[name, score]
        nestedlist.append(newlist)
        scorelist.append(score)
    scorelist.sort()
    firstmin=scorelist[0]
    secondmin=firstmin
    for number in scorelist:
        if number>firstmin:
            secondmin=number
            break
    for students in nestedlist:
        if students[1]==secondmin:
            namelist.append(students[0])
    namelist.sort()
    for student in namelist:
        print(student)


#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    newlist=[]
    tot=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        newdic=(name, student_marks[name])
        newlist.append(newdic)
    query_name = input()
    for student in newlist:
        if student[0]==query_name:
            l=len(student[1])
            for number in student[1]:
                tot+=number
            average=tot/l
            rounded_average = format(average, '.2f') 
            print(rounded_average)


#Lists
if __name__ == '__main__':
    n = int(input())
    new_list=[]
    for _ in range(n):
        command=input().split()
        if command[0]=="append":
            new_list.append(int(command[1]))
        elif command[0]=="remove":
            new_list.remove(int(command[1]))
        elif command[0]=="insert":
            new_list.insert(int(command[1]), int(command[2]))
        elif command[0]=="print":
            print(new_list)
        elif command[0]=="sort":
            new_list.sort()
        elif command[0]=="pop":
            new_list.pop()
        elif command[0]=="reverse":
            new_list.reverse()


#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    h=hash(t)
    print(h)



#STRINGS (10/14)


#sWAP cASE
def swap_case(s):
    newstring=""
    for char in s:
        if char.islower():
            newstring+=char.upper() 
        elif char.isupper():
            newstring+=char.lower() 
        else:
            newstring+=char     
    return newstring


#String Split and Join
def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#What's Your Name?
def print_full_name(first, last):
    print("Hello "+ first+" "+last+"! You just delved into python.")


#Mutations
def mutate_string(string, position, character):
    string=string[:position]+ character+ string[position+1:]
    return string


#Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    return count


#String Validators
if __name__ == '__main__':
    s = input()
    ret=False
    for e in s:
        if e.isalnum():
            ret=ret or True
            break
        else:
            ret=ret or False
    print(ret)
    ret=False
    for el in s:
        if el.isalpha():
            ret=ret or True
            break
        else:
            ret=ret or False
    print(ret)
    ret=False
        
    for ele in s:
        if ele.isdigit():
            ret=ret or True
            break
        else:
            ret=ret or False
    print(ret)
    ret=False
    
    for elem in s:
        if elem.islower():
            ret=ret or True
            break
        else:
            ret=ret or False
    print(ret)
    ret=False
    
    for eleme in s:
        if eleme.isupper():
            ret=ret or True
            break
        else:
            ret=ret or False
    print(ret)



#Text Alignment
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


#Text Wrap
def wrap(string, max_width):
    count=0
    res=""
    for i in string:
        if count==max_width:
            res+="\n"
            count=1
            res+=i
        else:
            res+=i 
            count+=1 
    return res


#String Formatting
def print_formatted(number):
    width = len(bin(number)[2:])  
    for n in range(1,number+1):
        decimal=str(n).rjust(width)
        octal=oct(n)[2:].rjust(width)
        hexadecimal=hex(n)[2:].upper().rjust(width)
        binary=bin(n)[2:].rjust(width)
        print(decimal + " " + octal + " " + hexadecimal + " " + binary)


#Capitalize!
def solve(s):
    for element in s.split():
        s =s.replace(element, element.capitalize())
    return s



#SETS(all – total: 13)


#Introduction to Sets
def average(array):
    myset=set()
    sum=0
    l=0
    for element in array:
        myset.add(element)
    for h in myset:
        sum+=h
    result=sum/len(myset)
    return result


#No Idea!
n, m = map(int, input().split())
array = list(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))
happiness=0
newset=set()
for e in array:
     if e in A:
        happiness=happiness+1
     if e in B:
         happiness=happiness-1    
print(happiness)


#Symmetric Difference
n = int(input())
list_a = list(map(int, input().split()))
m = int(input())
list_b = list(map(int, input().split()))
set_a=set()
set_b=set()
for el in list_a:
    set_a.add(el)
for elem in list_b:
    set_b.add(elem)
intersezione=set_a.intersection(set_b)
unione=set_a.union(set_b)
sorted_union=sorted(unione)
for result in sorted_union:
    if result not in intersezione:
        print(result)


#Set .add()
N = int(input())
result_set=set()
for country in range(N):
    country_name = input()
    result_set.add(country_name)
result=len(result_set)
print(result)


#Set .discard(), .remove() & .pop()
n = int(input())
line = input()
lista = line.split()
lista.reverse()
s = set(map(int, lista))
N = int(input())
for _ in range(N):
    command = input().split()
    if len(command) == 1:
        if len(s) == 0:
            break
        else:
            s.pop()
    else:
        if command[0] == 'remove':
            if int(command[1]) in s:
                s.remove(int(command[1]))
        if command[0] == 'discard':
            s.discard(int(command[1]))
sum_of_elements = sum(s)
print(sum_of_elements)


#Set .union() Operation
n = int(input())
english_subscribers = set(map(int, input().split()))
b = int(input())
french_subscribers = set(map(int, input().split()))
unione=english_subscribers.union(french_subscribers)
result=len(unione)
print(result)


#Set .intersection() Operation
n = int(input())
english_subscribers = set(map(int, input().split()))
b = int(input())
french_subscribers = set(map(int, input().split()))
intersezione=english_subscribers.intersection(french_subscribers)
result=len(intersezione)
print(result)


#Set .difference() Operation
n = int(input())
english_subscribers = set(map(int, input().split()))
b = int(input())
french_subscribers = set(map(int, input().split()))
differenza=english_subscribers.difference(french_subscribers)
result=len(differenza)
print(result)


#Set .symmetric_difference() Operation
n = int(input())
english_subscribers = set(map(int, input().split()))
b = int(input())
french_subscribers = set(map(int, input().split()))
simmetrica=english_subscribers.symmetric_difference(french_subscribers)
result=len(simmetrica)
print(result)


#Set Mutations
n=int(input())
A=set(map(int, input().split()))
N=int(input())
for _ in range(N):
    command=input().split()
    newset=set(map(int, input().split()))
    if command[0]=="intersection_update":
        A.intersection_update(newset)
    if command[0]=="update":
        A.update(newset)
    if command[0]=="symmetric_difference_update":
        A.symmetric_difference_update(newset)
    if command[0]=="difference_update":
        A.difference_update(newset)
result=sum(A)
print(result)


#The Captain's Room
K=int(input())
room_number=list(map(int,input().split()))
rooms=set(room_number)
nuova_lista=[]
result=[]
conteggio={}
for numero in room_number:
    if numero not in conteggio:
        conteggio[numero]=1
    else:
        conteggio[numero]+=1
for numero in room_number:
    if conteggio[numero] > 1:
        nuova_lista.append(numero)
        conteggio[numero]-= 1
nuova_lista_set=set(nuova_lista)
result=rooms.difference(nuova_lista_set)
captain_room=result.pop()
print(captain_room)


#Check Subset
T=int(input())
for _ in range(T):
    na=int(input())
    A=set(map(int, input().split()))
    nb=int(input())
    B=set(map(int, input().split()))
    if A.issubset(B):
        print(True)
    else:
        print(False)


#Check Strict Superset
A=set(map(int, input().split()))
n=int(input())
result=True
for _ in range(n):
    other_set=set(map(int, input().split()))
    if other_set.issubset(A) and len(A)>len(other_set):
        result=result and True
    else:
        result= result and False
print(result)



#COLLECTIONS(6/8)


#collections.Counter()
from collections import Counter
x = int(input())
shoes_sizes = list(map(int, input().split()))
N = int(input())
counter = Counter(shoes_sizes)
money = 0
for _ in range(N):
    size, prize = map(int, input().split())
    if counter[size] > 0:
        money += prize
        counter[size] -= 1
print(money)


#DefaultDict Tutorial
from collections import defaultdict
d=defaultdict(list)
index=defaultdict(list)
n, m=map(int, input().split())
for a in range(n):
    element_a=input()
    d['A'].append(element_a)
for b in range(m):
    element_b=input()
    d['B'].append(element_b)
for index_a, word_a in enumerate(d['A'], start=1):  
    index[word_a].append(index_a) 
for word_b in d['B']:
    if word_b in index:
        print(" ".join(map(str, index[word_b])))
    else:
        print(-1)


#Collections.namedtuple()
from collections import namedtuple
N=int(input())
columns=input().split()
sum=0
Student=namedtuple('Student', ['ID', 'MARKS', 'NAME', 'CLASS'])
id_idx= columns.index('ID')
marks_idx = columns.index('MARKS')
name_idx = columns.index('NAME')
class_idx = columns.index('CLASS')
for _ in range(N):
    informations=input().split()
    student=Student(ID=informations[id_idx], MARKS=int(informations[marks_idx]), NAME=informations[name_idx], CLASS=informations[class_idx])
    sum=sum+student.MARKS
average=sum/N
formatted_average="{:.2f}".format(average)
print(formatted_average)


#Collections.OrderedDict()
from collections import OrderedDict
ordered_dictionary = OrderedDict()
N=int(input())
for _ in range(N):
    row=input().split()
    if len(row)==3:
        item=row[0]+" "+row[1]
        prize=int(row[2])
    else:
        item=row[0]
        prize=int(row[1])
    if item not in ordered_dictionary:
        ordered_dictionary[item]=prize
    else:
        ordered_dictionary[item]+=prize   
for key, value in ordered_dictionary.items():
    print(key, value)


#Word Order
from collections import OrderedDict
ordered_dictionary = OrderedDict()
output_list=[]
n=int(input())
for _ in range(n):
    word=input()
    if word not in ordered_dictionary:
        ordered_dictionary[word]=1
    else:
        ordered_dictionary[word]+=1  
print(len(ordered_dictionary))
for key, value in ordered_dictionary.items():
    output_list.append(value)
result = ' '.join(map(str, output_list))
print(result)


#Collections.deque()
from collections import deque
d = deque()
N=int(input())
for _ in range(N):
    command=input().split()
    if len(command)==2:
        method=command[0]
        value=int(command[1])
        if method=="append":
            d.append(value)
        elif method=="appendleft":
            d.appendleft(value)
    else:
        method=command[0]
        if method=="pop":
            d.pop()
        elif method=="popleft":
            d.popleft()
result = ' '.join(map(str, d))
print(result)



#DATE AND TIME (1/2)

#Calendar Module
import calendar
month, day, year = map(int, input().split())
day= calendar.weekday(year, month, day)
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(days[day])



#EXCEPTIONS (only 1)
T=int(input())
for _ in range(T):
    a, b =input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)


#BUILTS-INS(only 3)

#Zipped!
N, X=map(int, input().split())
newlist=[]
result_string=[]
result_int=[]
for _ in range(X):
    marks=list(input().split())
    newlist.append(marks)
zipped_lists = zip(*newlist)
result_string = list(zipped_lists)
for lista in result_string:
    lista_di_numeri= [float(s) for s in lista]
    result_int.append(lista_di_numeri)
    
for i in result_int:
    print(sum(i)/X)


#Athlete Sort
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sorted_list=sorted(arr, key=lambda x: x[k])
    for line in sorted_list:
        print(' '.join(map(str, line)))


#ginortS
s=input()
low=""
digit_odd=""
digit_even=""
upper=""
for e in s:
    if e.islower():
        low=low+e
    elif e.isupper():
        upper=upper+e
    elif e.isdigit():
        if int(e)%2==0:
            digit_even=digit_even+e
        else:
            digit_odd=digit_odd+e       
low_list = list(low)
upper_list = list(upper)
digit_even_list = list(digit_even)
digit_odd_list = list(digit_odd)
low_list.sort()
upper_list.sort()
digit_even_list.sort()
digit_odd_list.sort()
sorted_low = ''.join(low_list)
sorted_upper= ''.join(upper_list)
sorted_even_digit= ''.join(digit_even_list)
sorted_odd_digit= ''.join(digit_odd_list)
print(sorted_low+ sorted_upper+ sorted_odd_digit+ sorted_even_digit)



#PYTHON FUNCTIONALS (only 1 )


#Map and Lambda Function
cube = lambda x: x*x*x # complete the lambda function 
def fibonacci(n):
    result=[]
    for number in range(n):
        result.append(number)
    for i in result:
        if i!=0 and i!=1:
            result[i]=result[i-1]+result[i-2]
    return result


#Regex and Parsing challenges(6/17)


#Re.split()
regex_pattern = r"[,.]"	


#Group(), Groups() & Groupdict()
import re
S=input()
m=r'([a-zA-Z0-9])\1+'
matches=re.search(m,S)
if matches:
    print(matches.group(1))
else:
    print(-1)


#Re.findall() & Re.finditer()
import re
S=input()
pattern=r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
matches=re.findall(pattern,S)
if matches:
    for match in matches:   
        print(match)
else:
    print(-1)


#Regex Substitution
import re
def sostituisci(match):
    simbolo = match.group(0)
    if simbolo == '&&':
        return 'and'
    elif simbolo == '||':
        return 'or'
N = int(input())
for _ in range(N):
    linea = input()
    risultato = re.sub(r'(?<= )&&(?= )|(?<= )\|\|(?= )', sostituisci, linea)
    print(risultato)


#Validating phone numbers
import re
N=int(input())
for _ in range(N):
    N=input()
    pattern=r"[789]{1}[0123456789]{9}"
    if re.fullmatch(pattern, N):
        print("YES")
    else:
        print("NO")


#Validating and Parsing Email Addresses
import re
import email.utils
n=int(input())
for _ in range(n):
    line=input()
    ins=email.utils.parseaddr(line)
    name=ins[0]
    em=ins[1]
    pattern=r"[a-zA-Z][a-zA-Z0-9-._]+[@][a-zA-Z]+[.][a-zA-Z]{1,3}"
    if re.fullmatch(pattern, em):
        print(line)



#XML(1/2)


#XML 1 - Find the Score
def get_attr_number(node):
    # your code goes here
    score=0
    for elem in node.iter():
        score+=len(elem.attrib)
    return score



#CLOSURES AND DECORATIONS (1/2)


#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        standardized_numbers = []
        for number in l:
            standardized_number = number.replace(" ", "")
            if len(standardized_number) == 10:
                standardized_number = '+91 ' + standardized_number[:5] + ' ' + standardized_number[5:]
            elif len(standardized_number) == 11:
                standardized_number = '+91 ' + standardized_number[1:6] + ' ' + standardized_number[6:]
            elif len(standardized_number) == 12:
                standardized_number = '+' + standardized_number[:2] + ' ' + standardized_number[2:7]+' '+ standardized_number[7:]
            else:
                standardized_number = standardized_number[:3] + ' ' + standardized_number[3:8]+' '+ standardized_number[8:]
                
            standardized_numbers.append(standardized_number)
        f(standardized_numbers)
    return fun


#NUMPY (all – total: 15 )


#Arrays
def arrays(arr):
    array=numpy.array(arr, float)
    inverted_array=array[::-1]
    return inverted_array


#Shape and Reshape
import numpy
change_array = numpy.array(input().split(), int)
change_array.shape=(3, 3)
print(change_array)


#Transpose and Flatten
import numpy
lista=[]
N, M=input().split()
for _ in range(int(N)):
    lista.append(input().split())
my_array = numpy.array(lista, int)
print(numpy.transpose(my_array))
print(my_array.flatten())


#Concatenate
import numpy
list1=[]
list2=[]
N, M, P=input().split()
for _ in range(int(N)):
    list1.append(input().split())
for _ in range(int(M)):
    list2.append(input().split())
array_1=numpy.array(list1, int)
array_2=numpy.array(list2, int)
array_1.shape = (int(N), int(P))
array_2.shape = (int(M), int(P))
print(numpy.concatenate((array_1, array_2), axis=0))


#Zeros and Ones
import numpy
shape=input().split()
numpy_shape= numpy.array(shape, int)
print(numpy.zeros((numpy_shape), dtype=int))      
print(numpy.ones((numpy_shape), dtype=int))


#Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')
N, M=input().split()
print(numpy.eye(int(N), int(M), k=0))


#Array Mathematics
import numpy
N, M=map(int, input().split())
a=[]
b=[]
for _ in range(N):
    rowa= list(map(int, input().split()))
    a.append(rowa)
for __ in range(N):
    rowb= list(map(int, input().split()))
    b.append(rowb)
print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))


#Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')
array_a=input().split()
my_array=numpy.array(array_a, float)
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))


#Sum and Prod
import numpy
N, M=input().split()
lista=[]
for _ in range(int(N)):
    lista.append(input().split())
my_array = numpy.array(lista, int)
my_array=numpy.sum(my_array, axis=0)  
print(numpy.prod(my_array, axis = None)) 


#Min and Max
import numpy
N, M=input().split()
array_a=[]
for _ in range(int(N)):
    row=list(map(int, input().split()))
    array_a.append(row)
my_array = numpy.array(array_a)
my_array=numpy.min(my_array, axis = 1)
print(numpy.max(my_array)) 


#Mean, Var, and Std
import numpy
N, M=input().split()
arr=[]
for _ in range(int(N)):
    row=list(map(int, input().split()))
    arr.append(row)
my_array = numpy.array(arr)
print(numpy.mean(my_array, axis=1))  
print(numpy.var(my_array, axis=0))
print(round(numpy.std(my_array, axis=None), 11))


#Dot and Cross
import numpy
N=int(input())
array_a=[]
array_b=[]
for _ in range(N):
    row_a=list(map(int, input().split()))
    array_a.append(row_a)
for __ in range(N):
    row_b=list(map(int, input().split()))
    array_b.append(row_b)
A = numpy.array(array_a)
B = numpy.array(array_b)
print(numpy.dot(A, B))


#Inner and Outer
import numpy
array_a=input().split()
array_b=input().split()
A=numpy.array(array_a, int)
B=numpy.array(array_b, int)
print(numpy.inner(A, B))
print(numpy.outer(A, B))


#Polynomials
import numpy
polynomial=list(map(float, input().split()))
x=int(input())
P=numpy.array(polynomial)
print(numpy.polyval(P, x))


#Linear Algebra
import numpy
N=int(input())
array_a=[]
for _ in range(N):
    row=input().split()
    array_a.append(row)
a=numpy.array(array_a, float)
det = numpy.linalg.det(a)
det=round(numpy.linalg.det(a),2)
print(det)









































        











    








































































    
        









