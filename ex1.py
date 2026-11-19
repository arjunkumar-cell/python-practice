# n1=int(input())
# n2=int(input())
# min=n1 if n1<n2 else n2
# for i in range(n2,n1+1,-1):
     
#      if(n1%i==0 or n2%i==0):
# def prime_check(n):
#     if n<2:
#       i  return False
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return False
#     return True

# def print_prime(ar):
#    for i in range(0,len(ar)-1):
#         for j in range(i+1,len(ar)):
#             if prime_check(ar[i])  or prime_check(ar[j]):
#                 print(ar[i],ar[j])
# def print_pairs(ar):
#     max=ar[0]*ar[1]
#     x=ar[0]
#     y=ar[1]
#     for i in range(0,len(ar)-1):
#         for j in range(i+1,len(ar)):
#             if ar[i]*ar[j]<max:
#                 max=ar[i]*ar[j]
#                 x=ar[i]
#                 y=ar[j]
#     print(x*y)

# n=int(input())
# ar=list(map(int,input().split()))   
# print_pairs(ar)
# def func():
#      try:
#           l=[1,2,3,4]
#           i=int(input())
#           print(l(i))
#           return 1
#      except:
#           print("some error occured")
#           return 0
#      finally:
#           print("im always king")
# x=func()
# print(x)
# 
# fruits=["apple","banana","orange","idli","samusa"]
# for index,i in enumerate(fruits):
#      print(index,i)
#      if index==2:
#           print( index,"arjun")
# lst=[10,20,50,30,40]

# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]<lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]
# print(lst)
def ConsonantAlphabetizer(s):
    res=s.split(".")
    my_set = set()
    for i in range(len(res)):
        if res[i] not in my_set:
            my_set.add(res[i])
    ans= sorted(my_set)
    for i in ans:
        if len(i)>3 and len(i)<=10:
            print(i)
s=input()
ConsonantAlphabetizer(s)

