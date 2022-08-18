from threading import Lock

from models.minefield import Minefield


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Barman(metaclass=SingletonMeta):
    """
    His main task is return game object by id_game
    """

    def __init__(self):
        self.dict_games = {}

    def add_game(self, id_game, dif_mode='easy'):
        if self.dict_games:
            self.dict_games.popitem()

        self.dict_games[id_game] = Minefield(dif_mode)

    def take_game(self, id_game):
        return self.dict_games[id_game]

    def del_game(self, id_game):
        self.dict_games.pop(id_game)
