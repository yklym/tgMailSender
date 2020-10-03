from .base import Base


class User(Base):
    def __init__(self, id: str, name: str, fullname: str, username: str):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.username = username

    def __repr__(self):
        return "<User(name='%s', fullname='%s', username='%s', curr_game_id='%s')>" % (
            self.name, self.fullname, self.username, self.curr_game_id)
