import random
import string
i=int(input())
chars=string.ascii_letters+string.digits+string.punctuation
with open ("test.txt","w",encoding="utf-8") as file:
    for j in range(i):
        l=random.randint(10,20)
        w=''.join(random.choices(chars,k=l))
        file.write(w)
        if j<i-1: file.write(f"\n")
with open ("test.txt","r",encoding="utf-8")as file:
    c=file.read()
with open ("copy_test.txt","w",encoding="utf-8")as file:
    file.write(c)
print("Finish")