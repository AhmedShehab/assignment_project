import html
import re

def sanitize_name(name):
    """Sanitize the username to prevent HTML, JS, and unwanted characters."""
    # Strip leading/trailing spaces
    name = name.strip()
    
    # Crop the name to max 50 letters
    name = name[:50]

    # Escape any HTML or special characters
    name = html.escape(name)

    # Remove non-alphanumeric characters (allow only letters, numbers, and spaces)
    name = re.sub(r'[^a-zA-Z0-9 ]', '', name)

    return name

def sanitize_message(message):
    """Sanitize the message to prevent HTML, JS, and unwanted characters, and crop to 1024 chars."""

    # Strip leading/trailing spaces
    message = message.strip()
    # Crop the message to 1024 characters
    message = message[:1024]
    
    # Remove any HTML tags (e.g., <b>, <script>, etc.)
    message = html.escape(message)
    
    return message