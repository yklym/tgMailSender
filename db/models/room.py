from .base import Base


class Room(Base):
    def __init__(self, id_name, owner_id, description='', is_private=False, participants_ids=[], max_users=10):
        self.id = id_name
        self.description = description
        self.is_private = is_private
        self.participants_ids = participants_ids
        self.owner_id = owner_id
        self.max_users = max_users
        self.messages = []

    def __repr__(self):
        return "<Room(name='%s', descr='%s', owner_id='%s')>" % (
            self.id, self.description, self.owner_id)
