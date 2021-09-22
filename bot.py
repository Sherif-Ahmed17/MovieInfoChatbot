from rivescript import RiveScript

bot = RiveScript(utf8=True)

bot.load_directory("brain")
bot.sort_replies()


def chat(message):
    if message == "":
        return -1, "No message found "
    else:
        responce = bot.reply("user", message)
    if responce:
        return 0, responce
    else:
        return -1, "No responce found"

# while True: 

#     msg = str(input("User: "))
#     reply = str(bot.reply('localuser', msg))
#     if msg == "quit":
#         break
#     else:
#         print("Bot: " + reply)       