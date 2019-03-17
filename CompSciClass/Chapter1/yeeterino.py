

class player:
    def __init__(self,health,holding):
        self.health = health
        self.holding = holding
    
    def stats(self):
        return 'Health:{} \nHolding:{}'.format(self.health, self.holding)



p1 = player(50,"sword")
p2 = player(6,"dagger")

print(p1.stats())

