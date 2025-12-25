import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Comprehensive Knowledge Base for Math and Science
KNOWLEDGE_BASE = {
    'math': '''
📝 **MATHEMATICS GUIDE** 📝

**ALGEBRA:**
- Linear Equations: ax + b = c
- Quadratic Formula: x = (-b ± √(b²-4ac)) / 2a
- Systems of equations can be solved by substitution or elimination

**GEOMETRY:**
- Circle Area: πr²
- Triangle Area: (base × height) / 2
- Pythagorean Theorem: a² + b² = c²
- Volume of sphere: (4/3)πr³

**CALCULUS:**
- Derivative measures rate of change
- Integral is the reverse of derivative
- Limit: approaching a value as x approaches a point

**STATISTICS:**
- Mean: sum of all values / count
- Median: middle value when sorted
- Mode: most frequently occurring value
- Standard deviation: measure of spread
    ''',
    
    'science': '''
🔬 **SCIENCE GUIDE** 🔬

**PHYSICS:**
- Force = Mass × Acceleration (F=ma)
- Energy: Kinetic (½mv²) and Potential (mgh)
- Newton's Laws of Motion
- Speed = Distance / Time

**CHEMISTRY:**
- Periodic Table: organizes elements by atomic number
- pH Scale: 0-14, 7 is neutral
- Chemical Bonds: Ionic, Covalent, Metallic
- Electron Configuration: how electrons arrange around nucleus
- Molar Mass: sum of atomic masses

**BIOLOGY:**
- Cell Structure: Nucleus, Mitochondria, Ribosomes, Membrane
- Photosynthesis: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂
- DNA Structure: Double helix
- Respiration: Breaking down glucose for energy
    '''
}

