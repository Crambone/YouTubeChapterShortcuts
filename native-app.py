import sys
import json
import struct
from pynput import keyboard

# Load the configuration from config.json
def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Log the error to stderr and send an error message to the browser
        error_message = f"Error loading config: {e}"
        send_message({"error": error_message})
        return None  # Continue running the script even if the config fails

# Function to send a message to the native app
def send_message(message):
    encoded_message = json.dumps(message).encode('utf-8')
    sys.stdout.buffer.write(struct.pack('@I', len(encoded_message)))
    sys.stdout.buffer.write(encoded_message)
    sys.stdout.flush()

# Handlers for the shortcuts
def on_activate_control_period():
    send_message({"moveTo": "nextChapter"})

def on_activate_control_comma():
    send_message({"moveTo": "prevChapter"})

def on_activate_control_semicolon():
    send_message({"action": "switchTargetTab"})

# Load the shortcut keys from the config file
config = load_config()
if config is None:
    config = {"nextChapter": "<ctrl>+.", "prevChapter": "<ctrl>+,", "switchTargetTab": "<ctrl>+;"}  # Use defaults if config fails

# Assign shortcuts dynamically from config
hotkeys = {
    config.get("nextChapter", "<ctrl>+."): on_activate_control_period,
    config.get("prevChapter", "<ctrl>+,"): on_activate_control_comma,
    config.get("switchTargetTab", "<ctrl>+;"): on_activate_control_semicolon,
}

# Use pynput's GlobalHotKeys with the loaded hotkeys
with keyboard.GlobalHotKeys(hotkeys) as h:
    h.join()
