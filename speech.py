import speech_recognition as sr
from gtts import gTTS
import os

# Updated Language options
LANGUAGES = {
    "1": ("English", "en"),
    "2": ("Telugu", "te"),
    "3": ("Tamil", "ta"),
    "4": ("Kannada", "kn")
}

def display_language_menu():
    print("\nSelect a Language:")
    for key, (name, _) in LANGUAGES.items():
        print(f"{key}. {name}")
    choice = input("Enter the number for your language: ")
    return LANGUAGES.get(choice, ("English", "en"))  # Default to English

def text_to_speech(language):
    text = input("\nEnter the text you want to convert to speech: ")
    try:
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")
        print("Playing the converted speech...")
        os.system("start output.mp3" if os.name == "nt" else "mpg123 output.mp3")
    except Exception as e:
        print("Error:", e)

def speech_to_text(language):
    recognizer = sr.Recognizer()
    print("\nListening... Speak now!")
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=10)  # Increased timeout
            print("Processing...")
            text = recognizer.recognize_google(audio, language=language)
            print(f"Recognized Text ({language}): {text}")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print("Error:", e)

def main():
    while True:
        print("\nChoose an Option:")
        print("1. Text-to-Speech")
        print("2. Speech-to-Text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            _, lang_code = display_language_menu()
            text_to_speech(lang_code)
        elif choice == '2':
            _, lang_code = display_language_menu()
            speech_to_text(lang_code)
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
