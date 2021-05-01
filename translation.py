import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hai {}!!</b>
<i>මම Auto Forword Bot🥳🥳
මෙම බොට් සියළුම ලිපිගොනු එක් පොදු නාලිකාවක් වෙත ඔබේ පුද්ගලික නාලිකාව වෙත යොමු කරයි
වැඩිපුර විස්තර /help</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>• Then use /run command in your bot</b>

<b><u>Available Command</b></u>

* /start - <b>Bot ආරම්භය</b>
* /help - <b>වෙනත් උදවු</b>
* /run - <b>start forward</b>
* /about - <b>මම ගැන</b>"""
  ABOUT_TXT = """<b><u>මම ගැන</b></u>

<b>Name :</b> <code>Auto Forward Bot🥳</code>
<b>Credit :</b> <code>@SL_PUNSITH1</code>
<b>Language :</b> <code>Python3</code>
<b>Lybrary :</b> <code>Pyrogram v1.2.9</code>
<b>Contry :</b> <code>Sri Lanka🥳</code>
<b>Build :</b><code>V4.4.4.1</code>"""
