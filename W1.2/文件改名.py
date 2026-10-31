import random
from pathlib import Path
a=Path(__file__).parent/"img"
for file in random.sample(list(a.glob("*.png")),50):
    file.rename(file.with_suffix(".jpg"))
print("Finish")