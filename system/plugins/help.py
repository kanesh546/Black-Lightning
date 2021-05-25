# Copyright (C) 2021 KeinShin@Github.








# import sys
# import os
# from sys import path
# dir_path = "/absolute/path/to/E:\on_cmd-UserBot"
# sys.path.insert(0, dir_path)
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nltk.util import Index
from pyrogram.methods import messages


from system.Config import Variable
from system.decorators import ERRORS_NAME
from system.plugins import light
from system import CMD_LIST, COMMAND_HELP, bot, app, SUDO_USER_NO_OF_TIME_USED
from pyrogram.errors import BotInlineDisabled
import logging
import pandas as pd

HNDLR = str(Variable.HNDLR)

g =  Variable.TG_BOT_USER_NAME
# unofficial_or_no_help = 0
@light.on(["help"])
async def helper(client, message):
        count = 0
        try:

         txt = message.text
        except IndexError as e:
          await message.edit(e)
        if " " in  txt:
          text = message.text.split()[1]
          try:
             string = ""
             o = str(COMMAND_HELP[text])
         
            #  for i in o:
                 
            #      string += HNDLR +  i + "\n"
            #      string += "\n"
            #      count += 1
             await message.edit(f"🐱‍🚀** Commands in {text}**🐱‍🚀\n\n`{o}`")
          except KeyError:


            search = text
            values = []
            a = ""
            for value in COMMAND_HELP.values():
              if search in value:
              
                    values.append(value)

            item = text         
            item2  = ""
            stored = ""
            for key, value,  in COMMAND_HELP.items():
                if item in value:
                    
                    item2 += "\n" + key
            a = "'s help"
            await message.edit(f"**ERROR! No command with name {text} perhaps you mean  stored in `{item2}` ?**")
            return
          except BaseException as e:
            await message.edit(f"ERROR!: {e}")
        else:
           try:
                if not g.startswith("@"):
                  logging.error("You should have '@' with your bot's username eg -:@{} not like -: {}".format(g, g))
                  await app.send_message(message.chat.id, "**You should have '@' with your bot's username eg -:@{} not like -: {}**".format(g, g))
                  return
                await message.delete()
                bot_results = await client.get_inline_bot_results(f"{g}", "Menu")
                await client.send_inline_bot_result(
               message.chat.id,
               bot_results.query_id,
               bot_results.results[0].id
           )

           except BotInlineDisabled:
             await message.edit(f"**Bot {g}  inline is disabled turn it on!**")
             return
           except BaseException as a:
             logging.error(a)
             await  message.edit(f"**ERROR** - `{a}`\n\n**Occured while  opening help menu try doing** __{g} Help Menu__\n\n**if help not appears contact @lightning_support_grup**")
    

@light.on(["details"])
async def detail(client, message):
  
    count = 0
    try:

     txt = message.text
    except IndexError as e:
      await message.edit(e)
    if " " in  txt:
      text = message.text.split()[1]
    try:
         string = ""
         o = str(COMMAND_HELP[f"{text}s' help"])
         await message.edit(f"{o}")
    except KeyError:
      await message.edit("**ERROR** - `No deatils found`")


COMMAND_HELP.update({
  "help": f"`{HNDLR}help (command) or {HNDLR}help`\
  \n{HNDLR}deatils ( plugin name )",
  "help's help": f"**USE**: __{HNDLR}help (command) gets the detailed help without triggering help menu and {HNDLR}help triggers help menu__\
  \n\n`{HNDLR}details (plugin name)` __it will get details without triggering help menu__.**"
})