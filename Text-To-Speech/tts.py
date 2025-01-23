import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 200)  # Speed of speech (higher is faster)
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
text = "Hello, My name is Deep How are you? this is your text to speech program."
speak(text)
