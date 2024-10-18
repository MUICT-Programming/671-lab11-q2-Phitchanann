# YOUR CODE HERE
list1 = []
list2 = []
updated_list = []

n = int(input())

for i in range(n):
    num = int(input())
    list1.append(num)

for i in range(n):
    num = int(input())
    list2.append(num)

def summation():
    for i in range(n):
        sum = list1[i]+list2[i]
        updated_list.append(sum)
    return updated_list

def find_min_max():
    num_max = max(updated_list)
    num_min = min(updated_list)
    min_max = (num_min,num_max)
    return min_max
 

print(summation())   
print(find_min_max())
