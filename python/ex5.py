#  def mergeSortedArray(ar1,ar2):
#     i=j=k=0
#     res=[0]*(len(ar1)+len(ar2))
#     while i<len(ar1) and j<len(ar2):
#         if ar2[j]<=ar1[i]:
#             res[k]=ar2[j]
#             k+=1
#             j+=1
#         else:
#             res[k]=ar1[i]
#             k+=1
#             i+=1
#     while j<len(ar2):
#         res[k]=ar2[j]
#         k+=1
#         j+=1
#     while i<len(ar1):
#         res[k]=ar1[i]
#         k+=1
#         i+=1
#     return res
# n=int(input())
# ar1=list(map(int,input().split()))
# m=int(input())
# ar2=list(map(int,input().split()))
# res=mergeSortedArray(ar1,ar2)
# print(res)



# def mergeSortedArray(ar1,ar2,ar3):
#     i=k=0
#     res=[0]*(len(ar1)+len(ar2)+len(ar3))
#     while k<len(res):
#         if i<len(ar1):
#             res[k]=ar1[i]
#             k+=1
#         if i<len(ar2):
#             res[k]=ar2[i]
#             k+=1
#         if i<len(ar3):
#             res[k]=ar3[i]
#             k+=1
#         i+=1
#     return res
# n=int(input())
# ar1=list(map(int,input().split()))
# m=int(input())
# ar2=list(map(int,input().split()))
# o=int(input())
# ar3=list(map(int,input().split()))
# res=mergeSortedArray(ar1,ar2,ar3)
# print(res)
def reArrangeArrays(ar):
    k=0
    res=[0]*len(ar)
    for i in range(len(ar)):
        if ar[i]>0:
            res[k]=ar[i]
            k+=1
    for i in range(len(ar)):
        if ar[i]==0:
            res[k]=0
            k+=1
    return res
n=int(input())
ar=list(map(int,input().split()))
res=reArrangeArrays(ar)
print(res)
