import telebot
from telebot import types
import random
import time

API_TOKEN = "7983561603:AAG_CL2tgOS5VhZszaDDMiCci8LG2J6GdX4"

bot = telebot.TeleBot(API_TOKEN)


CHARACTER_IMAGES = {
    "male_🗡️Воин": "https://imgur.com/eDYRH59",
    "female_🗡️Воин": "https://i.imgur.com/kFUi0VT.png",
    "male_🧙‍♂️Маг": "https://i.imgur.com/YPc1BTM.png",
    "female_🧙‍♂️Маг": "https://i.imgur.com/hxhr4aA.png",
    "male_🏹Лучник": "https://i.imgur.com/jgKK8A0.png",
    "female_🏹Лучник": "https://i.imgur.com/kNwEf1U.png",
}

CHARACTER_DESCRIPTIONS = {
    "male_🗡️Воин": "Сильный и храбрый воин, защитник своего народа.",
    "female_🗡️Воин": "Смелая воительница, мастер ближнего боя.",
    "male_🧙‍♂️Маг": "Мудрый маг, повелитель заклинаний и знаний.",
    "female_🧙‍♂️Маг": "Могущественная чародейка, хранительница древних тайн.",
    "male_🏹Лучник": "Меткий лучник, мастер дальнего боя.",
    "female_🏹Лучник": "Ловкая лучница, несравненная в искусстве стрельбы.",
}



class Player:
    def __init__(self, gender, char_class, name):
        self.gender = gender
        self.char_class = char_class
        self.name = name
        self.hp = 5
        self.max_hp = 5
        self.damage = 1
        self.armor = 1
        self.gold = 50
        self.xp = 0
        self.level = 1
        self.points = 0
        self.potions = 2
        self.training_count = 0
        self.enemy = None
        self.check_alh_kvest = 0
        self.vampire_on = 0
        self.check_location = 0


    def level_up(self):
        if self.xp >= self.level * 100:
            self.level += 1
            self.xp = 0
            self.points += 1
            return True
        return False

    def allocate_point(self, stat):

        if self.points > 0:
            if stat == "hp":
                self.max_hp+=1
                self.hp = min(player.hp + 1, max_hp)
            elif stat == "damage":
                self.damage += 1
            elif stat == "armor":
                self.armor += 1
            self.points -= 1
            return True
        return False

    def __str__(self):
        return (
            f"👤Имя: {self.name}\n"
            f"🚹/🚺Пол: {'Мужской' if self.gender == 'male' else 'Женский'}\n"
            f"⚔️Класс: {self.char_class}\n"
            f"📈Уровень: {self.level}\n"
            f"🛠️Очки прокачки: {self.points}\n"
            f"❤️Здоровье: {self.hp}\n"
            f"💰Золото: {self.gold}\n"
            f"💥Урон: {self.damage}\n"
            f"🛡️Броня: {self.armor}\n"
            f"🎓Опыт: {self.xp}/{self.level * 100}"
        )


enemies = [
   {"name": "🐙Слизь", "hp": random.randint(1, 6), "image_url": "https://i.imgur.com/UP9S8mp.png"},
   {"name": "🧟‍♂️Гоблин", "hp": random.randint(1, 6), "image_url": "https://i.imgur.com/Vj3hBNh.png"},
   {"name": "👹Троль", "hp": random.randint(1, 6), "image_url": "https://i.imgur.com/8pjhBBl.png"}
]

enemies_darkwood = [
   {"name": "🦇Маленький вампир", "hp": random.randint(1, 6), "image_url": "https://imgur.com/FEVDbL8"},
   {"name": "👻Призрак", "hp": random.randint(1, 6), "image_url": "https://i.imgur.com/TdNScT0.png"},
   {"name": "🐺Темный волк", "hp": random.randint(1, 6), "image_url": "https://imgur.com/5RlImor"}
]

ivent_boss_darkwood = [
   {"name": "🧛‍♂️Первородный вампир", "hp": random.randint(25, 45), "image_url": "https://i.imgur.com/jd2m60x.png"},
]

user_data = {}
training_cooldowns = {}


# Команда /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_create = types.KeyboardButton("🛠️Создать персонажа")
    button_creator = types.KeyboardButton("🤖Создатель")
    markup.add(button_create, button_creator)

    photo_url = "https://i.imgur.com/CO8HncI.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        caption=(
            "<b>Добро пожаловать в The Blade and the Ashes! ⚔️</b>\n\n"
            "Вы стоите на пороге волшебного мира, полного тайн и опасностей. "
            "Соберите хорошую экипировку и отправляйтесь навстречу неизвестному!\n\n"
            "✨ Нажмите 'Создать персонажа', чтобы начать своё приключение.\n"
            "✨ Нажмите 'Создатель', чтобы узнать, кто стоит за этим ботом."
        ),
        parse_mode="HTML",
        reply_markup=markup,
    )


@bot.message_handler(func=lambda message: message.text == "🌍✨Начать приключения")
def start_adventure(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_way = types.KeyboardButton("🚗Отправиться в путь")
    button_map = types.KeyboardButton("🗺️Карта")
    button_trainig = types.KeyboardButton("💪Тренироваться")
    button_up = types.KeyboardButton("💪Прокачка")
    button_status = types.KeyboardButton("🧝Статус")

    markup.add(button_way, button_map, button_trainig, button_status, button_up)
    photo_url = "https://i.imgur.com/3cyGUc0.jpeg"
    #bot.send_photo(message.chat.id, photo_url)
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙Путешествие начинается! 🌟\n\nОтправляйтесь в мир, полный опасностей и волшебства! ✨\n\n"
        "После трагической утраты родителей, жизнь главного героя изменилась навсегда. 💔 Оставшись один в опустевшем доме на окраине деревни, он решил не ждать милости судьбы. "
        "Вдохновлённый духом отца и стремлением найти своё место в этом мире, герой собрал немного припасов"
        " 🥾, накинул старый плащ отца 🧥 и вооружился простым мечом ⚔, найденным в заброшенной кузнице.\n\n"
        "С каждым шагом за пределами знакомой деревни мир становился всё более загадочным и манящим. 🌍 Неизведанные земли и скрытые тайны ждут впереди! 🔮"
        "Герой не знал, что его ждёт: эпические приключения, ответы на волнующие вопросы из прошлого или новые испытания на пути. "
        "🤔 Единственное, в чём он был уверен: его путешествие только начинается. 🌱🌟",
        parse_mode="HTML",
        reply_markup=markup,
    )



@bot.message_handler(commands=["sethp"])
def sethp(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]


    command_parts = message.text.split()
    if len(command_parts) < 2:
        bot.send_message(message.chat.id, "Пожалуйста, укажите значение здоровья. Например: /sethp 10")
        return

        new_hp = int(command_parts[1])



        player.hp = new_hp
        bot.send_message(message.chat.id, f"Ваше здоровье установлено на {new_hp} HP.")




