# Educational Telegram Bot 🎓

A simple and fast educational Telegram bot for students with Q&A, quizzes, and learning resources.

## Features

✨ **Available Commands:**
- `/start` - Welcome message and instructions
- `/help` - Show all available commands
- `/topics` - View all educational topics
- `/quiz` - Start a quiz on various subjects
- `/ask [subject]` - Get information about a specific subject

## Topics Covered

📚 **Available Learning Areas:**
- **Math** - Algebra, Geometry, Calculus, Statistics
- **Science** - Physics, Chemistry, Biology
- **English** - Grammar, Literature, Writing Skills
- **History** - Ancient, Medieval, and Modern History

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/emaadqn-boop/educational-telegram-bot.git
   cd educational-telegram-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get your Bot Token from BotFather on Telegram:
   - Open Telegram and search for @BotFather
   - Follow the instructions to create a new bot
   - Copy your bot token

4. Update the bot token in `bot.py`:
   - Replace `"YOUR_BOT_TOKEN_HERE"` with your actual token

5. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

Once the bot is running:

1. Search for your bot in Telegram
2. Send `/start` to begin
3. Use `/help` to see all commands
4. Select topics with `/topics`
5. Try quizzes with `/quiz`

## Example Interactions

**User:** `/topics`
**Bot:** Shows all available learning topics

**User:** `math`
**Bot:** Provides information about math topics

**User:** `/quiz`
**Bot:** Presents quiz questions

## Technologies Used

- Python 3.8+
- python-telegram-bot (v20.3)
- Telegram Bot API

## Contributing

Feel free to fork, modify, and improve this bot. Pull requests are welcome!

## License

MIT License - Feel free to use this project as you wish.

## Support

If you have questions or issues, please create an issue in the GitHub repository.

---

**Happy Learning!** 📖✏️
