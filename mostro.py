class Entity:
    def __init__(self, x, y, field):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self)
    def move(self, motion):
        if motion == "w"  and self.y > 0:
            self.y -= 1
        elif motion == "s"  and self.y < field.h - 1:
            self.y += 1
        elif motion == "a"  and self.x > 0:
            self.x -= 1
        elif motion == "d"  and self.x < field.w - 1:
            self.x += 1

class Monster(Entity):
    def __init__(self, x, y, name, damage, field):
        super().__init__(x, y, field)
        self.name = name
        self.hp = 50
        self.damage = damage

class Field:
    def __init__(self):
        self.w = 5
        self.h = 5
        self.entities = []

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if y == e.y and x == e.x:
                        print('[X]', end = '')
                        break
                else:
                    print('[ ]', end = '')
            print()

field = Field()
m = Monster(2, 2, "Pikachu", 50, field)

while True:
    field.draw()
    move = input("Per far muovere il mostro digitare 'w' per salire, 's' per scendere, 'a' per andare verso sinistra e 'd' per andare verso destra. Per interrompere digitare 'STOP': ")
    if move == "STOP":
        quit()
    m.move(move)
