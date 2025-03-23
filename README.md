# Telegram Tutorial Bot

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
2. Install the required packages:

```bash
pip install python-telegram-bot==13.13 urllib3 six
```

## Setup

1. Create a new bot using [@BotFather](https://t.me/botfather) on Telegram
2. Get your bot token
3. Open the `TutorialBot.py` file and replace `"YOUR_BOT_TOKEN"` with your actual bot token

## Running the Bot

```bash
python TutorialBot.py
```

## Commands

- `/scream` - Activates SCREAM mode (all messages will be converted to uppercase)
- `/whisper` - Deactivates SCREAM mode
- `/menu` - Shows an interactive menu with inline buttons

## Notes for Python 3.13+ Users

If you're running Python 3.13 or newer, you might encounter an issue with the `imghdr` module which was removed from the standard library. The workaround provided in this repository (the custom `imghdr.py` file) addresses this issue.

## License

This project is open source and available under the MIT License.
