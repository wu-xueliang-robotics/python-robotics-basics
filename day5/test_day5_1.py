import random

ran = []
ran = {round(random.gauss(5,0.2),3) for i in range(30)}

avg = sum(ran)/len(ran)
print(ran)
print(f"maxima is :{max(ran)} ,minima is :{min(ran)}")
