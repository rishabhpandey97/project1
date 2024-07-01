import openai
import pyttsx3
import speech_recognition as sr


# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key


while True:
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    try:
    # Recognize the speech
        SpeechText = recognizer.recognize_google(audio)
        print(f"You said: {SpeechText}")
        if(SpeechText == "close"):
            exit()
    # Your prompt/question to ChatGPT
        prompt = SpeechText

    # Send the prompt to ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine for your task
            prompt=prompt,
            max_tokens=3000  # You can adjust thze max tokens for response length
        )

    # Extract and print the response text
        text = response.choices[0].text
        print("Ai Voice Assistant Response - ",text)
    # Initialize the TTS engine
       
        voice = engine.getProperty('voices') 
        engine.setProperty('voice', voice[1].id) 

    # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Convert and play the text
        engine.say(text)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