@bot.message_handler(func=lambda message: message.text == "💪Провести тренировку")
def training(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]


    current_time = time.time()
    last_training_time = training_cooldowns.get(user_id, 0)
    if player.training_count >= 3 and current_time - last_training_time < 100:
        cooldown_time = int(100 - (current_time - last_training_time))
        bot.send_message(message.chat.id, f"Вы уже провели 3 тренировки. Подождите {cooldown_time} секунд.")
        return

    if current_time - last_training_time >= 300:
        player.training_count = 0

    xp_gain = random.randint(50, 100)
    player.xp += xp_gain
    player.training_count += 1
    training_cooldowns[user_id] = current_time

    # Проверяем уровень
    if player.level_up():
        bot.send_message(message.chat.id, f"Поздравляем! Вы достигли {player.level} уровня! 🎉")

    bot.send_message(message.chat.id, f"Ты хочешь потренироваться, тогда иди за мной\n"
                                      f"Вы потренировались и получили {xp_gain} опыта.")
                                      #f" Текущий уровень:\n{player}")






@bot.message_handler(func=lambda message: message.text == "💪Тренироваться")
def training(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    current_time = time.time()
    last_training_time = training_cooldowns.get(user_id, 0)
    if player.training_count >= 3 and current_time - last_training_time < 50:  # 5 минут
        cooldown_time = int(50 - (current_time - last_training_time))
        bot.send_message(message.chat.id, f"Вы уже провели 3 тренировки. Подождите {cooldown_time} секунд.")
        return

    if current_time - last_training_time >= 300:
        player.training_count = 0

    xp_gain = random.randint(10, 20)
    player.xp += xp_gain
    player.training_count += 1
    training_cooldowns[user_id] = current_time

    if player.level_up():
        bot.send_message(message.chat.id, f"Поздравляем! Вы достигли {player.level} уровня! 🎉")

    bot.send_message(message.chat.id, f"Вы потренировались и получили {xp_gain} опыта.")


@bot.message_handler(func=lambda message: message.text == "💪Прокачка")
def upgrade_menu(message):
    user_id = message.chat.id

    # Проверяем, есть ли игрок
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    if player.points == 0:
        bot.send_message(message.chat.id, "У вас нет очков прокачки. Получите их, повышая уровень!")
        return

    markup = types.InlineKeyboardMarkup()
    hp_button = types.InlineKeyboardButton("❤️➕Увеличить здоровье", callback_data="upgrade_hp")
    damage_button = types.InlineKeyboardButton("🛡️➕Увеличить урон", callback_data="upgrade_damage")
    damage_armor = types.InlineKeyboardButton("⚔️➕Увеличить броню", callback_data="upgrade_armor")
    markup.add(hp_button, damage_button, damage_armor)

    bot.send_message(
        message.chat.id,
        f"Выберите, куда распределить очки. У вас {player.points} очков.\n\n",
        reply_markup=markup,
    )

@bot.callback_query_handler(func=lambda call: call.data in ["upgrade_hp", "upgrade_damage", "upgrade_armor"])
def allocate_points(call):
    user_id = call.message.chat.id
    player = user_data[user_id]

    if call.data == "upgrade_hp":
        if player.allocate_point("hp"):
            bot.answer_callback_query(call.id, "Очко добавлено в здоровье!")
    if call.data == "upgrade_armor":
        if player.allocate_point("armor"):
            bot.answer_callback_query(call.id, "Очко добавлено в броню!")
    elif call.data == "upgrade_damage":
        if player.allocate_point("damage"):
            bot.answer_callback_query(call.id, "Очко добавлено в урон!")

    bot.edit_message_text(
        f"Очки распределены!\n\n",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
    )

@bot.message_handler(func=lambda message: message.text == "🧝Статус")
def show_status(message):
    user_id = message.chat.id
    if user_id in user_data and isinstance(user_data[user_id], Player):
        player = user_data[user_id]

        char_key = f"{player.gender}_{player.char_class}"
        photo_url = CHARACTER_IMAGES.get(char_key, "https://i.imgur.com/default.png")  # URL по умолчанию

        bot.send_photo(
            message.chat.id,
            photo_url,
            caption=(
                f"<b>🛠️Статус персонажа:</b>\n\n"
                f"👤Имя: {player.name}\n"
                f"🚹/🚺Пол: {'Мужской' if player.gender == 'male' else 'Женский'}\n"
                f"⚔️Класс: {player.char_class}\n"
                f"❤️Здоровье: {player.hp}\n"
                f"💥Урон: {player.damage}\n"
                f"🛡️Броня: {player.armor}\n"
                f"💰Золото: {player.gold}"

            ),
            parse_mode="HTML",
        )
    else:
        bot.send_message(
            message.chat.id,
            "У вас ещё нет созданного персонажа. Нажмите 'Создать персонажа', чтобы начать своё приключение!",
            reply_markup=types.ReplyKeyboardRemove(),
        )



@bot.message_handler(func=lambda message: message.text == "🗺️Карта")
def show_map(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_darkcity = types.KeyboardButton("🌆Темный город")
    button_darkwood = types.KeyboardButton("🌲🌑Темнолесье")
    button_forgottencaves = types.KeyboardButton("🗻Забытые пещеры")
    button_holyforest = types.KeyboardButton("🌳✨Святой лес")
    button_exit = types.KeyboardButton("🗺️Убрать карту")

    markup.add(button_darkcity,button_darkwood,button_forgottencaves, button_holyforest, button_exit)
    photo_url = "https://i.imgur.com/wdTZ8UC.png"
    bot.send_photo( message.chat.id,
        photo_url,
        "🌙 На ветхом пергаменте, испещрённом "
        "странными символами и размытыми чернилами, "
        "перед тобой появляются четыре Темный город, Темнолесье, Забытые пещеры. "
        "Каждая из них обладает особой атмосферой и манит своими загадками.",
        parse_mode = "HTML",
        reply_markup = markup
    )

@bot.message_handler(func=lambda message: message.text == "🏕️Сделать привал")
def start_adventures(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_way = types.KeyboardButton("🚗Отправиться в путь")
    button_search = types.KeyboardButton("🔍Исследовать окрестности")
    button_sleep = types.KeyboardButton("📈Отдых")
    button_trainig = types.KeyboardButton("💪Тренироваться")
    button_up = types.KeyboardButton("💪Прокачка")
    button_status = types.KeyboardButton("🧝Статус")

    markup.add(button_way, button_search, button_sleep, button_trainig, button_status, button_up)
    photo_url = "https://i.imgur.com/qbJR5ta.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Вы решили отдохнуть и сделали привал. Но будьте осторожней, рядом могут быть враги враги",
        parse_mode="HTML",
        reply_markup=markup,
    )

def roll_dice():
   return random.randint(1, 6)

def attack(player_attack, enemy_defense):
   return player_attack > enemy_defense

def battle(enemy, message):
   player_turn = True





def create_enemy():
    enemy = random.choice(enemies).copy()  # Создаём копию, чтобы не изменять оригинальный список
    enemy["hp"] = random.randint(1, 6)  # Генерируем здоровье для врага
    return enemy

def create_darkwood_enemy():
    enemy = random.choice(enemies_darkwood).copy()  # Создаём копию, чтобы не изменять оригинальный список
    enemy["hp"] = random.randint(1, 6)  # Генерируем здоровье для врага
    return enemy

def create_boss():
    enemy = random.choice(ivent_boss_darkwood).copy()  # Создаём копию, чтобы не изменять оригинальный список
    enemy["hp"] = random.randint(30, 45)  # Генерируем здоровье для врага
    return enemy

@bot.message_handler(func=lambda message: message.text == "🔍Исследовать окрестности")
def search_way(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    gold_found = random.randint(1, 10)
    choose = random.randint(1, 3)

    player.check_locate = 0


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_search = types.KeyboardButton("🔍Исследовать окрестности")
    button_status = types.KeyboardButton("🏕️Сделать привал")
    markup.add(button_search, button_status)

    if choose == 1:
        photo_url = "https://i.imgur.com/P29CsdT.png"
        bot.send_photo(
            user_id,
            photo_url,
            f"🌙 Вы нашли {gold_found} золота. Это удача! 💰",
            parse_mode="HTML",
            reply_markup=markup,
        )
        player.gold += gold_found

    elif choose == 2:
        photo_url = "https://imgur.com/9W7LXdc"
        bot.send_photo(
            user_id,
            photo_url,
            "🌙 Вы наткнулись на ловушку и потеряли 1 HP! 🩸",
            parse_mode="HTML",
            reply_markup=markup,
        )
        player.hp -= 1

    elif choose == 3:
        enemy = create_enemy()
        player.enemy = enemy

        combat_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        combat_markup.add(
            types.KeyboardButton("⚔️Атака"),
            types.KeyboardButton("🏃‍♂️Сбежать"),
            types.KeyboardButton("🧝Статус"),
            types.KeyboardButton("🧪Использовать зелье"),
        )

        bot.send_photo(
            user_id,
            enemy["image_url"],
            f"🌙 Вы наткнулись на {enemy['name']}! У него {enemy['hp']} HP. Что будете делать?",
            reply_markup=combat_markup,
        )


@bot.message_handler(func=lambda message: message.text in ["⚔️Атака", "🏃‍♂️Сбежать", "🏃💨Убежать", "🧪Использовать зелье"])
def combat(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    if player.enemy is None:
        bot.send_message(user_id, "Врагов поблизости нет.")

    enemy = player.enemy

    if message.text == "⚔️Атака":
        player_roll = roll_dice()
        enemy_roll = roll_dice()

        bot.send_message(
            user_id,
            f"Ты атаковал! Бросок кубика: {player_roll}. Враг защищается! Бросок кубика: {enemy_roll}."
        )

        if player_roll > enemy_roll:
            enemy["hp"] -= player.damage
            bot.send_message(
                user_id,
                f"Ты попал! {enemy['name']} потерял {player.damage} HP. У него осталось {enemy['hp']} HP."
            )
        else:
            bot.send_message(user_id, f"Твой удар не попал! {enemy['name']} уклонился.")

        if enemy["hp"] <= 0:
            random_gold = random.randint(1, 20)
            random_xp = random.randint(1, 20)
            player.gold += random_gold
            player.xp += random_xp


            if enemy["name"] == "Маленький вампир" and player.vampire_on == 0:
                vampire = random.randint(1,3)
                if vampire == 1 :
                    one_check = 1
                    player.vampire_on = 1
                    player.max_hp = player.max_hp + 20
                    player.hp = player.max_hp
                    player.damage += 10
                    if player.gender == "male":
                        if player.char_class == "🧙‍♂️Маг":
                            photo_url = "https://i.imgur.com/xWYlOXM.png"  # Замените на ссылку на ваше фото
                        if player.char_class == "🗡️Воин":
                            photo_url = "https://i.imgur.com/DDpl1KN.png"  # Замените на ссылку на ваше фото
                        if player.char_class == "🏹Лучник":
                            photo_url = "https://i.imgur.com/vWy1KS6.png"  # Замените на ссылку на ваше фото

                        bot.send_photo(
                            message.chat.id,
                            photo_url,
                            "🌙Кровь вампира попала в вашу, поэтому вы стали чувствовать прилив сил. На голове у вас"
                            "появились рога. Ваши физическая и жизненная сила увеличилась.",
                            parse_mode="HTML",
                        )
                    if player.gender == "female":
                        if player.char_class == "🏹Лучник":
                            photo_url = "https://i.imgur.com/zQ2d4xc.png"
                        if player.char_class == "🧙‍♂️Маг":
                            photo_url = "https://i.imgur.com/g3Xhpfh.png"
                        if player.char_class == "🗡️Воин":
                            photo_url = "https://imgur.com/QPV0Zho"
                        bot.send_photo(
                            message.chat.id,
                            photo_url,
                            "🌙Кровь вампира попала в вашу ДНК, поэтому вы стали чувствовать прилив сил. На голове у вас"
                            "появились рога. Ваши физическая и жизненная сила увеличилась.",
                            parse_mode="HTML",
                        )

            bot.send_message(
                user_id,
                f"🌙 Вы победили {enemy['name']}! Вы получили {random_gold} золота и {random_xp} опыта.",
            )
            player.enemy = None
            if player.check_locate == 0:
                search_way(message)
            if player.check_locate == 1:
                interact_with_darkwood(message)
            if player.check_locate == 3:
                the_end(message)


        enemy_roll = roll_dice()
        player_roll = roll_dice()

        bot.send_message(
            user_id,
            f"{enemy['name']} атакует! Бросок кубика: {enemy_roll}. Ты защищаешься! Бросок кубика: {player_roll}."
        )

        if enemy_roll > player_roll:
            player.hp -= random.randint(1, 3)
            bot.send_message(
                user_id,
                f"{enemy['name']} нанес вам урон. Ваше здоровье: {player.hp} HP."
            )
        else:
            bot.send_message(user_id, f"Ты уклонился от атаки {enemy['name']}!")

        if player.hp <= 0:
            bot.send_message(user_id, "Ты был побеждён... Игра окончена!")
            player.enemy = None
            send_welcome(message)


    elif message.text == "🏃‍♂️ь" or message.text == "🏃💨Убежать":
        flee_roll = roll_dice()
        bot.send_message(user_id, f"Ты пытаешься сбежать! Бросок кубика: {flee_roll}.")
        if flee_roll >= 4:
            bot.send_message(user_id, f"Ты успешно сбежал от {enemy['name']}!")
            player.enemy = None
            if player.check_locate == 0:
                search_way(message)
            if player.check_locate == 1:
                interact_with_darkwood(message)
        else:
            bot.send_message(user_id, f"Попытка сбежать не удалась! {enemy['name']} атакует!")

    elif message.text == "🧪Использовать зелье":
        if player.potions > 0:
            player.hp = min(player.hp + 10, player.max_hp)
            player.potions -= 1
            bot.send_message(
                user_id,
                f"Вы использовали зелье! Ваше здоровье восстановлено на 10 HP. Текущее здоровье: {player.hp} HP."
            )
        else:
            bot.send_message(user_id, "У вас нет зелий для использования.")


@bot.message_handler(func=lambda message: message.text == "🚗Отправиться в путь")
def lets_go_way(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_go_darkcity = types.KeyboardButton("🌆Может в темный город")
    button_go_darkwood = types.KeyboardButton("🌲🌑Может в темнолесье")
    button_go_forgottencaves = types.KeyboardButton("🗻Может в забытые пещеры")
    button_go_holyforest = types.KeyboardButton("🌳✨Может в святой лес")
    button_go_sleep = types.KeyboardButton("🏕️Сделать привал")

    markup.add(button_go_darkcity,button_go_darkwood,button_go_forgottencaves, button_go_holyforest, button_go_sleep)

    photo_url = "https://i.imgur.com/DB2YpFY.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Вы стоите у повозки и смотрите на карту. Вы думаете, куда же вам отправиться. Вдруг из повозки к вам кто-то обращается\n\n"
        "- Эй, милашка, по твоему взгляду понятно, что ты отличный искатель приключений. Куда ты хочешь отправиться?",
        parse_mode = "HTML",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "📈Отдых")
def lets_go(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    photo_url_male = "https://i.imgur.com/j1yrdGS.png"  # Замените на ссылку на ваше фото
    photo_url_female = "https://i.imgur.com/HAuRQhG.png"  # Замените на ссылку на ваше фото

    if player.gender == "male":
        player.hp = min(player.hp + 1, player.max_hp)
        bot.send_photo(
            message.chat.id,
            photo_url_male,
            "🌙 Вы хорошо выспались",
            parse_mode = "HTML",
        )
    else:
        player.hp = min(player.hp + 1, player.max_hp)
        bot.send_photo(
            message.chat.id,
            photo_url_female,
            "🌙 Вы хорошо выспались",
            parse_mode = "HTML",
        )


@bot.message_handler(func=lambda message: message.text == "🌆Может в темный город")
def interact_with_driver(message):
    user_id = message.chat.id
    if user_id not in user_data or not isinstance(user_data[user_id], Player):
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pay_button = types.KeyboardButton("Заплатить за поездку")
    no_pay_button = types.KeyboardButton("Не платить")
    markup.add(pay_button, no_pay_button)
    photo_url = "https://i.imgur.com/tMrXr0b.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "Возчик: «ХААХАХ Залазей в повозку? Цена за поездку — 19 золотых монет. Как поступите?»",
        parse_mode="HTML",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "🌳✨Может в святой лес")
def interact_with_driver(message):
    user_id = message.chat.id
    if user_id not in user_data or not isinstance(user_data[user_id], Player):
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    bot.send_message(
        message.chat.id,
        "Извините, но вы не можете попасть в эту локацию, потому что она слишком опасна для вас»",
        parse_mode="HTML",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "🌲🌑Может в темнолесье")
def interact_with_driver(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    player.check_locate = 1

    if player.check_alh_kvest == 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        skip = types.KeyboardButton("⛔Сказать секретное слово")
        skip_button = types.KeyboardButton("↩️Выйти на главную площадь")
        markup.add(skip, skip_button)

        photo_url = "https://i.imgur.com/tMrXr0b.png"
        bot.send_photo(
            message.chat.id,
            photo_url,
            "🌙 Слушай, путник, я не смогу тебя туда довести, потому что там живут эти "
            "мерзкие существа 'вампиры'. Я туда не ногой и тебе не советую",
            parse_mode = "HTML",
            reply_markup=markup

        )
    if player.check_alh_kvest == 0:
        bot.send_message(
            message.chat.id,
            "Извините, но вы не можете попасть"
            " в эту локацию, потому что она слишком опасна для вас»",
            parse_mode = "HTML",
            )


@bot.message_handler(func=lambda message: message.text == "⛔Сказать секретное слово")
def interact_with_driver(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    if player.gold >= 40:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        skip = types.KeyboardButton("✅Хорошо")
        skip_button = types.KeyboardButton("🏕️Сделать привал")
        markup.add(skip, skip_button)

        photo_url = "https://i.imgur.com/H96tLRS.png"
        bot.send_message(
            message.chat.id,
            "🌙 Так ты от той девчушки алхимички. Она нам все уши прожужала, чтобы"
            "мы ее туда отвезли. Мы, конечно, этого не сделали, но ты другое дело. Залезай, но это,"
            "конечно, не бесплатно. Это будет стоить тебе 40 золоты.",
            parse_mode = "HTML",
            reply_markup=markup
        )
    else:
        bot.send_message(
            message.chat.id,
            "Извините, но у тебя нету денег. Приходи, когда появятся деньжата.",
            parse_mode="HTML",
        )

@bot.message_handler(func=lambda message: message.text == "✅Хорошо")
def interact_with_driver(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    skip = types.KeyboardButton("🔍Исследовать эту локацию")
    skip_button = types.KeyboardButton("📈Отдых")
    markup.add(skip, skip_button)

    photo_url = "https://i.imgur.com/rFtZqlA.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Так все, дальше я тебя не повезу. Выходи тут. Я приеду сюда же, чтобы тебя "
        "забрать в полночь. Остерегайся вампиров.",
        parse_mode="HTML",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "🔍Исследовать эту локацию")
def interact_with_darkwood(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    mission = random.randint(1, 100)

    gold_found = random.randint(1, 10)
    choose = random.randint(1, 3)


    if mission > 10:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_search = types.KeyboardButton("🔍Исследовать эту локацию")
        button_status = types.KeyboardButton("🏕️Отдых")
        markup.add(button_search, button_status)

        if choose == 1:
            photo_url = "https://i.imgur.com/P29CsdT.png"
            bot.send_photo(
                user_id,
                photo_url,
                f"🌙 Вы нашли {gold_found} золота. Это удача! 💰",
                parse_mode="HTML",
                reply_markup=markup,
            )
            player.gold += gold_found

        elif choose == 2:
            photo_url = "https://imgur.com/9W7LXdc"
            bot.send_photo(
                user_id,
                photo_url,
                "🌙 Вы наткнулись на ловушку и потеряли 1 HP! 🩸",
                parse_mode="HTML",
                reply_markup=markup,
            )
            player.hp -= 1

        elif choose == 3:
            enemy = create_darkwood_enemy()
            player.enemy = enemy

            combat_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            combat_markup.add(
                types.KeyboardButton("⚔️Атака"),
                types.KeyboardButton("🧝Статус"),
                types.KeyboardButton("🧪Использовать зелье"),
            )

            bot.send_photo(
                user_id,
                enemy["image_url"],
                f"🌙 Вы наткнулись на {enemy['name']}! У него {enemy['hp']} HP. Что будете делать?",
                reply_markup=combat_markup,
            )

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_search = types.KeyboardButton("🚪Открыть дверь!")
        markup.add(button_search)


        photo_url = "https://i.imgur.com/jKOhPH5.png"
        bot.send_photo(
            user_id,
            photo_url,
            "🌙 Вы подходите к огромному замку. Ваши ноги трясуться, но вы все таки решаетесь! 🩸",
            parse_mode="HTML",
            reply_markup=markup,
        )


@bot.message_handler(func=lambda message: message.text == "🚪Открыть дверь!")
def start_adventures(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_search = types.KeyboardButton("🔍Исследовать")
    button_status = types.KeyboardButton("🧝Статус")

    markup.add(button_search, button_status)
    photo_url = "https://i.imgur.com/X9prz7g.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Вы зашли в замок и видите бесчисленное кол-во дверей. Куда же вы пойдете сначала?",
        parse_mode="HTML",
        reply_markup=markup,
    )


@bot.message_handler(func=lambda message: message.text == "🔍Исследовать")
def search_castle(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    gold_found = random.randint(1, 10)
    choose = random.randint(1, 3)

    player.check_locate = 3


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_search = types.KeyboardButton("🔍Исследовать")
    button_status = types.KeyboardButton("🧝Статус")
    button_sleep = types.KeyboardButton("📈Отдых")
    markup.add(button_search, button_status, button_sleep)

    if choose == 1:
        photo_url = "https://i.imgur.com/DQMTj8i.png"
        bot.send_photo(
            user_id,
            photo_url,
            f"🌙 Вы нашли {gold_found} золота. Это удача! 💰",
            parse_mode="HTML",
            reply_markup=markup,
        )
        player.gold += gold_found

    elif choose == 2:
        photo_url = "https://i.imgur.com/TXWZeo1.png"
        bot.send_photo(
            user_id,
            photo_url,
            "🌙 Вы наткнулись на ловушку и потеряли 1 HP! 🩸",
            parse_mode="HTML",
            reply_markup=markup,
        )
        player.hp -= 1

    elif choose == 3:
        enemy = create_boss()
        player.enemy = enemy

        combat_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        combat_markup.add(
            types.KeyboardButton("⚔️Атака"),
            types.KeyboardButton("🧝Статус"),
            types.KeyboardButton("🧪Использовать зелье"),
        )

        bot.send_photo(
            user_id,
            enemy["image_url"],
            f"🌙 Вы наткнулись на {enemy['name']}! У него {enemy['hp']} HP. Что будете делать?",
            reply_markup=combat_markup,
        )



def the_end(message):
    user_id = message.chat.id
    player = user_data[user_id]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    photo_url = "https://imgur.com/oozSHaj"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "Вы смогли убить первородного вампира, но из-за этого стал рушиться замок, потдерживаемый его силой"
        ". Вы успеваете подхватить женщину на плече и сбежать. После этого вы ждете назначенного времени и"
        " покидаете темнолесье.\n\n"
        "После этого вы добираетесь до темного города и видите возсоединение матери и дочки.\n\n"
        "----------------THE END----------------",
        reply_markup=markup,
    )
    send_welcome(message)



















@bot.message_handler(func=lambda message: message.text == "🗻Может в забытые пещеры")
def interact_with_driver(message):
    user_id = message.chat.id
    if user_id not in user_data or not isinstance(user_data[user_id], Player):
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    bot.send_message(
        message.chat.id,
        "Извините, но вы не можете попасть в эту локацию, потому что она слишком опасна для вас»",
        parse_mode="HTML",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "Войти в кузницу")
def go_bs(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = types.KeyboardButton("Ты угадал. Мне нужно укрепить свои силы. Что ты можешь мне предложить?")
    markup.add(answer)

    photo_url = "https://i.imgur.com/UkpXCkz.png"
    bot.send_photo(
        chat_id=user_id,
        photo=photo_url,
        caption=(
            f"{player.name}, о, да кто это пожаловал в мою кузницу? "
            "Гляжу, ты далеко не бродяга, а человек с серьезными намерениями! "
            "Итак, что привело тебя сюда, путник? Ищешь орудие, чтобы прорубить себе "
            "путь сквозь орды врагов, или хочешь защиту, чтобы дожить до завтрашнего дня? "
            "Может, просто потренироваться хочешь, чтобы крепче стать?"
        ),
        parse_mode="HTML",
        reply_markup=markup
    )







@bot.message_handler(func=lambda message: message.text == "Ты угадал. Мне нужно укрепить свои силы. Что ты можешь мне предложить?")
def blacksmith_options(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buy_weapon = types.KeyboardButton("🗡️Купить оружие")
    buy_armor = types.KeyboardButton("🛡️Купить броню")
    train = types.KeyboardButton("💪Провести тренировку")
    exit_button = types.KeyboardButton("↩️Выйти")
    markup.add(buy_weapon, buy_armor, train, exit_button)

    bot.send_message(
        user_id,
        "Я могу предложить тебе:\n"
        "   Оружие для увеличения урона за 5 золотых .\n"
        "   Броню для повышения защиты за 5 золотых.\n"
        "   Тренировку, чтобы стать сильнее.\n"
        "   Выход из кузницы.\n"
        "Что выбираешь?",
        reply_markup=markup
    )




@bot.message_handler(func=lambda message: message.text == "🗡️Купить оружие")
def buy_weapon(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("✅Хорошо, я заплачу")
    no = types.KeyboardButton("❓Извините, но у меня нет таких денег")
    ex = types.KeyboardButton("↩️Выйти")
    markup.add(yes, no, ex)

    photo_url = "https://i.imgur.com/UkpXCkz.png"
    bot.send_photo(
        chat_id=user_id,
        photo=photo_url,
        caption=(
            f"{player.name}, Хорошо, тогда это будет стоить тебе 5 золотых."
        ),
        parse_mode="HTML",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == "🛡️Купить броню")
def buy_armor(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(user_id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("✅Хорошо, я заплачу за броню")
    no = types.KeyboardButton("❓Извините, но у меня нет таких денег")
    ex = types.KeyboardButton("↩️Выйти")
    markup.add(yes, no, ex)

    photo_url = "https://i.imgur.com/UkpXCkz.png"
    bot.send_photo(
        chat_id=user_id,
        photo=photo_url,
        caption=(
            f"{player.name}, Хорошо, тогда это будет стоить тебе 5 золотых."
        ),
        parse_mode="HTML",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text == "✅Хорошо, я заплачу за броню")
def ok(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    if player.gold >= 15:
        player.gold -= 15
        player.armor += 1
        bot.send_message(
            user_id,
            f"Ты приобрёл новую броню! 🗡️\nТеперь твоя зашита увеличен до {player.armor}. "
            f"У тебя осталось {player.gold} золота."
        )
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        agree = types.KeyboardButton("❓Что ты предлагаешь взамен?")
        decline = types.KeyboardButton("💰Нет, я найду деньги.")
        markup.add(agree, decline)

        bot.send_message(
            user_id,
            "Хм, вижу, что у тебя не хватает золота... Но я не всегда работаю за деньги. "
            "Есть и другие способы оплаты, если ты достаточно смелый. Что скажешь?",
            reply_markup=markup
        )


@bot.message_handler(func=lambda message: message.text == "✅Хорошо, я заплачу")
def ok(message):
    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    if player.gold >= 15:
        player.gold -= 15
        player.damage += 1
        bot.send_message(
            user_id,
            f"Ты приобрёл новое оружие! 🗡️\nТеперь твой урон увеличен до {player.damage}. "
            f"У тебя осталось {player.gold} золота."
        )
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        agree = types.KeyboardButton("❓Что ты предлагаешь взамен?")
        decline = types.KeyboardButton("💰Нет, я найду деньги.")
        markup.add(agree, decline)

        bot.send_message(
            user_id,
            "Хм, вижу, что у тебя не хватает золота... Но я не всегда работаю за деньги. "
            "Есть и другие способы оплаты, если ты достаточно смелый. Что скажешь?",
            reply_markup=markup
        )


@bot.message_handler(func=lambda message: message.text == "❓Что ты предлагаешь взамен?")
def alternative_payment(message):
    user_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    accept = types.KeyboardButton("Согласиться")
    refuse = types.KeyboardButton("Отказаться")
    markup.add(accept, refuse)

    bot.send_message(
        user_id,
        "Кузнец хитро улыбается: 'Ну, раз у тебя нет денег, ты можешь... оказать мне услугу. "
        "Ничего сложного, но ты должен быть готов ко всему. Согласен?'",
        reply_markup=markup
    )












def enter_darkcity(message):
    user_id = message.chat.id

    player = user_data[user_id]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    enter_blacksmith = types.KeyboardButton("Войти в кузницу")
    enter_amber_grimoire = types.KeyboardButton("Войти в алхимический магазин")
    back = types.KeyboardButton("🏕️Сделать привал")
    markup.add(enter_blacksmith, enter_amber_grimoire, back)
    photo_url = "https://imgur.com/wH8Kitg"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "Вы входите в город, окружённый высокой каменной стеной,"
        " кажущейся словно вековой. Старая, кованая железная дверь с "
        "громким скрипом отворяется, и перед вами открывается мрачная картина. "
        "Узкие улочки стелются лабиринтом между ветхими домами, из окон которых "
        "едва пробивается свет тусклых фонарей. В воздухе витает тяжёлый запах сырости, "
        "перемешанный с лёгким ароматом горящих дров. Город будто живёт своей жизнью, "
        "скрытой от посторонних глаз, а главной площади, в самом сердце городка, "
        "заметны несколько заведений, каждое из которых обещает не только интерес, но и, возможно, ответы на ваши вопросы.",
        reply_markup=markup,
    )



@bot.message_handler(func=lambda message: message.text == "↩️Выйти")
def exittt(message):
    enter_darkcity(message)


@bot.message_handler(func=lambda message: message.text == "💰Нет, я найду деньги.")
def alternative(message):
    user_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = types.KeyboardButton("↩️Вернуться в город")
    markup.add(back_button)

    bot.send_message(
        user_id,
        "Буду этого с нетерпением ждать!",
        reply_markup=markup
    )
    enter_darkcity(message)


@bot.message_handler(func=lambda message: message.text == "❓Извините, но у меня нет таких денег")
def alternative(message):
    user_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = types.KeyboardButton("↩️Вернуться в город")
    markup.add(back_button)

    bot.send_message(
        user_id,
        "Буду этого с нетерпением ждать!",
        reply_markup=markup
    )
    enter_darkcity(message)


@bot.message_handler(func=lambda message: message.text in ["Согласиться", "Отказаться"])
def payment_choice(message):
    user_id = message.chat.id

    if message.text == "Согласиться":
        bot.send_message(
            user_id,
            "Кузнец кивает с одобрением: 'Вот это по-нашему! Ты оказался не только смелым, но и находчивым.' "
            "После выполнения сделки ты чувствуешь, как твоё оружие становится острее и мощнее.\n\n"
            "Твой урон увеличен на 1."
        )
        user_data[user_id].damage += 1
    elif message.text == "Отказаться":
        bot.send_message(
            user_id,
            "Кузнец хмурится: 'Ну что ж, твой выбор. Приходи, когда у тебя будет достаточно золота.'"
        )
        enter_darkcity(message)

@bot.message_handler(func=lambda message: message.text in ["Заплатить за поездку", "Не платить"])
def handle_driver_choice(message):
    user_id = message.chat.id
    if user_id not in user_data or not isinstance(user_data[user_id], Player):
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]
    choice = message.text

    if choice == "Заплатить за поездку":
        if player.gold >= 19:
            player.gold -= 19
            bot.send_message(
                message.chat.id,
                "Возчик: «Спасибо за оплату! Держитесь крепче, сейчас поедем!»\n"
                f"Ваши оставшиеся золотые: {player.gold}.",
                reply_markup=types.ReplyKeyboardRemove(),
            )
            enter_darkcity(message)

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            accept_button = types.KeyboardButton("Согласиться на предложение возчика")
            decline_button = types.KeyboardButton("Отклонить предложение")
            markup.add(accept_button, decline_button)

            bot.send_message(
                message.chat.id,
                "Возчик: «Похоже, у вас не хватает золота. Пожалуйста, выберите другой вариант.»"
                "«Раз нет монет, я могу предложить тебе альтернативу... — его голос становится мягче, и он улыбается двусмысленно. — Как насчёт услуги за услугу?»\n\n"
                "Вы чувствуете лёгкое напряжение от его слов. Что вы ответите?",
                reply_markup=markup,

            )

    elif choice == "Не платить":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        accept_button = types.KeyboardButton("Согласиться на предложение возчика")
        decline_button = types.KeyboardButton("Отклонить предложение")
        markup.add(accept_button, decline_button)

        bot.send_message(
            message.chat.id,
            "Возчик: «Раз нет монет, я могу предложить тебе альтернативу... — его голос становится мягче, и он улыбается двусмысленно. — Как насчёт услуги за услугу?»\n\n"
            "Вы чувствуете лёгкое напряжение от его слов. Что вы ответите?",
            reply_markup=markup,
        )

@bot.message_handler(func=lambda message: message.text in ["Согласиться на предложение возчика", "Отклонить предложение"])
def handle_driver_alternative(message):
    user_id = message.chat.id
    if user_id not in user_data or not isinstance(user_data[user_id], Player):
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]
    choice = message.text

    if choice == "Согласиться на предложение возчика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        watch_button = types.KeyboardButton("Смотреть")
        skip_button = types.KeyboardButton("Пропустить")
        markup.add(watch_button, skip_button)

        bot.send_message(
            message.chat.id,
            "🚗 Возчик: «Отлично, рад, что мы договорились. Не каждый день встречаются такие смелые путники!»\n\n"
            "Вы можете решить, будете ли наблюдать за происходящим.",
            reply_markup=markup,
        )
        enter_darkcity(message)
    elif choice == "Отклонить предложение":
        bot.send_message(
            message.chat.id,
            "🚗 Возчик: «Ну что ж, ваше право. Будете искать другой способ добраться. Удачи, путник!»\n\n"
            "Он уезжает, оставив вас в раздумьях.",
            reply_markup=types.ReplyKeyboardRemove(),
        )
        start_adventure(message)

@bot.message_handler(func=lambda message: message.text in ["Смотреть", "Пропустить"])
def handle_watch_event(message):
    choice = message.text

    if choice == "Смотреть":
        bot.send_message(
            message.chat.id,
            "🔞 Возчик, явно довольный вашим согласием, приказал опустится на колени, "
            "не отводя от вас взгляда. Твои движения были неуверенными, "
            "потому что ты делал это впервые. Вы ощутили тепло, "
            "смешанное с легким ароматом пота.Сначала было неловко, а "
            "затем волнение смешалось с удивлением. Тело реагировало быстрее, "
            "чем разум мог осознать происходящее. В голове мелькали мысли — "
            "то ли смущение от интимности момента, то ли чувство "
            "странной власти над ситуацией.\n\n Возчик, похоже, полностью сосредоточился на своем 'предложении',"
            " выполняя его с таким усердием, словно от этого зависела его жизнь. "
            "Его движения становились всё более уверенными, а вы не могли решить,"
            " смотреть ли ему в глаза или просто отвлечься мыслями куда-то вдаль. "
            "После завершения возчик, поднялся, и, будто ничего не случилось, "
            "сказал с легкой усмешкой:\n\n -Ну что ж, договор — есть договор. Давайте отправляться, путник.\n\n Вы чувствовали лёгкое замешательство, "
            "будто перешли какую-то черту. Смешение странной гордости и смущения оставило след в "
            "вашем сознании, но поездка продолжалась, как ни в чём не бывало.",
            reply_markup=types.ReplyKeyboardRemove(),
        )
    if choice == "Пропустить":
        bot.send_message(
            message.chat.id,
            "🚗 Вы отворачиваетесь, предпочитая не наблюдать за происходящим. Возчик, довольный сделкой, взмахивает поводьями, и вы отправляетесь в путь.",
            reply_markup=types.ReplyKeyboardRemove(),
        )


@bot.message_handler(func=lambda message: message.text == "🌳✨Святой лес")
def darkwood(message):
    photo_url = "https://i.imgur.com/3RNazW1.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Описание: Светлый и тихий, он манит своей красотой. "
        "Но за этой спокойной картиной прячется тайна, "
        "а умные взгляды зверей будто изучают каждого, кто войдёт.\n\n Противники: Единороги.",
        parse_mode = "HTML",
    )

@bot.message_handler(func=lambda message: message.text == "Войти в алхимический магазин")
def alhimichka_kvest(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    watch_button = types.KeyboardButton("Войти")
    skip_button = types.KeyboardButton("↩️Выйти на главную площадь")
    markup.add(watch_button, skip_button)

    photo_url = "https://i.imgur.com/TelCE2X.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Вы стоите у огромной двери, которая немного приоткрыта. Над ней вы видите надпись, 'Зелья от Саи'",
        parse_mode = "HTML",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "Войти")
def alhimichka_kvest(message):

    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    if player.check_alh_kvest == 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        skip = types.KeyboardButton("Ответить ей")
        skip_button = types.KeyboardButton("↩️Выйти на главную площадь")
        markup.add(skip, skip_button)

        photo_url = "https://i.imgur.com/H96tLRS.png"
        bot.send_photo(
            message.chat.id,
            photo_url,
            "🌙 Вы входите в магазинчик и слышите детский плач. Вы подходите ближе и видите девочку сидящую на стуле. Вы окликиваете ее и он от неожиданности всхлипывает сильнее.\n\n"
            "- Что ты здесь делаешь? Ты что не видел вывиску закрыто",
            parse_mode = "HTML",
            reply_markup=markup

        )

    if player.check_alh_kvest == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        skip_button = types.KeyboardButton("↩️Выйти на главную площадь")
        markup.add(skip_button)

        photo_url = "https://i.imgur.com/anUwTSV.png"
        bot.send_photo(
            message.chat.id,
            photo_url,
            "🌙 Вы входите в крошечный магазинчик. "
            "Внутри царит странная тишина, будто время остановилось. "
            "Полки покрыты слоем пыли, а воздух наполнен тонким запахом "
            "старости и забвения. Вам кажется, что здесь давно никого не "
            "было, но ощущение чьего-то взгляда не покидает вас...",
            parse_mode = "HTML",
            reply_markup=markup
        )
    player.check_alh_kvest = 1


@bot.message_handler(func=lambda message: message.text == "Ответить ей")
def alhimichka_kvest(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    watch_button = types.KeyboardButton("Помочь девочке")
    skip_button = types.KeyboardButton("↩️Выйти на главную площадь")
    markup.add(watch_button, skip_button)

    bot.send_message(
        message.chat.id,
        "🌙 Извини, но я не заметил ее и дверь была открыта. Почему ты плачешь? Может я могу помочь.\n\n"
        "Как ты можешь мне помоч? Вчера моя мама отправилась в темнолеьсе, чтобы найти 'олотые гребы', но так и не вернулась. И никто не хочет мне помоч,"
        "потому что бояться 'короля темнолесья'. Теперь ты хочешь мне помоч?",
        parse_mode = "HTML",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "Помочь девочке")
def alhimichka_kvest(message):

    user_id = message.chat.id

    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала создайте персонажа!")
        return

    player = user_data[user_id]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    skip_button = types.KeyboardButton("↩️Выйти на главную площадь")
    markup.add(skip_button)

    if player.gender == "male":
        photo_url = "https://i.imgur.com/akzUfE1.png"
        bot.send_photo(
            message.chat.id,
            photo_url,
            "🌙 Девочка смотрит с выпученными глазами и нас и не верит вашим словам."
            "-Чт...Что? Ты правда поможешь? Если ты спасешь мою маму, мы будем тебе век обязаны"
            "Вот держи это тебе. Чтобы ты быстро добрался. Сейчас возчики просто так никого не перевозят туда,"
            "но если ты скажешь 'Воблинус', то они тебя довезут. Еще раз спасибо тебе.\n\n"
            "Она подбегает к тебе и прыгает в объятия.",
            parse_mode = "HTML",
            reply_markup=markup
        )
    else:
        photo_url = "https://imgur.com/weUgu7E"
        bot.send_photo(
            message.chat.id,
            photo_url,
            "🌙 Девочка смотрит с выпученными глазами и нас и не верит вашим словам."
            "-Чт...Что? Ты правда поможешь? Если ты спасешь мою маму, мы будем тебе век обязаны"
            "Вот держи это тебе. Чтобы ты быстро добрался. Сейчас возчики просто так никого не перевозят туда,"
            "но если ты скажешь 'Воблинус', то они тебя довезут. Еще раз спасибо тебе.\n\n"
            "Она подбегает к тебе и прыгает в объятия.",
            parse_mode = "HTML",
            reply_markup=markup
        )
    player.check_alh_kvest = 2


@bot.message_handler(func=lambda message: message.text == "↩️Выйти на главную площадь")
def leave(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    watch_button = types.KeyboardButton("Войти в кузницу")
    skip_button = types.KeyboardButton("Войти в алхимический магазин")
    skip_button1 = types.KeyboardButton("🏕️Сделать привал")
    markup.add(watch_button, skip_button, skip_button1)

    bot.send_message(
        message.chat.id,
        "🌙 Вы выходите на главную площадь. Куда дальше?",
        parse_mode = "HTML",
        reply_markup=markup
    )



@bot.message_handler(func=lambda message: message.text == "🗻Забытые пещеры")
def darkwood(message):
    photo_url = "https://i.imgur.com/TmYJ8ir.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Описание: Тёмные своды, уходящие вглубь земли. "
        "На стенах древние письмена и следы времени. "
        "Те, кто спускался туда, редко "
        "возвращались с ясным рассудком.\n\n Противники: Гоблины.",
        parse_mode = "HTML",
    )

@bot.message_handler(func=lambda message: message.text == "🌲🌑Темнолесье")
def darkwood(message):
    photo_url = "https://i.imgur.com/hOnxb2l.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Описание: Лес, где ветви деревьев сомкнулись так плотно, "
        "что свет здесь чужак. Говорят, его тропы меняют путь,"
        "а шёпот в ветвях зовёт путников по имени.\n\n Противники: Вампиры, Тролли.",
        parse_mode = "HTML",
    )

@bot.message_handler(func=lambda message: message.text == "🌆Темный город")
def darkcity(message):
    photo_url = "https://i.imgur.com/UaJf0Fl.png"
    bot.send_photo(
        message.chat.id,
        photo_url,
        "🌙 Описание: Место вечного заката, "
        "где узкие улочки искажены тенью. "
        "Площадь с единственным фонарём, горящим тусклым светом, "
        "будто зовёт к себе тех, кто не боится тайн. Тут вы можете приобрести все, что душе угодно, главное знать, где искать.",
        parse_mode = "HTML",
    )


@bot.message_handler(func=lambda message: message.text == "Сбросить всё и начать заново")
def reset_data(message):
    bot.send_message(message.chat.id, "Все данные сброшены. Вы можете начать создание персонажа заново! 🌀", reply_markup=types.ReplyKeyboardRemove(),)
    send_welcome(message)



@bot.message_handler(func=lambda message: message.text == "🤖Создатель")
def show_creator(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_back = types.KeyboardButton("Назад")
    markup.add(button_back)
    bot.send_message(
        message.chat.id,
        "<b>Бот создан с любовью 💜</b>\n\n"
        "<b>╔════════════════════════╗</b>\n"
        "║ Автор: @zxccccccer.ㅤㅤㅤㅤㅤㅤㅤㅤㅤ ║\n"                  
        "║ Спасибо, что используете этого бота!  ║\n"
        "<b>╚════════════════════════╝</b>",
        parse_mode="HTML",
        reply_markup=markup,
    )

@bot.message_handler(func=lambda message: message.text == "Назад")
def back_to_menu(message):
    send_welcome(message)

@bot.message_handler(func=lambda message: message.text == "🗺️Убрать карту")
def back_to_adventure(message):
    start_adventure(message)


@bot.message_handler(func=lambda message: message.text == "🛠️Создать персонажа")
def choose_gender(message):
    markup = types.InlineKeyboardMarkup()
    male_button = types.InlineKeyboardButton("👨‍🦱Мужчина", callback_data="male")
    female_button = types.InlineKeyboardButton("👩‍🦰Женщина", callback_data="female")
    markup.add(male_button, female_button)
    bot.send_message(message.chat.id, "❓Выберите пол персонажа:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["male", "female"])
def choose_class(call):
    user_data[call.from_user.id] = {"gender": call.data}
    markup = types.InlineKeyboardMarkup()
    warrior_button = types.InlineKeyboardButton("🗡️Воин", callback_data="🗡️Воин")
    mage_button = types.InlineKeyboardButton("🧙‍♂️Маг", callback_data="🧙‍♂️Маг")
    archer_button = types.InlineKeyboardButton("🏹Лучник", callback_data="🏹Лучник")
    markup.add(warrior_button, mage_button, archer_button)
    bot.edit_message_text(
        "❓Выберите класс персонажа:",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=markup,
    )

@bot.callback_query_handler(func=lambda call: call.data in ["🗡️Воин", "🧙‍♂️Маг", "🏹Лучник"])
def ask_name(call):
    user_data[call.from_user.id]["class"] = call.data
    user_data[call.from_user.id]["is_creating"] = True
    bot.send_message(call.message.chat.id, "❓Введите имя вашего персонажа:")


@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id].get("is_creating", False))
def finalize_character(message):
    user_id = message.chat.id
    name = message.text
    gender = user_data[user_id]["gender"]
    char_class = user_data[user_id]["class"]

    # Создаем объект Player
    player = Player(gender, char_class, name)
    user_data[user_id] = player

    char_key = f"{gender}_{char_class}"
    bot.send_photo(
        message.chat.id,
        CHARACTER_IMAGES[char_key],
        caption=f"{CHARACTER_DESCRIPTIONS[char_key]}\n\n{player}",
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_adventure_button = types.KeyboardButton("🌍✨Начать приключения")
    reset_button = types.KeyboardButton("❌Сбросить всё и начать заново")


    markup.add(start_adventure_button, reset_button)
    bot.send_message(
        message.chat.id,
        "✅Ваш персонаж готов к приключениям! Что вы хотите сделать?",
        reply_markup=markup,
    )





if __name__ == "__main__":
   bot.polling(none_stop=True)
