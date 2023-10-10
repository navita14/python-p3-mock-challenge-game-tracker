class Result:
    def __init__(self, player, game, score):
        self.player = player #link result.player
        self.game = game
        game.results.append(self)
        player.results.append(self)
        self.score = score

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if 1 <= new_score <= 5000:
            self._score = new_score
        else:
            raise ValueError("not a number between 1 and 5000")
    
 

    


    
    
    
