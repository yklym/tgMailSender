from common.states import CommonBotState
from .base import Base


class User(Base):
    def __init__(self, tg_user=None, state=CommonBotState.DEFAULT_STATE):
        self.state = state
        self.tmp_room = dict()

        if not tg_user:
            return

        self.id = tg_user.id
        self.name = tg_user.first_name
        self.fullname = tg_user.first_name + ' ' + tg_user.last_name
        self.username = tg_user.username

    def __repr__(self):
        return "<User(name='%s', fullname='%s', username='%s', state-'%s')>" % (
            self.name, self.fullname, self.username, self.state)
