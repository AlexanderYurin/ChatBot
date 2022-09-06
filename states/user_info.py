from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    command = State()
    city = State()
    count_city = State()
    start_date = State()
    finish_date = State()
    photo = State()
    count_photo = State()
    price = State()
    distance = State()



