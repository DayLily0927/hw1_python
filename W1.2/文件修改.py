with open("test.txt","r",encoding="utf-8")as file:
    c=file.read()
    cplus=f"python{c}python"
with open("test.txt","w",encoding="utf-8")as file:
    file.write(cplus)