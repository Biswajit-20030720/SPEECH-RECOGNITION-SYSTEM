import speech_recognition as sr  # Import the speech recognition library

# Step 1: Create a recognizer object that will handle the audio input
recognizer = sr.Recognizer()

# Step 2: Load your audio file (must be in .wav format for best results)
with sr.AudioFile("sample_audio.wav") as source:
    print("🔊 Listening to the audio file...")
    audio = recognizer.record(source)  # Read the entire audio file into memory

# Step 3: Use Google's free online speech recognition to convert speech to text
try:
    text = recognizer.recognize_google(audio)
    print("✅ Transcription complete:")
    print(f"📝 {text}")
except sr.UnknownValueError:
    print("❌ Sorry, I couldn’t understand what was said in the audio.")
except sr.RequestError as e:
    print(f"⚠️ Could not connect to the Google service. Error: {e}")
