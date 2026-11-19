
# def mul(ar):
#     sum=1
#     for i in range(len(ar)):
#         sum=sum*ar[i]
#     return sum
# # def min(ar):
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
# def productarray(ar):
#     prod=mul(ar)
#     res=[0]*len(ar)
#     for i in range(len(ar)):
#         res[i]=prod//ar[i]
#     return res



# n=int(input())
# ar=list(map(int,input().split()))
# ans=productarray(ar)
# print(ans)
class shape:
    def draw(self):
        print("drawing shape")
    def make(self):
        print("making shape")
class circle(shape):
    def draw(self):
        print("drawing circle")
    def make(self):
        print("making circle")
class rectangle(shape):
    def draw(self):
        print("drawing rectangle")
    def make(self):
        print("making rectangle")
def my_shape(s):
    s.draw()
    s.make()
def main():
    print("1.circle \n 2.rectangle")
    n=int(input())
    if n==1:
        s=circle()
    elif n==2:
        s=rectangle()
    my_shape(s)
if __name__=="__main__":
    main()