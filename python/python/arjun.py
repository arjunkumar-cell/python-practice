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
# student={}
# while True:
#     print("1.display")
# #     print("2.add student")
# #     print("3.pop student")
# #     print("4.exit")
# #     choice=int(input("enter your choice 1-4"))
# #     if choice==1:
# #         for key,value in student.items():
# #             print(key,value)
# #     elif choice==2:
# #         name=input("enter name")
# #         percentage=int(input("enter your percentage"))
# #         student[name]=percentage
# #     elif choice==3:
# #         name=input("enter name of the student to pop")
# #         if name in student:
# #    for         student.pop(name)
# #     elif choice==4:
# #         print("exting")
# #         break
# #     else:
# #         print("invalid choice")


# def smallestWord(s):
#     words=s.split()
#     for word in words:
#         print(word+(str(len(word))),end=" ")
# s=input()
# smallestWord(s)



# def check(s):
#     max_len=s[0]
    
#     for word in s[1:]:
#         if len(word) < len(max_len):
#             max_len=word
#     return max_len




# n=input()
# arr=n.split()

# print(check(arr))

# class account:
#     def __init__(self,name,accno):
#         self.name=name
#         self.accno=accno
#         self._balance=0
#     def check_balance(self):
#         print(f" your balance:{self._balance}")
#     def deposit(self,amount):
#         self._balance+=amount
#         print(f"deposited succesfully and your balance is {self._balance}")
#     def withdraw(self,amount):
#         if self._balance>=amount:
#             self._balance-=amount
#         else:
#             print("please enter valid amount")
# class savingsAccount(account):
#     def intrest(self):
#         interest_rate=0.04
#         interest=self._balance*interest_rate
#         print(f"calculated interest is {interest}")
# class curentAccount(account):
#     def withdraw(self,amount):
#         overdraft_amount=1000
#         if self._balance + overdraft_amount>=amount:
#             self._balance-=amount
#             print(f"withdrawn succesful {self._balance}")
#         else:
#             print("pls enter valid amount")
# class bank:
#     def __init__(self,name,branch):
#         self.name=name
#         self.branch=branch
#         self.__account={}

#     def createAccount(self,id,holder_name,type):
#         if type=="savings":
#             new_account=savingsAccount(holder_name,id)
#         elif type=="current":
#             new_account=curentAccount(holder_name,id)
#         self.__account[id]=new_account
#         return new_account

#     def getAccount(self,id):
#         if id not in self.__account:
#             print("account not founfd")
#             return None
#         else:
#             accounta1=self.__account[id]
#             print(f"account found {accounta1}")
#             return accounta1
# cbk=bank("unioun bank","thokot")
# c1=cbk.createAccount(101,"arjun","savings")
# s1=cbk.createAccount(102,"abhi","current")
# c1.deposit(1000)
# s1.deposit(200)
# c1.withdraw(1500)
# s1.withdraw(500)

# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         self.__marks={}
#     def get_marks(self):
#         return self.__marks

#     def add_marks(self,subject,marks):
#         self.__marks[subject]=marks
#     def calculate_average(self):
#         total=0
#         for mark in self.__marks.values():
#             total+=mark
#         average=total/len(self.__marks)
#         return average
#     def is_passed(self):
#         has_passed=all(mark<35 for mark in self.__marks.values())
#         if has_passed:
#             print(f"{self.name} is  passed")
#         else:
#             print(f"{self.name} is  failed")
#     def calculate_grade(self):
#         percentage=self.calculate_average()*100
#         if percentage>=90:
#             print("A")
#         elif percentage>=80:
#             print("B")
#         else:
#             print("C")
# class reportGenerate:
#     @staticmethod
#     def generate(student:student):
#         student_marks=student.get_marks()
#         print(f"name:{student.name} rollno:{student.rollno}")
#         print("******marks*******")
#         for subject,mark in student_marks.items():
#             print(f"{subject}-{mark}")
#         print("******marks*******")
#         print(f"average:{student.calculate_average()}")
#         student.is_passed()
#         student.calculate_grade()
# class classrrom:
#     def __init__(self,rollno,name):
#         self.name=name
#         self.rollno=rollno
#         self.__student=[]

#     def add_student(self,student):
#         self.__student.append(student)
#     def get_student(self):
#         for student in self.__student:
#             print(f"{student.rollno}.{student.name}")

# s=student("arjun",1)
# s.add_marks("amths",66)
# s.add_marks("science",26)
# cls=classrrom("10","B")
# cls.add_student(s)
# cls.get_student()
try:
    age=int(input("enter the age"))
    print(f"Age is:{age}")
except Exception as e:
    print("error occured:",e)
finally:
    print("thank you")

    







