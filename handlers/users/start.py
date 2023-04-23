from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def caesar_cipher(text: str, shift: int) -> str:
    result = ''
    for char in text:
        if char.lower() in ALPHABET:
            index = ALPHABET.index(char.lower())
            shifted_index = (index + shift) % len(ALPHABET)
            shifted_char = ALPHABET[shifted_index]
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    # Command '/start' handler
    text = 'Привет, это шифр Цезаря! Введи сообщение на английском, которое нужно зашифровать.'
    await message.answer(text=text)

@dp.message_handler()
async def cmd_caesar_cipher(message: types.Message):
    # Caesar cipher handler
    shift = 3  # сдвиг
    encrypted_text = caesar_cipher(message.text, shift)
    text = f'Зашифрованное сообщение: {encrypted_text}'
    await message.answer(text=text)
