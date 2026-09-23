# Jarvis - Personal Voice Assistant

Jarvis is a Python-based personal voice assistant that processes spoken commands and provides automated responses and actions. The project combines speech recognition, text-to-speech conversion, command handling, and Python automation to demonstrate the development of an interactive voice-controlled application.

## About the Project

The main purpose of this project is to practice Python programming concepts by building an interactive voice-controlled application. The program demonstrates speech recognition, text-to-speech conversion, command processing, API integration, music playback, and basic Python automation.

## How the Project Works

1. The assistant starts and listens for the user's voice command.
2. Speech recognition converts the spoken command into text.
3. The program processes the command using Python.
4. Based on the command, Jarvis performs the appropriate action or generates a response.
5. The response can be converted into speech using text-to-speech technology.
6. The assistant continues listening for additional commands.

## Features

- Voice-based command input
- Speech recognition
- Text-to-speech responses
- Automated command handling
- Music playback
- Python-based task automation
- Interactive voice-controlled operation
- AI-powered response processing

## Technologies Used

- Python
- Speech Recognition
- Text-to-Speech
- Pygame
- OpenAI API
- Python automation
- Environment variables

## How to Run

Clone the repository:

    git clone https://github.com/anushka-bhamare/jarvis-python.git

Navigate to the project directory:

    cd jarvis-python

Create a virtual environment:

    python -m venv .venv

Activate the virtual environment on Windows:

    .venv\Scripts\activate

Install the required dependencies according to the packages used in the project.

Run the program:

    python main.py

Make sure your microphone is connected and working before starting the application.

## API Configuration

The project uses an environment variable for the OpenAI API key.

Create a `.env` file locally and add:

    OPENAI_API_KEY=your_api_key_here

Never upload the `.env` file or API key to GitHub.

Make sure `.env` is included in `.gitignore`.

## Project Structure

    jarvis-python/
    │
    ├── main.py
    ├── client.py
    ├── musiclibrary.py
    ├── .gitignore
    └── README.md

## Learning Outcomes

Through this project, I practiced and strengthened my understanding of:

- Python functions and modules
- Speech recognition
- Text-to-speech conversion
- Voice command processing
- Working with external Python libraries
- API integration
- Environment variable usage
- Music and file handling
- Basic Python automation
- Git and GitHub project management

## Future Improvements

Possible improvements for the project include:

- Adding more voice commands
- Improving natural language understanding
- Adding additional automation features
- Adding a graphical user interface
- Improving error handling
- Adding more system controls
- Integrating additional APIs and services

## Conclusion

Jarvis is a Python-based personal voice assistant project that demonstrates how different Python concepts, libraries, APIs, and automation techniques can be combined to create an interactive voice-controlled application.

This project helped me gain practical experience with speech recognition, text-to-speech conversion, API integration, Python automation, and GitHub project management.

## Author

Anushka Bhamare
