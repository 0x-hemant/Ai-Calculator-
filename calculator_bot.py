import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the button layout for the calculator
button_list = [
    [InlineKeyboardButton("Addition (+)", callback_data='add'),
     InlineKeyboardButton("Subtraction (-)", callback_data='subtract')],
    [InlineKeyboardButton("Division (/)", callback_data='divide')]
]
reply_markup = InlineKeyboardMarkup(button_list)

# Define the functions to handle each calculation
def addition(update: Update, context: CallbackContext) -> None:
    result = int(context.args[0]) + int(context.args[1])
    update.message.reply_text(f"The result is {result}")

def subtraction(update: Update, context: CallbackContext) -> None:
    result = int(context.args[0]) - int(context.args[1])
    update.message.reply_text(f"The result is {result}")

def division(update: Update, context: CallbackContext) -> None:
    result = int(context.args[0]) / int(context.args[1])
    update.message.reply_text(f"The result is {result}")

# Define the function to handle inline button presses
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == 'add':
        query.answer()
        query.edit_message_text(text="Enter the two numbers you want to add, separated by a space:")
        context.user_data['operation'] = 'add'
    elif query.data == 'subtract':
        query.answer()
        query.edit_message_text(text="Enter the two numbers you want to subtract, separated by a space:")
        context.user_data['operation'] = 'subtract'
    elif query.data == 'divide':
        query.answer()
        query.edit_message_text(text="Enter the two numbers you want to divide, separated by a space:")
        context.user_data['operation'] = 'divide'

# Define the main function to start the bot
def main() -> None:
    # Create the Updater and pass in the bot token
    updater = Updater("6084266554:AAHAEXQAQBcA8-xr4vtNnVTDuRLOseI8u4U", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add the command handler for each operation
    dispatcher.add_handler(CommandHandler("add", addition))
    dispatcher.add_handler(CommandHandler("subtract", subtraction))
    dispatcher.add_handler(CommandHandler("divide", division))

    # Add the callback query handler for the inline buttons
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process is stopped
    updater.idle()

if __name__ == '__main__':
    main()
   