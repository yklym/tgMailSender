from common.keyboards import main_keyboard_markup
from common.states import JoinRoomBotState
from db.repositories import RoomRepository, UserRepository
from handlers.utils.filters import is_private_chat
from loader import bot


@bot.message_handler(func=is_private_chat, commands=['start'])
def start(message):
    sub_commands = message.text.split(' ')
    if len(sub_commands) > 1:
        room_id = ' '.join(sub_commands[1].split('_'))
        room = RoomRepository.get_by_id(room_id)

        if room.password:
            UserRepository.set_state(message.db_user.id, JoinRoomBotState.TRY_PASS)
            UserRepository.set_target_room(message.db_user.id, room_id)
            bot.send_message(message.chat.id, f'Вас було запрошено до кімнати {room_id}!\n'
                             'Що продовжити уведіть пароль:')
        else:
            RoomRepository.add_participant(room_id, message.db_user.id)
            bot.send_message(message.chat.id, f'Вас було додано до кімнати {room_id}!')
    else:
        bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}\n',
                         reply_markup=main_keyboard_markup)
