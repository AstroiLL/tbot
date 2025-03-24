# tBot

A collection of Telegram bots with basic functionality.

## Features

### Main Bot (tBot.py)
- Echo messages back to the user
- SCREAM mode (converts all messages to uppercase)
- Interactive inline buttons menu with navigation
- Command handling with proper logging
- Environment variable configuration

### Echo Bot (tbot-echobot.py)
- Basic echo functionality
- Simple command handling (/start, /help)
- Environment variable configuration
- Proper logging setup

## Prerequisites

- Python 3.12 or higher
- uv package manager (recommended) or pip
- python-telegram-bot library (version 20.7 or higher)
- python-dotenv for environment variable management
- A Telegram bot token (obtained from [@BotFather](https://t.me/botfather))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/tbot.git
cd tbot
```

2. Enter in a virtual environment:
```bash
source .venv/bin/activate

```

3. (if required) Install the required packages using uv (recommended):
```bash
uv pip install -e .
# or manually install dependencies:
uv pip install "python-telegram-bot>=20.7" "python-dotenv>=1.0.0"
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

### Echo Bot (tbot-echobot.py)
```bash
python tbot-echobot.py
```

## Commands

### Main Bot (tBot.py)
- `/scream` - Activates SCREAM mode (all messages will be converted to uppercase)
- `/whisper` - Deactivates SCREAM mode
- `/menu` - Shows an interactive menu with inline buttons

### Echo Bot (tbot-echobot.py)
- `/start` - Sends a greeting message with user mention
- `/help` - Sends a help message
- Any text message will be echoed back

## Bot Behavior

### Main Bot (tBot.py)
- When in normal mode, the bot will copy any messages you send to it
- When in SCREAM mode, the bot will echo your messages in ALL CAPS
- The `/menu` command displays interactive inline buttons that navigate between two menus
- The second menu includes a tutorial button that links to the Telegram Bot API documentation
- All actions are logged to the console

### Echo Bot (tbot-echobot.py)
- Simple echo functionality for text messages
- Basic command handling with start and help commands
- Uses environment variables for configuration
- Proper logging setup with reduced httpx noise
- Greets users with their name when they start the bot

## Project Structure

- `tBot.py` - Main bot with advanced features (scream mode, menus)
- `tbot-echobot.py` - Simple echo bot with basic functionality
- `.env` - Environment variables file (contains your bot token)
- `pyproject.toml` - Project dependencies and metadata
- `.gitignore` - Files to ignore in git repository
- `.python-version` - Python version specification
- `uv.lock` - uv dependency lock file

## Development

This project contains two different bot implementations:
1. `tBot.py` - A more feature-rich implementation with advanced features like scream mode and interactive menus
2. `tbot-echobot.py` - A simpler implementation based on the official python-telegram-bot example

Both bots use:
- Modern async/await syntax
- Environment variables for configuration
- Proper logging setup
- Type hints for better code quality

For larger bots, consider organizing features into separate modules.

## License

This project is open source and available under the MIT License.
