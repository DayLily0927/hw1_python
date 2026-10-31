with open ("test.txt","r",encoding="utf-8")as f1,\
     open ("copy_test.txt","r",encoding="utf-8")as f2:
         l1=f1.readlines()
         l2=f2.readlines()
         err=[]
         l=min(len(l1),len(l2))
         lm=max(len(l1),len(l2))
         for i in range(l):
             if l1[i]!=l2[i]:
                 err.append(i+1)
         if l!=lm:
             for i in range(l,lm):
                 err.append(i+1)
print(err)