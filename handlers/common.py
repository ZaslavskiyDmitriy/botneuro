from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keyboard.keyboards import kb1, kb2
from utilts.cat import cat


router = Router()


#Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
 name = message.chat.first_name
 await message.answer(f'Привет, {name}', reply_markup=kb1)


#хэндлер на команду /?
@router.message(F.text.lower() == 'ты кто?')
async def cmd_rg(message: types.Message):
  name = message.chat.first_name
  await message.answer(f'Я бот и я люблю котиков, {name}')

#хэндлер на команду /закрыть 
@router.message(Command('закрыть'))
@router.message(F.text.lower() == 'закрыть')
async def cmd_rg(message: types.Message):
  name = message.chat.first_name
  await message.answer(f'Хорошего дня, {name}')


#Хэндлер на команду /cat
@router.message(Command('cat'))
@router.message(Command('котики'))
@router.message(F.text.lower() == 'покажи котиков')
async def cmd_cat(message: types.Message):
  name = message.chat.first_name
  img_cat = cat()
  await message.answer(f'Держи котиков, {name}')
  await message.answer_photo(photo=img_cat)




#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
 msg_user = message.text.lower()
 name = message.chat.first_name
 if 'привет' in msg_user:
  await message.answer(f'Как дела?, {name}')
 elif 'Хорошо,а у тебя?' == msg_user:
   await message.answer(f'Все замечательно, {name}')
 elif 'кот' in msg_user:
  await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
 else:
   await message.answer(f'Я не знаю такого слова')