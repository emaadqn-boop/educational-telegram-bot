import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Knowledge base for the bot
KNOWLEDGE_BASE = {
    'math': 'Math Topics: Algebra, Geometry, Calculus, Statistics',
    'science': 'Science Topics: Physics, Chemistry, Biology',
    'english': 'English: Grammar, Literature, Writing Skills',
    'history': 'History: Ancient, Medieval, Modern History'
}

QUIZ_DATA = {
    'math_q1': {'q': 'What is 2+2?', 'a': '4'},
    'math_q2': {'q': 'What is 5*5?', 'a': '25'},
    'science_q1': {'q': 'What is H2O?', 'a': 'Water'}
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /start is issued."""
    welcome_text = (
        "Welcome to Educational Bot! 🎓\n\n"
        "Commands:\n"
        "/help - Show all commands\n"
        "/topics - Show available topics\n"
        "/quiz - Start a quiz\n"
        "/ask - Ask a question\n"
    )
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /help is issued."""
    help_text = (
        "Available Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this message\n"
        "/topics - List all topics\n"
        "/quiz - Take a quiz\n"
        "/ask [subject] - Get info on a subject\n"
    )
    await update.message.reply_text(help_text)

async def topics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show available topics."""
    topics_text = "Available Topics:\n"
    for topic in KNOWLEDGE_BASE.keys():
        topics_text += f"\n- {topic.upper()}\n  {KNOWLEDGE_BASE[topic]}"
    await update.message.reply_text(topics_text)

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a quiz."""
    quiz_text = "Quiz: Answer these questions!\n\n"
    for quiz_id, quiz_item in QUIZ_DATA.items():
        quiz_text += f"{quiz_id}: {quiz_item['q']}\n"
    await update.message.reply_text(quiz_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages."""
    text = update.message.text.lower()
    
    # Check for topic requests
    for topic in KNOWLEDGE_BASE.keys():
        if topic in text:
            await update.message.reply_text(f"Topic: {KNOWLEDGE_BASE[topic]}")
            return
    
    # Default response
    default_response = (
        "I didn't understand that. Try:\n"
        "/topics - See available topics\n"
        "/quiz - Take a quiz\n"
        "/help - Show all commands"
    )
    await update.message.reply_text(default_response)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token("YOUR_BOT_TOKEN_HERE").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("topics", topics))
    application.add_handler(CommandHandler("quiz", quiz))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # log all errors
    application.add_error_handler(error_handler)

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
