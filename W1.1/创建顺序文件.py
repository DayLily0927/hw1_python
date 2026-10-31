import random
import string
from pathlib import Path
def m():
    a=Path(__file__).parent
    b=a/"img"
    b.mkdir(exist_ok=True)
    
    chars=string.ascii_letters+string.digits
    name=set()
    
    while(len(name)<100):
        pre=" ".join(random.choices(chars,k=4))
        fullname=f"{pre}.png"
        
        if fullname in name:
            continue
        name.add(fullname)
        file_path=b/fullname
        file_path.touch()
    print("Finish")
m()