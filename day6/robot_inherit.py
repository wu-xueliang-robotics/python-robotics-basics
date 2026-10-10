class Robot:
    def __init__ (self, name, radius = 0.15):
        self.name = name
        self.radius = radius
        self.speed = 0

    def move(self, speed):
        self.speed = speed
        print(f"{self.name} move speed is {self.speed} m/s")

    def status(self):
        return f"{self.name}:speed = {self.speed}"

class WarehouseRobot(Robot):
    def __init__ (self, name, radius = 0.15, task = "check"):
        super().__init__(name,radius)
        self.task = task

    def patrol(self):
        print(f"{self.name} begin to work:{self.task}")

    def status(self):
        return f"[仓库]{super().status()} task = {self.task}"

class ArmRobot(Robot):
    def __init__ (self, name, radius = 0.15):
        super().__init__(name, radius)
        self.holding = None

    def grab(self, target):
        self.holding = target
        print(f"{self.name} have hold {self.holding}")

    def status(self):
        return f"[arm] {super().status()} holding = {self.holding}"

bot = Robot("normal bot")
wbot = WarehouseRobot("SANY-Inspector", task = "巡检货架")

bot.move(2.0)
print(bot.status())

wbot.move(3.0)
wbot.patrol()
print(wbot.status())

armbot = ArmRobot("SANY_Arm")
armbot.move(1.5)
armbot.grab("box")
print(armbot.status())
