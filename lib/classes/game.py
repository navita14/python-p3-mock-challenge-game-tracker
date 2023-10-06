class Game:
    def __init__(self, title):
        self.title = title
        self.results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value,str) and len(value) > 0:
            self._title = value
        else:
            raise Exception(f"not {value}")
    

    def get_players(self):
        new_players = []
        for result in self.results:
            new_players.append(result.player)
        return new_players
    
    def average_score(self, player):
        total = 0
        for result in self.results:
            if result.player == player:
                total = result.score + total
        return (total / len(self.results))


# Game("Skribbl.io")
# print(Game("Skribbl.io").title)

# Game(9)
# print(Game(9).title)
