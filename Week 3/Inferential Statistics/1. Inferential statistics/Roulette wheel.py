import random

class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1,37):
            self.pockets.append(i)
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0     # return 1 dollar if player bet right color
        self.pocketOdds = len(self.pockets) - 1.0   
    
    def spin(self):
        self.ball = random.choice(self.pockets)
    
    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10) or (self.ball > 18 and self.ball <= 28)):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1
    
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()
    
    def betBlack(self, amt):
        if self.isBlack():
            return amt*self.blackOdds
        else:
            return -amt
    
    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else:
            return -amt*self.redOdds
    
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else: 
            return -amt
    
    def __str__ (self):
        return "fair roulette"

def playroulette(game, numSpins, toPrint = True):
    luckyNumber = '2'
    bet = 1
    toRed, toBlack, toPocket = 0.0, 0.0, 0.0
    for i in range(numSpins):
        game.spin()
        toRed += game.betRed(bet)
        toBlack += game.betBlack(bet)
        toPocket += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, ' spins of ', game)
        print('Expected return betting red = ' + str(100*toRed/numSpins) + '%')
        print('Expected return betting black = ' + str(100*toBlack/numSpins) + '%')
        print('Expected return betting ' , luckyNumber, ' = '+ str(100*toPocket/numSpins) + '%')
    return (toRed/numSpins, toBlack/numSpins, toPocket/numSpins)

numSpins = 1000000
game = FairRoulette()
playroulette(game, numSpins)
