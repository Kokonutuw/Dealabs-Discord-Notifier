# Dealabs-Discord-Notifier

This Discord bot monitors Dealabs offers and automatically shares them in your Discord server.

## Features

- Continuous monitoring of Dealabs offers
- Automatic notifications on Discord
- No duplicates thanks to offer memory
- Updates every 60 seconds

## Configuration

1. Copy the [deal.py](cci:7://file:///c:/Users/maxim/Desktop/Bot%20discord/deal.py:0:0-0:0) file to your project
2. Edit the file to configure:
   - `rss_url`: Dealabs RSS feed URL
   - `webhook_url`: Your Discord webhook URL

## Requirements

- Python 3.x
- Required libraries:
  - requests
  - xml.etree.ElementTree

## Installation

1. Install dependencies:
```bash
pip install requests
