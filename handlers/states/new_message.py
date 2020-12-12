from common.states import NewMessageBotState, CommonBotState, JoinRoomBotState
from db.repositories import RoomRepository, UserRepository
from loader import bot
from ..utils.filters import check_state, apply_many, is_private_chat


@bot.message_handler(
    func=lambda m: apply_many(m, lambda mess: check_state(mess, NewMessageBotState.NEW_MESSAGE), is_private_chat))
def add_message(message):
    RoomRepository.add_message(message.db_user.target_room, message.text)
    target_room = RoomRepository.get_by_id(message.db_user.target_room)
    UserRepository.set_state(message.db_user.id, CommonBotState.DEFAULT_STATE)

    for user_id in target_room.participants_ids:
        user_receiver = UserRepository.get_by_id(user_id)
        if  message.db_user.target_room not in user_receiver.muted_list:
            bot.send_message(chat_id=user_id,
                             text=f"Ви отримали нове повідомлення у кімнаті <b>{message.db_user.target_room}</b>",
                             parse_mode='HTML')

@bot.message_handler(
    func=lambda m: apply_many(m, lambda mess: check_state(mess, JoinRoomBotState.TRY_PASS), is_private_chat))
def add_message(message):
    room = RoomRepository.get_by_id(message.db_user.target_room)

    UserRepository.set_state(message.db_user.id, CommonBotState.DEFAULT_STATE)

    if message.text == room.password:
        RoomRepository.add_participant(room.id, message.db_user.id)
        bot.send_message(message.chat.id, f'Вас було додано до кімнати {room.id}!')
    else:
        bot.send_message(message.chat.id, f'Вам не вдалося увійти за паролем, спробуйте ще раз перейти за посиланням!')
