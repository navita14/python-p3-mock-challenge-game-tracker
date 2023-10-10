class Game:
    def __init__(self, title):
        self.title = title
        self.results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if len(new_title) > 0:
            self._title = new_title
        else:
            raise ValueError(f"not {value}")
    

    def get_players(self):  #player instances list
        new_players = []
        for result in self.results:
            new_players.append(result.player)
        return new_players
    
    def average_score(self, player):
        # total = 0
        # for result in self.results:
        #     if result.player == player:
        #         total = result.score + total
        # return (total / len(self.results))
        total = 0
        count = 0
        for result in self.results:
            if result.player == player:
                total += result.score
                count += 1
        return total / count




# Game("Skribbl.io")
# print(Game("Skribbl.io").title)

# Game(9)
# print(Game(9).title)
