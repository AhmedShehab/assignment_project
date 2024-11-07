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
