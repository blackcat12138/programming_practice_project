import win32com.client

speaker = win32com.client.Dispatch("SAPT.SpVoice")
speaker.Speak("How are you?")
