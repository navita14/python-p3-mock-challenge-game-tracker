class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        game.results.append(self)
        player.results.append(self)
        self.score = score

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if isinstance(value, int) and 1 <= value <= 5000:
            self._score = value
        else:
            raise Exception("not a number between 1 and 5000")
    
 

    


    
    
    
