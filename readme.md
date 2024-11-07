This is a simple real-time chat application built with Django Channels and WebSockets.

## Requirements

To run this project, you need to have Python 3.x and Django installed. The dependencies for this project are listed in the `requirements.txt` file.

### Installing Dependencies

1. **Clone the repository**:

    clone the project to your local environment

    ```bash
    cd assignment_project
    ```

2. **Create a virtual environment**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment**:

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:
        ```bash
        venv\\Scripts\\activate
        ```

4. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

## Setting Up the Database and Running Migrations

Before you start the server, you need to apply the database migrations.

1. **Run migrations**:

    ```bash
    python manage.py migrate
    ```

    This will create the necessary database tables for your application.

## Running the Server

To start the development server, run the following command:

```bash
python manage.py runserver
```

## How to use the Chat

Once the django server is running you can use the chat feature by opening the following url

```bash
http://localhost:8000/chat/
```

Enter your name when prompted and it should be working

## How it's implemented

The chat feature is implemented using Django Channels for handling WebSockets. Django Channels allows Django to handle real-time communication, which is essential for building chat applications. The WebSocket connection is established between the client and server, enabling real-time message exchange.

-   **WebSocket Consumer**: A custom `MessageConsumer` is created to handle WebSocket connections, manage messages, and broadcast them to all connected clients.
-   **In-memory connection tracking**: Active connections are tracked in memory to broadcast messages to all users.
-   **Message Persistence**: All messages are saved in the database using Django’s ORM for later retrieval.
-   **Real-time Broadcasting**: When a user sends a message, the message is saved and broadcasted to all connected users via WebSockets.
-   **Database Used**: A simple sqlite3.db database for this specific case it's just a local simple app no need for complications

This approach provides a simple efficient solution for real-time messaging

## What I Planned to Do but Couldn't Complete

Initially, I planned to implement a simple terminal-based client where users could input their name and message, and also receive messages from other users. The idea was to use a `client.py` file that could connect to the WebSocket server and facilitate communication. Although the WebSocket functionality worked perfectly during debugging, and messages were successfully broadcasted to all active connections, I faced a challenge in getting the client to display the broadcasted messages.

Due to this issue, I decided to switch to a web-based interface and used an HTML template with a simple UI, allowing users to interact with the chat in a more user-friendly way. The WebSocket communication remains the same, but now, messages are displayed on the web page instead of the terminal.

This approach provides a more intuitive experience for users and ensures that all messages are visible in real-time via the browser interface.

## Ideas for Future Improvements

-   **User Authentication**: Use a Django `User` model with authentication to replace the simple username input. This would allow users to sign in and chat under their authenticated account, making it more secure and personalized.

-   **Message Timestamps**: Show message timestamps so users can see when each message was sent.

-   **Chat Rooms**: Allow users to create and join specific chat rooms based on topics or interests.

-   **Typing Indicators**: Display a "typing..." indicator when someone is typing a message, improving the user experience and making the chat feel more interactive.

-   **User Presence**: Track and display which users are currently online, letting others know who is available for chatting.

-   **Message History**: Implement a simple message history feature where users can see past messages when they join the chat, instead of only receiving new messages.

-   **Emojis and Rich Text**: Allow users to send emojis or even formatted text (bold, italics, etc.) to make the chat more expressive.

-   **File Sharing**: Add the ability for users to share files or images within the chat.

-   **Admin Features**: Provide administrative features to mute, kick, or ban users if necessary to maintain a safe environment.
