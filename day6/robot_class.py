class robot:
    def __init__( self, name, radius = 0.15):  #类的基本用法 def __init__(self, a, b, c, d)
        self.name = name
        self.radius = radius
        self.speed = 0

    def move(self, speed):  #set speed
        self.speed = speed
        print(f"{self.name} begin to move,speed is {self.speed}")

    def clac_rps(self):
        circle = 2 *3.14159 * self.radius
        return self.speed / circle

    def stop(self):  #let robot stop
        self.speed = 0
        print(f"the {self.name} had been stop")

    def set_radius(self, radius): #修改radius的值
        self.radius = radius
        print(f"the {self.name} radius has been change to {self.radius}")

bot1 = robot("Kust-Bot")
bot2 = robot("SANY-Bot",radius = 0.2)

bot1.move(2.0)
print(f"wheel_speed is {bot1.clac_rps():.2f} rps")

bot2.move(3.0)
print(f"wheel_speed is {bot2.clac_rps():.2f} rps")

bot1.stop()

bot1.set_radius(0.16)
