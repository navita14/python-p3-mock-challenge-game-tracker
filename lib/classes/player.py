class Player:
    def __init__(self, username):
        self.username = username
        self.results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise ValueError("this_username_is_too_long")
    
    def games_played(self):  #games instances
        new_games = []
        for result in self.results:
            new_games.append(result.game) 
        return new_games

    def has_played_game(self, game):
        # if game in self.games_played():
        #     return True
        # else:
        #     return False
        
        
        #another way
        # for result in self.results:
        #     if self.game == game:
        #         return True
        # return False

        #another way
        return game in self.games_played()
 
    def num_times_played(self, game):
        # x = 0
        # for i in self.games_played():
        #     if i == game:
        #         x += 1
        # return x

        count = 0
        for result in self.results:
            if result.game == game:
                count += 1
        return count
            

    def __repr__(self) -> str:
        return f'<Player {self.username}>'