import telegram.ext
import os
from telegram.ext import Updater, CommandHandler, MessageHandler

# Getting Bot Token From Secrets
BOT_TOKEN = os.environ.get('6150441649:AAGQvImaxli2cYX2P4bAHlcunClglbWio4U')

# Creating Updater object
updater = Updater(BOT_TOKEN)
updater
dispatcher = updater.dispatcher

def start(update, context):
  context.bot.send_message(
    chat_id=update.effective_chat.id,
    text="Welcome to online writing account activation61 helpline")


def help(update, context):
  text = """Commands:
/start -> Welcome to online writing account activation61 helpline
/help -> This particular message
/content -> Online Writing Activation61 is an international platform with a team of experts
/aboutus -> Online Writing Account Activation is a team of experts
/accounts -> We have a variety of various accounts
/payments -> For any transactions
/updates -> We always keep our clients updated
/challenges -> Some of the challenges our customers face"""
  context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def content(update, context):
  text = "Online Writing Account Activation is a platform meant to help writers who are stranded and don't know what to do, yet they have the capabilities of delivering quality work."
  context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def aboutus(update, context):
  text = "We are a team of experts meant to deliver quality services to our clients. Some of our experts work as customer care in various writing websites, however, we cannot disclose those websites for the security of their jobs."
  context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def accounts(update, context):
  text = "We have a variety of websites for which we offer account verification and activation for our clients. Activation depends on the client's specifications."
  context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def payments(update, context):
  text = "For any transaction to be done, please use the till number 8502742 for security purposes."
  context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def challenges(update, context):
  text = "Here is just an overview of challenges faced by our clients: delayed activation and termination of client accounts. Account termination occurs when clients who have bought an account try to change login and email account details."
  context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def updates(update, context):
  text = """Dear members,
We hope this message finds you well and thank you for being a valued member of our community. We would like to take this opportunity to update you on some exciting developments happening behind the scenes.
At ONLINE WRITING ACTIVATION61, we are dedicated to providing you with the best possible experience on our platform. To achieve this, we are currently working diligently on enhancing our platform to bring you a host of new features and improvements. While these updates are taking some time, we believe they will greatly enhance your overall user experience.
We understand your eagerness to experience these changes firsthand, and we want to assure you that our development team is working tirelessly to make this happen. We are committed to delivering quality services.
We appreciate your patience and support during this time. We will keep you updated on our progress and provide you with a more specific timeline as soon as we have further information. In the meantime, if you have any questions or concerns, please don't hesitate to reach out to our support team.
Thank you once again for choosing ONLINE WRITING ACTIVATION61. We look forward to sharing our exciting updates with you soon!
Best regards,
Secretary Online writing activation61"""
  context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def handle_message(update, context):
  context.bot.send_message(
    chat_id=update.effective_chat.id,
    text=
    "Sorry, I didn't understand that command. Type /help to see the available commands."
  )


# Registering handlers
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
content_handler = CommandHandler('content', content)
aboutus_handler = CommandHandler('aboutus', aboutus)
accounts_handler = CommandHandler('accounts', accounts)
payments_handler = CommandHandler('payments', payments)
challenges_handler = CommandHandler('challenges', challenges)
updates_handler = CommandHandler('updates', updates)
message_handler = MessageHandler(Filters.text, handle_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(content_handler)
dispatcher.add_handler(aboutus_handler)
dispatcher.add_handler(accounts_handler)
dispatcher.add_handler(payments_handler)
dispatcher.add_handler(challenges_handler)
dispatcher.add_handler(updates_handler)
dispatcher.add_handler(message_handler)

print("Bot Started And Waiting For New Messages\n")

# Start the bot
updater.start_polling()
updater.idle()
