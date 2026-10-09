import random

raw = [round(random.gauss(2.0,0.1),3) for i in range(20)]

print(raw)
print("the last of five number:",raw[0:5])
print("the end of number",raw[-1])
print("total number:",len(raw))

avg = sum(raw)/len(raw)
print(f"average is :{avg:.2f} maxima is {max(raw):.2f} minima is:{min(raw)}")
