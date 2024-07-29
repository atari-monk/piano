import pyttsx3

# Initialize the TTS engine with a more natural voice setting
engine = pyttsx3.init()

# Define the lyrics text
lyrics = """
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Twinkle, twinkle, little star,
How I wonder what you are!

Then the traveler in the dark
Thanks you for your tiny spark;
He could not see which way to go,
If you did not twinkle so.

Twinkle, twinkle, little star,
How I wonder what you are!

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.

Twinkle, twinkle, little star,
How I wonder what you are!
"""

# Adjust the properties for a more natural sound
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 0.2)  # Volume (0.0 to 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index to choose a different voice

# Save the speech to a file
output_file = "C:\\atari-monk\\code\\piano\\audio\\lyrics\\twinkle_twinkle_high_quality.mp3"
engine.save_to_file(lyrics, output_file)

# Run the engine to process the file saving
engine.runAndWait()

output_file
