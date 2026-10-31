count=0
sum=0
for i in range(5):
    if i==0:
        continue
    for j in range(5):
        if j==0:
            continue
        for m in range(5):
            if m==0:
               continue
            if i!=j and j!=m and i!=m:
                count+=1
                sum=i*100+j*10+m
                print(sum)
print(count)