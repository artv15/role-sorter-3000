import os


TOKEN = os.environ.get('BOT_TOKEN') #Токен бота. Получается с config var BOT_TOKEN
REGENERATED = 0

POST_ID = 722505136890707988 #Пост с которого должна читаться реакция

ROLES = {
    '✅': 718805239226040336 #CLASS-D role
    } #Роли для выдачи по эмоциям.

EXCROLES = {719617447031734313, 718580201897984061, 718579578335133857, 718578603943526401, 719609937021501440, 720641991389478923} #Роли для исключения

MAX_ROLES_PER_USER = 1 #Лимит ролей для 1-го пользователя