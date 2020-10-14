from .base import Base


class Room(Base):
    def __init__(self, id_name, owner_id, description='', is_private=False, participants_ids=[], max_users=10):
        self.id = id_name
        self.description = description
        self.is_private = is_private
        self.participants_ids = participants_ids
        self.owner_id = owner_id
        self.max_users = max_users

    def __repr__(self):
        return "<User(name='%s', fullname='%s', username='%s', state-'%s')>" % (
            self.name, self.fullname, self.username, self.state)
