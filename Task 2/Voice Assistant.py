import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listens for user input and returns the recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, the service is down.")
            return None

def handle_command(command):
    """Processes the recognized command."""
    if command is None:
        speak("I didn't catch that. Could you repeat, please?")
    elif "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "what's your name" in command:
        speak("I am your personal voice assistant.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm sorry, I don't know how to respond to that.")
    return True

def main():
    """Main function to run the voice assistant."""
    speak("Voice assistant activated. How can I help you?")
    running = True
    while running:
        command = listen()
        running = handle_command(command)

if __name__ == "__main__":
    main()