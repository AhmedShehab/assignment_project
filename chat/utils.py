def crop_message(message):
    """
    Crop the message to a maximum of 1024 characters.

    Args:
    - message (str): The message to be cropped.

    Returns:
    - str: The cropped message if it exceeds 1024 characters, otherwise the original message.
    """
    if len(message) > 1024:
        return message[:1024]  # Crop the message to the first 1024 characters
    return message