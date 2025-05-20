import asyncio
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest

session_name = 'online_session'  # сохраняется в этом файле

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        phone = input("Введи номер (в формате +7...): ")
        await client.send_code_request(phone)
        code = input("Введи код из Telegram: ")
        await client.sign_in(phone, code)

    print("Ты теперь вечно онлайн...")
    while True:
        try:
            await client(UpdateStatusRequest(offline=False))
            await asyncio.sleep(30)  # обновляем онлайн каждые 30 секунд
        except Exception as e:
            print("Ошибка:", e)
            await asyncio.sleep(10)

with client:
    client.loop.run_until_complete(main())
