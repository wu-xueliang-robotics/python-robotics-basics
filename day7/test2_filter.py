import random
class Filter:
    def __init__ (self, window = 5):
        self.window = window
        self.history = []

    def add(self, value):
        self.history.append(value)
        if len(self.history) < window:
            return value
        recent = self.history[-self.window:]
        return sum(recent)/self.window

    def reset(self):
        self.history = []
        print("filter has been reset")

class RangeFilter(Filter):
    def __init__ (self, window = 3 ,max_range = 5.0):
        super().__init__(window)
        self.window = window
        self.max_range = max_range

    def add(self, value):
        if value > self.max_range:
            return None

        self.history.append(value)

        if len(self.history) < self.window:
            return sum(self.history) / len(self.history)
        else:
            recent = self.history[-self.window:]
            return sum(recent) / self.window

    def stats(self):
        if not self.history:
            return "there not have date"

        count = len(self.history)

        return f"total have {count}, maxima is {max(self.history)},minima is {min(self.history)}"

f = RangeFilter(window = 3,max_range = 5)

raw = [round(random.gauss(2.0,0.1),3) for i in range(15)]

raw[4] = 7.0
raw[9] = 6.0

print(f"origin date:{raw}")

for v in raw:
    r = f.add(v)

    if r is None:
        print(f"input:{v:5.2f} is diable to use ->input is too large")
    else:
        print(f"input {v:.2f} -> {r:.3f}")

print(f"result is :{f.stats()}")
