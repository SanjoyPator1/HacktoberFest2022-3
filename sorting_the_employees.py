# You are a software engineer at an MNC. You are given the task of sorting the employees in your company based on their salary. Perform the task so that the employees, including yourself, will get a bonus from the management.
# CONSTRAINT:

# 0<=salary<=1000000

# Input Description: Number of employees followed by their name and salary

# Output Description: Sorted list of employee names

# Sample Input : 3 Karthik 23000 rohan 81734 varshini 12343

# Sample Output : varshini Karthik Rohan

emp=int(input("No of employees : "))
li=[] #created an empty list to store employees name
k=[]  #created an empty list to store employees salary

for i in range(emp):  # used for loop to enter the employees detain in the respective list
    name=input()
    sal=int(input())
    li.append(name)
    k.append(sal)
# print(li)
# k.sort()
# print(k)

zipped_lists = zip(k, li) #Pair list2 and list1 elements

sorted_zipped_lists = sorted(zipped_lists) #Sort by first element of each pair

sorted_list1 = [element for _, element in sorted_zipped_lists]

print(sorted_list1)
