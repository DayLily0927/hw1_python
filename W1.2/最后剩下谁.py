people=list(range(1,234))
count=0#如果连续报数
while len(people)>1:
    people1=[]
    for i in people:
        count+=1
        if count%3!=0:
            people1.append(i)
    people=people1
print(people[0])