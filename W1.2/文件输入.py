import random
with open ("data1.txt","w",encoding="utf-8") as file:
    for i in range(30):
        file.write(f"{random.randint(1,100)}")
        file.write(f" ")
        if (i+1)%3==0:
            file.write(f"\n")
nums=[]
with open ("data1.txt","r",encoding="utf-8") as file:
    a=file.readlines()
    for i in a:
        for j in i.split():
            num=int(j)
            nums.append(num)
nums1=[]
count=0
for i in range(len(nums)):
    if i%3==1:
        nums1.append(nums[i])
        count+=nums[i]
nums1.sort()
ave=count/10
ave1=(nums1[4]+nums1[5])/2
print(nums1[0],nums1[9],ave,ave1)
