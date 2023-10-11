#Birthday Cake Candles:
#To solve this problem, I created the 'sorted_candles' list, which is the list of elements of the 'candles' array (The function 
# accepts INTEGER_ARRAY candles as a parameter) sorted in decrescending order. Then I counted the occurrences of 
# the element 'sorted_candles[0]' which, being the highest number in the sorted list, represents the height of the tallest candle.

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    ret=0
    sorted_candles=sorted(candles, reverse=True)
    ret=sorted_candles.count(int(sorted_candles[0]))
    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()





#Number Line Jumps:
#I solved this problem considering the equation of uniform linear motion, x = x0 + vot. In our case 't' does not represent
# time but it rapresents the number of jumps (as the prompt states that the kangaroo moves at a rate of 'v' meters per jump). 
# To determine if the kangaroos will ever meet (i.e., if they will ever be at the same position at the same time), 
# I equated the two equations(x1 + v1t = x2 + v2t) and solved for the unknown 't,' which is given by t = (x2 - x1)/(v1 - v2). 
# If t is greater than or equal to 0 and is an integer (because they jump in the positive direction of the x axis and must be 
# at the same position 'x' at the same moment, so 't' must be an integer), then they will meet; otherwise, they won't. 
# Of course, I handled the case where v1 = v2 (in that case, the denominator of 't' becomes zero), in which case they will meet 
# only if their initial positions 'x1' and 'x2' are the same

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1== v2:
        if x1==x2:
            return "YES"
        else:
            return "NO"
    t=(x2-x1)/(v1-v2)
    if t>=0 and int(t)==t:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()





#Viral Advertising
#I solved this problem by initially creating the list with predefined values representing Day, Shared, Liked, and Cumulative
# of the first day. This was possible because I knew from the prompt that the first day (list[0]), 
# they advertise the product to exactly 5 people on social media(list[1]), and half of those people (i.e., 5//2=2, list[3])
# like the advertisement. Naturally, the cumulative value for the first day is equal to the likes of the first day. 
# Then I used a 'for' loop that starts from 2 (because if n==1, I directly return the cumulative value of the first day, list[3]) 
# and goes up to n+1 (as I want to calculate the cumulative value of day n) and I used it for continuously updating the 'list'.

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    list=[1,5,2,2]
    if n==1:
        return list[3]
    else:
        for day in range(2, n+1):
            list[0]=day
            list[1]=(list[1]//2)*3
            list[2]=list[1]//2
            list[3]+=list[2]
        return list[3]
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()





#Recursive Digit Sum
#I solved this problem recursively.In this case the base case (that represents the condition in which the function terminates recursion) is when the length of the string 'n' is equal to 1.
#  In this case, the function simply returns the value of 'n' converted to an integer, because a single-digit number is already a super-digit.
#The recursive step (that rapresents what the function do when the base case is not satisfied) calculates the sum of the digits of 'n' and multiplies the result by 'k' 
# (because we need to concatenate the string to itself k times), and then calls the same function with the new value obtained as a string and k=1.

import math
import os
import random
import re
import sys

def superDigit(n, k):
    if len(n) == 1:
        return int(n)
    digit_sum = sum(int(digit) for digit in n) * k
    return superDigit(str(digit_sum), 1)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()





#Insertion Sort - Part 1
#To store the value of the last element of the array arr I initialized number with this value.
#Then I created a loop that starts from the second-to-last element (index n-2) and goes down to the first element (index 0) of the array in reverse order. This loop is used to compare 
# and shift elements to the right to place number in the correct position in the sorted array.
#Inside the loop, it checks if number is less than the element at the current index. If true, it shifts the current element one position to the right (by assigning the current element to 
# the next position in the array, arr[index+1] = arr[index]), and then it prints the current state of the array as space-separated values using print(" ".join(map(str, arr))). This shows the 
# array after each step of insertion.
#Else if number is greater than or equal to the current element, it assigns number to the position immediately to the right of the current element (i.e., arr[index+1] = number), and then it prints
# the current state of the array. This indicates that number has been correctly placed in its sorted position.
#If number is greater than all the elements in the array, it is placed at the beginning of the array (i.e., arr[0] = number), and the array's current state is printed.


import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    number=arr[n-1]
    for index in range(n-2, -1, -1):
        if number<arr[index]:
            arr[index+1]=arr[index]
            print(" ".join(map(str, arr)))
        else:
            arr[index+1]=number
            print(" ".join(map(str, arr)))
            break               
    if arr[0]>number:
        arr[0]=number
        print(" ".join(map(str, arr)))
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)





#Insertion Sort - Part 2
#A for loop iterates through the array starting from the second element (index 1) and going up to the last element (index n-1). In the loop, the current element at index i is stored
#  (as before we store the number) in the variable 'number.' A variable 'j' is initialized with the value 'i - 1.' This j variable will be used to compare and potentially move elements in 
# the array to insert the value 'number' in its correct position. In fact the while loop continues as long as j is greater than or equal to 0 and 'number' is smaller than the element at index j.
#  So the loop checks if the element at index j is greater than 'number,' and if it is, that element is shifted one position to the right in the array (arr[j+1] = arr[j]).This process
#  continues until it's found the correct position for 'number' and is assigned the value 'number' to arr[j+1]. After each insertion step, the current state of the array is printed as 
# space-separated values using 'print(" ".join(map(str, arr)).

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(1, n):
        number = arr[i]
        j=i-1  
        while j>=0 and number<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = number
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

















