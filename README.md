# tBot

A collection of Telegram bots with basic functionality.

## Features

### Main Bot (tBot.py)
- Echo messages back to the user
- SCREAM mode (converts all messages to uppercase)
- Interactive inline buttons menu
- Simple command handling

### Simple Bot (tbot-get.py)
- Basic echo functionality
- Simple command handling
- Environment variable configuration

## Prerequisites

- Python 3.10 or higher
- python-telegram-bot library (version 13.7)
- python-dotenv for environment variable management
- A Telegram bot token (obtained from [@BotFather](https://t.me/botfather))

## Installation

1. Ensure you have Python 3.10+ installed on your system
2. Clone this repository:
```bash
git clone https://github.com/yourusername/tbot.git
cd tbot
```

3. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate.bat  # On Windows
```

4. Install the required packages:
```bash
pip install -e .
# or manually install dependencies:
pip install python-telegram-bot==13.7 python-dotenv
```

## Configuration

1. Create a new bot using [@BotFather](https://t.me/botfather) on Telegram
2. Get your bot token
3. Set up your environment variables by creating/editing the `.env` file:
```
TELEGRAM_BOT_TOKEN=your_token_here
```

## Running the Bots

### Main Bot (tBot.py)
```bash
python tBot.py
```

### Simple Bot (tbot-get.py)
```bash
python tbot-get.py
```

## Commands

### Main Bot (tBot.py)
- `/scream` - Activates SCREAM mode (all messages will be converted to uppercase)
- `/whisper` - Deactivates SCREAM mode
- `/menu` - Shows an interactive menu with inline buttons

### Simple Bot (tbot-get.py)
- `/start` - Sends a greeting message
- Any text message will be echoed back

## Bot Behavior

### Main Bot (tBot.py)
- When in normal mode, the bot will copy any messages you send to it
- When in SCREAM mode, the bot will echo your messages in ALL CAPS
- The `/menu` command displays interactive inline buttons that navigate between two menus
- The second menu includes a tutorial button that links to the Telegram Bot API documentation

### Simple Bot (tbot-get.py)
- Simple echo functionality for text messages
- Basic command handling with a start command
- Uses environment variables for configuration

## Project Structure

- `tBot.py` - Main bot with advanced features
- `tbot-get.py` - Simple bot with basic functionality
- `.env` - Environment variables file (contains your bot token)
- `pyproject.toml` - Project dependencies and metadata
- `.gitignore` - Files to ignore in git repository
- `.python-version` - Python version specification

## Development

This project contains two different bot implementations:
1. `tBot.py` - A more feature-rich implementation with advanced features
2. `tbot-get.py` - A simpler implementation for basic bot functionality

For larger bots, consider organizing features into separate modules.

## License

This project is open source and available under the MIT License.
