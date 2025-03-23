# tBot

A simple tutorial bot for Telegram that demonstrates basic functionality.

## Features

- Echo messages back to the user
- SCREAM mode (converts all messages to uppercase)
- Interactive inline buttons menu
- Simple command handling

## Prerequisites

- Python 3.10
- python-telegram-bot library (version 13.7)
- A Telegram bot token (obtained from [@BotFather](https://t.me/botfather))

## Installation

1. Ensure you have Python installed on your system
2. Create a virtual environment:

```bash
python -m venv new_venv
source new_venv/bin/activate  # On Linux/Mac
# or
new_venv\Scripts\activate.bat  # On Windows
```

3. Install the required packages:

```bash
pip install python-telegram-bot==13.7
```

## Setup

1. Create a new bot using [@BotFather](https://t.me/botfather) on Telegram
2. Get your bot token
3. Open the `TutorialBot.py` file and replace `"<YOUR_BOT_TOKEN>"` with your actual bot token

## Running the Bot

```bash
python tBot.py
```

## Commands

- `/scream` - Activates SCREAM mode (all messages will be converted to uppercase)
- `/whisper` - Deactivates SCREAM mode
- `/menu` - Shows an interactive menu with inline buttons

## Bot Behavior

- When in normal mode, the bot will copy any messages you send to it
- When in SCREAM mode, the bot will echo your messages in ALL CAPS
- The `/menu` command displays interactive inline buttons that navigate between two menus

## License

This project is open source and available under the MIT License.
