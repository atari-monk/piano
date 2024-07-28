import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get and list available voices
voices = engine.getProperty('voices')

# Print details about each voice
for idx, voice in enumerate(voices):
    print(f"Voice {idx}:")
    print(f"  ID: {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Languages: {voice.languages}")
    print(f"  Gender: {voice.gender}")
    print(f"  Age: {voice.age}")
    print()

# Clean up the engine
engine.stop()
