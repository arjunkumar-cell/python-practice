
def mul(ar):
    sum=1
    for i in range(len(ar)):
        sum=sum*ar[i]
    return sum
# def min(ar):
#     min=ar[0]
#     for i in range(len(ar)):
#         if ar[i]<min:
#             min=ar[i]
#     return min
# def max(ar):
#     max=ar[0]
#     for i in range(len(ar)):
#         if ar[i]>max:
#             max=ar[i]
#     return max
def productarray(ar):
    prod=mul(ar)
    res=[0]*len(ar)
    for i in range(len(ar)):
        res[i]=prod//ar[i]
    return res



n=int(input())
ar=list(map(int,input().split()))
ans=productarray(ar)
print(ans)