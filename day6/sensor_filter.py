import random
class SensorFilter:
    def __init__(self, window = 5):
        self.window = window
        self.history = []

    def add(self, value):
        self.history.append(value)
        if len(self.history) < self.window:
            return value
        recent = self.history[-self.window:]
        return sum(recent) / self.window

    def reset(self):
        self.history = []
        print("filter has been reset!!")
#验收逐个打印原始-->滤波，数据不足五个时返回原值，不报错#
f = SensorFilter(window = 5)
raw = [random.gauss(2.0,0.1)for i in range(20)]

for v in raw:
    filtered = f.add(v)
    print(f"origin is {v:.2f} -> filtered to {filtered:.2f}")
