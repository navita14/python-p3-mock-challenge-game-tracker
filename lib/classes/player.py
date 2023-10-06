class Player:
    def __init__(self, username):
        self.username = username
        self.results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if isinstance(value,str) and 2 <= len(value) <= 16:
            self._username = value
        else:
            raise Exception("this_username_is_too_long")
    
    def games_played(self):
        new_games = []
        for result in self.results:
            new_games.append(result.game) 
        return new_games

    def has_played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False
 
    def num_times_played(self, game):
        x = 0
        for i in self.games_played():
            if i == game:
                x += 1
        return x
            
