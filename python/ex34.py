
# def checkVowels(s):
#     t="" miss
#     for i in range(len(s)):
#         if(s[i]>="A" and s[i]<="Z" ):
#             t=t+s[i]
#     for i in range(len(s)):
#         if(s[i]>="a" and s[i]<="z"):
#             t=t+s[i]
#     sum=0
#     for i in range(len(s)):
#         if s[i]>="0" and s[i]<="9":
#             sum=sum+s[i]
#             t=t+sum
#     return t
            
# s=input()
# res=checkVowels(s)
# print(res)

# def evenSubarrays(ar):
#     for size in range(1,len(ar)+1):
#         for i in range(0,len(ar)-size+1):
#             subarray=ar[i:i+size]
#         pi    if size%2==0:
#                 print(*subarray)
#         return None
# n=int(input())
# ar=list(map(int,input().split()))
# res=evenSubarrays(ar)
# print(res)





#  0123 45678910111213 14 15 16
#### OP:hello_____arjun
    #01234567891011
# s="mississippi"
# miss
# issi
# ssis
# siss
# issi
# ssip      for(start,stop,step)
# sipp
# ippi
# s=input()
# for i in range(0,len(s)-4+1):
#     print(s[i:i+4])






# hereiamhackerrank
# hackerank

# def checkPalindrome(s):
#     return s==s[::-1]
# def checkSubstring(s1):
#     for size in range(1,len(s1)):
#         for i in range(len(s1)-size+1):
#             t=""
#             for j in range(i,i+size):
#                 t=t+s1[j]
#             if(checkPalindrome(t)):
#                 print(t)
# s1=input()
# res=checkSubstring(s1)
# print(res)ss




# s="india is my country"
# word=s.split()
# print(*word[::-1])   #country is my india




# s="india is my country"
# word=s.split()
# t=""
# for i in word:
#     t=t+ (i[::-1])
# print(t)


# s="india is my country"
# word=s.split()
# t=""
# for i  in word:
#     if len(i)>=3:
#         t=t+i+"5"
#     else:
#         t=t+i+"2"
# print(t)
 
# 01234
# hello

#s1:mississippi
# t:miss
# issi
# ssis
# siss
# issi
# ssip      for(start,stop,step)    
# sipp
# ippi
#s2:issi    yes    no
# def checkPalindrome(s):
#     return s==s[::-1]
# def subString(s):
#     for size in range(1,len(s)+1):
#         for i in range(0,len(s)-size+1):
#             t=""
#             for j in range(i,i+size):
#                 t=t+s[j]
#             if checkPalindrome(t):
#                 print(t)

# s=input()
# res=subString(s)
# print(res)
# op:country is my india
#  01234 01 01 0123456
# op=india5 is2 my2 country5
# s="india is my country"
# word=s.split()
# t=""
# for i in word:
#     t=t+i+str(len(i))
# print(t)
# s="how are you"
# word=s.split()
# for i in word:     
#     print(i)
# def greet(name,age):
#     print(f"Name: {name}, Age: {age}")
# greet("hohb",25)
# def removeCharacters(s):
#     my_set=set()
#     t=""
#     for i in range(len(s)):
#         if s[i] not in my_set:
#             my_set.add(s[i])
#             t=t+s[i]
#     print(t)
# s=input()
# removeCharacters(s)
    
   

  #        1  2  3
# s=india is my country

# op:isindia mycountry


# def countWords(s):
#     count=0
#     for i in range(len(s)-1):
#         if s[i]==" " and s[i+1]!=" ":
#             count+=1
#     return count if s[0]==" "  else  count+1

# def reverse(s):
#     t=""
#     for i in range(len(s)-1,-1,-1):
#          t=t+s[i]
#     return t

       




# def split(s):
#     words=countWords(s)
#     ar=['']*words
#     j=0
#     t=""
#     for i in range(len(s)):
#         if s[i]!=" ":
#             t=t+s[i]    
#         elif len(t)>0:
#             ar[j]=t
#             j+=1
#             t=""
#     if len(t)>0:
#         ar[j]=t
#     return ar
# s=input()              
# res=split(s)
# for i in range(len(res)):
#     print(reverse(res[i]),end=" ")



# def characterLen(s):
#     d={}
#     for i in range(len(s)):
#         if s[i] in d:
#             c=d.get(s[i])
#             d[s[i]]=c+1
#         else:
#             d[s[i]]=1
#     for key,value in d.items():
#         # value=d.get(key) 
#         print(key+str(value),end="")
# s=input()
# characterLen(s)


# def reverseWords(s):
#     words=s.split()
#     t=""
#     for i in range(len(words)-1,-1,-1):
#         t=t+words[i][::-1]+" "
#     return t.strip()
# s=input()
# res=reverseWords(s) 
# print(res)
# # for i in range(len(res)-1,-1,-1):
# #     print(res[::-1],end="")
# from functools import reduce
# my_list=[1,2,3,4,5]
# res=reduce(lambda x: x%2==0,my_list)
# print(res)
# class customer:
#     def __init__(self,name,balance):
#         self.__name=name
#         self.__balance=balance
#     def get_balance(self):
#         return self.__balance
#     def get_name(self):
#         return self.__name
#     def set_balance(self,balance):
#         self.__balance=balance
#     def set_name(self,name):
#         self.__name=name
    

# def main():
#     c1=customer("arjun",10000)
#     print(c1.get_name())
#     c1.set_name("abhi")
#     print(c1.get_name())
#     print(c1.get_balance())
#     c1.set_balance(15000)
#     print(c1.get_balance())
# if __name__=="__main__":
#     main()
    

# def specialCharcterCount(s):
#     vowels="aeiouAEIOU"
#     t=""
#     for i in range(len(s)):
#         if s[i] not in vowels:
#             t=t+s[i]
#     return t
# s=input()
# res=specialCharcterCount(s)
# print(res)
class shapes:

    def calculate_area(self):
        pass
class circle(shapes):
    def __init__(self,r):
        self.r=r
    def calculate_area(self):
        return 3.14*self.r*self.r
class rectangle(shapes):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        return self.length*self.breadth
c=circle(10)
r=rectangle(10,12)
print(c.calculate_area())
print(r.calculate_area())


