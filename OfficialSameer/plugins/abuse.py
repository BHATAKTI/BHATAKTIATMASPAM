import asyncio

import os

import random

from telethon import events

from telethon import functions, types

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from OfficialSameer import SAM, SAM2, SAM3, SAM4, SAM5 , SAM6, SAM7, SAM8, SAM9, SAM10, SAM11, SAM12, SAM13, SAM14, SAM15, SAM16, SAM17, SAM18, SAM19, SAM20, SAM21, SAM22, SAM23, SAM24, SAM25, SAM26, SAM27, SAM28, SAM29, SAM30, SAM31, SAM32, SAM33, SAM34, SAM35, SAM36, SAM37, SAM38, SAM39, SAM40, SUDO_USERS

from resources.data import DEADLYSPAM

from .. import CMD_HNDLR as hl

  

    

@idk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@ydk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@wdk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@sdk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@hdk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@adk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@bdk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@cdk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@edk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@ddk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@vkk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@kkk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@lkk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@mkk.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@sid.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@shy.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@ana.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@ake.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@eel.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@khu.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@shi.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@yaa.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@dav.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@raj.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

@put.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))

 

async def _(e):

    usage = "**Module Name = BIRTHDAY**\n\nCommand:\n\n ..bday <Username of User>\n\nit will continuously birthday until you restart!!."

    if e.sender_id in SUDO_USERS:

        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):

            return await e.reply(usage, parse_mode=None, link_preview=None )

        DEADLYSPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        bitxh = await e.get_reply_message()

        if len(DEADLYSPAM) == 1:

            user = str(DEADLYSPAM[0])

            a = await e.client.get_entity(user)

            g = a.id

            if int(g) in DEADLYSPAM:

                text = f"I can't bdy @ZINDA_H_TU_MERE_LIYE_HEART_HACK Owner"

                await e.reply(text, parse_mode=None, link_preview=None )

            elif int(g) in SUDO_USERS:

                text = f"This guy is a sudo user."

                await e.reply(text, parse_mode=None, link_preview=None )

            else:

                c = a.first_name

                name = f"[{c}](tg://user?id={g})"

                caption1 =f"{name} HAPPY BIRTHDAY JANNI"

                caption2 =f"{name} **𝙂𝙊𝘿 𝘽𝙇𝙀𝙎𝙎 𝙏𝙊 𝙐❤️**"

                caption3 =f" {name} 𝙈𝘼𝙔 𝘽𝙀 𝙇𝙊𝙉𝙂 𝘼 𝘼𝙇𝙄𝙑𝙀 𝙏𝙄𝙈𝙀"

                caption4 =f" {name} 𝘽𝙃𝘼𝙂𝙒𝘼𝙉 𝙏𝙀𝙆𝙊 𝙎𝘼𝘽 𝙆𝙃𝙐𝙎𝙃𝙄 𝘿𝙀💜"

                caption5 =f"{name} **𝙏𝙐 𝙑𝙊 𝙃 𝙅𝙊 𝙇𝘼𝙆𝙃𝙊 𝙈 𝙈𝙄𝙇𝙏𝘼 𝙃🔥🎉🎉**"

                caption6 =f" {name} __𝘼𝙅𝙅𝙅 🎉🎉𝙋𝘼𝙍𝙏𝙔 𝘿𝙄𝙔𝙊 𝙎𝘼𝘽 𝘿𝙊𝙎𝙏𝙊 𝙆𝙊__ 🤤"

                caption7 =f"# {name} 𝙇𝘼𝙇𝘼𝙇𝘼𝙇𝘼𝙇𝘼𝙇𝘼 𝙃𝘼𝙋𝙋𝙔 𝘽𝙄𝙍𝙏𝙃𝘿𝘼𝙔 𝘿𝘼𝙍𝙇𝙄𝙉𝙂🔥🎉"

                caption8 =f"{name} **𝙏𝙐 𝙈𝙀𝙍𝙀 𝙇𝙄𝙁𝙀 𝙆𝘼 𝙀𝙆 𝘼𝘼𝙄𝙎𝘼 𝙎𝘼𝙆𝙎 𝙃 𝙅𝙄𝙎𝙆𝙊 𝙈 𝙆𝘼𝘽𝙃𝙄 𝙉𝙊𝙄 𝘽𝙃𝙐𝙇𝙐𝙉𝙂𝘼🔥🎉😁**"

                caption9 =f"{name} 𝙃𝘼𝙋𝙋𝙔 𝘽𝙄𝙍𝙏𝙃𝘿𝘼𝙔 𝙏𝙐 𝙅𝙄𝙔𝙀 🙀1000 𝙎𝘼𝙇𝙇 𝘽𝙎𝘿𝙆❤️"

                caption10 =f"{name} __AGAYA SWADH__"

                caption11 =f"{name} **𝕋𝕌 𝕄𝔼ℝ𝔼 𝕃𝕀𝔽𝔼 𝕂𝔸 𝔹𝔼𝕊𝕋 ℙ𝔼ℝ𝕊𝕆ℕ ℍ😌❤️**"

                caption12 =f"**𝚃𝚄 𝚅𝙷𝙸 𝙷 𝙽𝙰 𝙹𝙾 𝙰𝙹𝙹 𝙿𝙰𝚁𝚃𝚈 𝙽𝙰 𝙳𝙰𝙽𝚈 𝙺 𝙻𝙸𝚈𝙴 𝙾𝙵𝙵 𝚁𝙷𝙴𝙶𝙰😌**"

                caption13 =f"**🅜🅔🅡🅔 🅓🅞🅢🅣 🅣🅔🅡🅔 🅢🅐🅜🅝🅨 🅣🅞 🅗🅐🅡 🅔🅚 🅒🅗🅘🅙 🅚🅐🅐🅜 🅗**"

                caption14 =f"__Haiii__"

                caption15 =f"{name} TERE B⃗I⃗R⃗T⃗H⃗D⃗A⃗Y⃗ P⃗R⃗ T⃗E⃗R⃗E⃗ G⃗F⃗/B⃗F⃗ K⃗I⃗ U⃗M⃗A⃗R⃗ T⃗E⃗K⃗O⃗ L⃗A⃗G⃗ J⃗A⃗Y⃗❤️🥰"

                caption16 =f"🆃🅰🅿🅰"

                caption17 =f"🆃🅰🅿"

                caption18 =f"🆃🅰🅿🅰"

                caption18 =f"🆃🅰🅿"

                caption20 =f"__A̶J̶J̶J̶ P̶A̶R̶T̶Y̶ H̶O̶G̶I̶ N̶O̶N̶ S̶T̶O̶P̶🎉🎉🙈🙈🙈_"

                caption21 =f"{name} 𝗧𝗘𝗥𝗜 𝗠𝗔A̶M̶I̶ 🎉K̶O̶ B̶O̶L̶U̶N̶G̶A̶ 🙂T̶E̶L̶E̶ P̶R̶ L̶A̶D̶K̶I̶/L̶A̶D̶K̶A̶ B̶A̶J̶I̶ K̶A̶R̶T̶A̶ H̶🤣🤣🔥🎉🤧"

                caption22 =f"🤤"

                caption23 =f"{name} __𝑂𝑁𝐿𝐼𝑁𝐸 𝐴𝐴🤦‍♂️ 𝑃𝐴𝑅𝑇𝑌 𝐷𝐸𝑁𝑌 𝐾 𝑇𝐼𝑀𝐸 𝑂𝐹𝐹 𝐶𝐻𝐿𝐴/𝐶𝐻𝐴𝐿𝐼 𝐺𝑌𝐼__🤤🤤"

                caption24 =f"{name} __𝐎𝐍𝐋𝐈𝐍𝐄 𝐀𝐀𝐀 𝐘𝐀 𝐆𝐇𝐀𝐑 𝐒𝐄 𝐔𝐓𝐇𝐀𝐔🔥🎉🎉🎉__"

                caption25 =f"{name} __𝐌𝐄𝐑𝐄 𝐓𝐑𝐅 𝐒𝐄 𝐓𝐎𝐅𝐅𝐀 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎁🎁__"

                caption26 =f"{name} __#𝐇𝐀𝐏𝐏𝐘_𝐁𝐈𝐑𝐓𝐇𝐃𝐀𝐘_𝐌𝐄𝐑𝐄_𝐉𝐀𝐀𝐍✨🎊🎊🎊🎊🎊🎊🎊🎊🎊__ 🤤🤤"

                caption27 =f"😂✨🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🤣"

                caption28 =f"😂"

                caption29 =f"__𝐆𝐎𝐃 𝐁𝐋𝐄𝐒𝐒 {name} 𝐓𝐎 𝐔 𝐁𝐒𝐃𝐊 𝐓𝐔 𝐉𝐀𝐀𝐍 𝐇 𝐌𝐄𝐑𝐄🎉🥺__"

                caption30 =f"{name} **𝐉𝐁𝐁 𝐓𝐔𝐌 𝐎𝐍𝐋𝐈𝐍𝐄 𝐍𝐇𝐈 𝐀𝐀𝐓𝐀/𝐀𝐀𝐓𝐈 𝐌𝐄𝐊𝐎 𝐀𝐋𝐎𝐍𝐄 𝐅𝐄𝐋𝐋 𝐇𝐎𝐓𝐀 𝐇🥺💔__ \n\n _ {name} 𝐋𝐎𝐁𝐄 𝐔❤️🧡❤️💜🤍🖤🤎💜💙💚💛🧡❤️💖💝💘__"

                fuk = e.chat_id

                async with e.client.action(bdy, "typing"):

                        await e.client.send_message(bdy, caption1)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption2)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption3)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption4)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption5)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption6)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(fuk, caption7)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption8)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption9)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption10)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption11)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption12)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption13)

                        await asyncio.sleep(0.4)

                        await e.client.send_message(bdy, caption14)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption15)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption16)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption17)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption18)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption19)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption20)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption21)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption22)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption23)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption24)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption25)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption26)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption27)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption28)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption29)

                        await asyncio.sleep(0.3)

                        await e.client.send_message(bdy, caption30)

                        await asyncio.sleep(0.3)

        else:

             await e.reply(usage)
