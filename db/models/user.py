from common.states import CommonBotState
from .base import Base


class User(Base):
    def __init__(self, tg_user=None, state=CommonBotState.DEFAULT_STATE):
        self.state = state
        self.tmp_room = dict()

        if not tg_user:
            return
        print(tg_user)
        self.id = tg_user.id
        self.name = tg_user.first_name

        self.fullname = self.__get_fullname(tg_user.first_name, tg_user.last_name)
        self.username = tg_user.username
        self.target_room = ''
        self.muted_list = []

    @staticmethod
    def __get_fullname(first_name, second_name):
        fullname = first_name
        if second_name:
            fullname += ' ' + second_name
        return fullname

    def __repr__(self):
        return "<User(name='%s', username='%s', state-'%s')>" % (
            self.name, self.username, self.state)
