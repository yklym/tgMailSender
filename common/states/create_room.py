from .base import BaseBotState


class CreateRoomBotState(BaseBotState):
    NONE = 'none'
    GET_ROOM_NAME = 'get_room_name'
    GET_ROOM_DESCRIPTION = 'get_room_description'
    GET_ROOM_PASS = 'getRoomPass'
