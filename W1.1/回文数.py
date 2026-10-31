num=input()
s=len(num)
flag=1
for i in range(s):
    if num[i]!=num[s-1-i]:
        flag=0
        break
if flag==1:
    print("yes")
else :
    print("no")    