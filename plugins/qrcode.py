#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


import os
from pyrogram import Client,Filters
from telegraph import upload_file
import pyqrcode 
import png 
from messages import msg


@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        
        chat_id=message.chat.id,
        text=f"<b>Hello {message.from_user.first_name}, My Name Is 𝗤𝗥𝗖𝗢𝗗𝗘 𝗙𝗟𝗜𝗫 𝗕𝗢𝗧. 🥳\n\nI'm A <u>𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗤𝗥𝗖𝗢𝗗𝗘 𝗦𝗖𝗔𝗡𝗡𝗘𝗥 𝗕𝗢𝗧.</u>\n\nSend Me A Link/Text To Convert It Into 𝗤𝗥𝗖𝗢𝗗𝗘.\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @Modzilla 𝗜𝗳 𝗬𝗼𝘂 𝗟𝗼𝘃𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 ♥️.</b>",
        reply_to_message_id=message.message_id,
        parse_mode = "html" 
    )
    
@Client.on_message(Filters.text & Filters.private)
async def qrcode(client, message):
    qr = await client.send_message(
        chat_id=message.chat.id,
        text=f"Making your QR Code... 😁",
        reply_to_message_id=message.message_id  
    )
    s = str(message.text)
    qrname = str(message.from_user.id)
    qrcode = pyqrcode.create(s)
    qrcode.png(qrname + '.png', scale = 6) 
    img = qrname + '.png'
    await qr.edit_text("Uploading... ⏫")
    try:
        response = upload_file(img)
    except Exception as error:
        await qr.edit_text(f"{msg.error}")
        return
    try:
        await message.reply_photo(photo=img)

    except Exception as error:
        print(error)

    await qr.edit_text(f"https://telegra.ph{response[0]}")

    try:
        os.remove(img)
    except Exception as error:
        print('Somting is {error}')
         
