import random

raw = []
for i in range(20):
    raw.append(random.gauss(2.0,0.1))

raw = [round(random.gauss(2.0,0.1),3)for i in range(20)]

print(raw)
print("前五个：", [f"{x:.2f}" for x in raw[0:5]])
print(f"last is :{raw[-1]}:.2f")
print(f"total have :{len(raw)}")

avg = sum(raw) / len(raw)
print(f"average is {avg:.2f} max number is {max(raw):.2f} min number is {min(raw):.2f}")
