# st="A@1yush"
# uppercnt=0
# lowercnt=0
# di=0
# specialchr=0
# for i in range(len(st)):
#     if st[i].isupper():
#         uppercnt+=1
#     elif st[i].islower():
#         lowercnt+=1
#     elif st[i].isdigit():
#         di+=1
#     else:
#         specialchr+=1            

# print("the upper count is :",uppercnt)    
# print("the lower case count is :",lowercnt)    
# print("the digits count is :",di)    
# print("the special character count is :",specialchr)

# st="Ayush"
# # for i in range(len(st)):
# #     print(i)

# for i in range(len(st)-1,-1,-1):
#     print(st[i],end="")    

n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))
if n1>n2 and n1>n3:
    greatest=n1
elif n2>n1 and n2>n3:
    greatest=n2
else:
    greatest=n3

print(greatest)    

n='a'
print(n.isalpha())