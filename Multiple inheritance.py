class Horse:
    def __init__(self, dx):
        self.x_distance = 0
        self.sound = 'Frrr'
        self.dx = dx

    def run(self):
        self.x_distance += self.dx

class Eagle:
    def __init__(self, dy):
       self.y_distance = 0
       self.sound = 'I train, eat, sleep, and repeat'
       self.dy = dy

    def fly(self):
        self.y_distance += self.dy


class Pegasus(Horse, Eagle):
    def __init__(self, dx=10, dy=11):
        super().__init__(dx)
        super(Horse, self).__init__(dy)

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.run()
        self.fly()

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


#p1 = Pegasus()
#print(p1.get_pos())
#p1.move(5, 7)
#print(p1.get_pos())
#p1.voice()