# Detailed Quiz Questions with Answers
QUIZ_DATA = {
    # Math Questions
    'math_q1': {
        'q': '❓ What is 2² + 3² = ?',
        'options': ['a) 10', 'b) 13', 'c) 12'],
        'answer': 'b',
        'explanation': '2² = 4, 3² = 9, so 4 + 9 = 13 ✅'
    },
    'math_q2': {
        'q': '❓ Solve: 3x + 5 = 20',
        'options': ['a) 3', 'b) 5', 'c) 15'],
        'answer': 'b',
        'explanation': '3x = 20 - 5 = 15, x = 15/3 = 5 ✅'
    },
    'math_q3': {
        'q': '❓ What is the area of a circle with radius 5?',
        'options': ['a) 25π', 'b) 10π', 'c) 5π'],
        'answer': 'a',
        'explanation': 'Area = πr² = π(5)² = 25π ✅'
    },
    'math_q4': {
        'q': '❓ Find the hypotenuse if a=3, b=4',
        'options': ['a) 5', 'b) 6', 'c) 7'],
        'answer': 'a',
        'explanation': 'Using Pythagorean theorem: c² = 3² + 4² = 9 + 16 = 25, c = 5 ✅'
    },
    
    # Science Questions
    'science_q1': {
        'q': '❓ What is H₂O?',
        'options': ['a) Carbon dioxide', 'b) Water', 'c) Oxygen'],
        'answer': 'b',
        'explanation': 'H₂O is the chemical formula for water - essential for life! 💧'
    },
    'science_q2': {
        'q': '❓ What is F = ma?',
        'options': ['a) Energy', 'b) Newton\'s 2nd Law', 'c) Velocity'],
        'answer': 'b',
        'explanation': 'F = ma is Newton\'s Second Law of Motion 🚀'
    },
    'science_q3': {
        'q': '❓ What does DNA stand for?',
        'options': ['a) Digital Network', 'b) Deoxyribonucleic Acid', 'c) Data'],
        'answer': 'b',
        'explanation': 'DNA is Deoxyribonucleic Acid - the molecule of life 🧬'
    },
    'science_q4': {
        'q': '❓ What is the pH of water?',
        'options': ['a) 5', 'b) 7', 'c) 9'],
        'answer': 'b',
        'explanation': 'Pure water has a pH of 7 (neutral) 🧪'
    },
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when /start is issued."""
    welcome_text = (
        "🎓 **WELCOME TO EDUCATIONAL BOT!** 🎓\n\n"
        "I am here to help you learn Mathematics and Science!\n\n"
        "**Available Commands:**\n"
        "/help - Show all commands\n"
        "/math - Learn Mathematics\n"
        "/science - Learn Science\n"
        "/quiz_math - Take Math Quiz\n"
        "/quiz_science - Take Science Quiz\n"
        "/ask - Ask a question\n\n"
        "What would you like to learn? 🚀"
    )
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help message."""
    help_text = (
        "📚 **AVAILABLE COMMANDS:**\n\n"
        "/start - Start the bot\n"
        "/help - Show this message\n"
        "/math - Learn Mathematics topics\n"
        "/science - Learn Science topics\n"
        "/quiz_math - Test your Math knowledge\n"
        "/quiz_science - Test your Science knowledge\n"
        "/ask [topic] - Ask about a topic\n"
        "/explain - Explain a concept\n\n"
        "Just type a question or topic name! 💡"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def math_guide(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send mathematics guide."""
    await update.message.reply_text(KNOWLEDGE_BASE['math'], parse_mode='Markdown')

async def science_guide(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send science guide."""
    await update.message.reply_text(KNOWLEDGE_BASE['science'], parse_mode='Markdown')

async def math_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a math quiz."""
    quiz_text = "🎯 **MATH QUIZ** 🎯\n\n"
    quiz_text += "📝 Here are your questions:\n\n"
    
    math_questions = ['math_q1', 'math_q2', 'math_q3', 'math_q4']
    for i, q_id in enumerate(math_questions, 1):
        q = QUIZ_DATA[q_id]
        quiz_text += f"{i}. {q['q']}\n"
        for opt in q['options']:
            quiz_text += f"   {opt}\n"
        quiz_text += "\n"
    
    quiz_text += "📌 Reply with your answers (e.g., 'b, a, c, b')\n"
    await update.message.reply_text(quiz_text, parse_mode='Markdown')

async def science_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a science quiz."""
    quiz_text = "🔬 **SCIENCE QUIZ** 🔬\n\n"
    quiz_text += "📝 Here are your questions:\n\n"
    
    science_questions = ['science_q1', 'science_q2', 'science_q3', 'science_q4']
    for i, q_id in enumerate(science_questions, 1):
        q = QUIZ_DATA[q_id]
        quiz_text += f"{i}. {q['q']}\n"
        for opt in q['options']:
            quiz_text += f"   {opt}\n"
        quiz_text += "\n"
    
    quiz_text += "📌 Reply with your answers (e.g., 'b, b, b, b')\n"
    await update.message.reply_text(quiz_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages and provide intelligent responses."""
    text = update.message.text.lower()
    response = ""
    
    # Check for specific topics
    if 'algebra' in text or 'equation' in text:
        response = "🔢 **ALGEBRA HELP**\nAlgebra deals with equations and variables.\nExample: 2x + 5 = 13 → x = 4\n\nTry /math for more!"
    elif 'geometry' in text or 'area' in text or 'circle' in text:
        response = "📐 **GEOMETRY HELP**\n- Circle Area: πr²\n- Triangle Area: (base × height)/2\n- Pythagorean: a² + b² = c²\n\nTry /math for more!"
    elif 'physics' in text or 'force' in text:
        response = "⚡ **PHYSICS HELP**\nF = ma (Force = Mass × Acceleration)\nEnergy: Kinetic & Potential\n\nTry /science for more!"
    elif 'chemistry' in text or 'ph' in text or 'element' in text:
        response = "🧪 **CHEMISTRY HELP**\nPH Scale: 0-14 (7 is neutral)\nPeriodic Table organizes elements\nChemical Bonds: Ionic, Covalent\n\nTry /science for more!"
    elif 'biology' in text or 'cell' in text or 'dna' in text:
        response = "🧬 **BIOLOGY HELP**\nDNA: Double helix structure\nPhotosynthesis: CO₂ + H₂O → Glucose\nCell parts: Nucleus, Mitochondria\n\nTry /science for more!"
    elif 'calculus' in text or 'derivative' in text:
        response = "📈 **CALCULUS HELP**\nDerivative = Rate of Change\nIntegral = Area under curve\nLimits approach specific values\n\nTry /math for more!"
    elif '?' in text:
        response = (
            "❓ **I can help with:**\n"
            "- Mathematics (Algebra, Geometry, Calculus, Statistics)\n"
            "- Science (Physics, Chemistry, Biology)\n\n"
            "Try typing:\n"
            "/math - Learn math\n"
            "/science - Learn science\n"
            "/quiz_math - Math quiz\n"
            "/quiz_science - Science quiz"
        )
    else:
        response = (
            "👋 Hello! I'm an educational bot.\n\n"
            "I can help you with:"
            "\n📚 Mathematics\n"
            "🔬 Science\n\n"
            "Use /help for all commands!"
        )
    
    await update.message.reply_text(response, parse_mode='Markdown')

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a message."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main() -> None:
    """Start the bot."""
    # YOU MUST REPLACE 'YOUR_BOT_TOKEN' WITH YOUR ACTUAL BOT TOKEN FROM @BotFather
    BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN')
    
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("math", math_guide))
    application.add_handler(CommandHandler("science", science_guide))
    application.add_handler(CommandHandler("quiz_math", math_quiz))
    application.add_handler(CommandHandler("quiz_science", science_quiz))
    
    # Add message handler for general messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
