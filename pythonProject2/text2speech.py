import pyttsx3

voice_converter = pyttsx3.init()

voices = voice_converter.getProperty('voices')
for voice in voices:
    print("Voice:")
    print("Name: %s"%voice.name)
    print("Gender: %s" %voice.gender)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voice_converter.setProperty('voice', voice_id)

voice_converter.say("I'm also a geek")
voice_converter.say('hello geeks for geeks')

voice_converter.runAndWait()
