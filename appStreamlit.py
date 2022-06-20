import streamlit as st
from gtts import gTTS
def text2Speech(data):
    my_text = data
    tts = gTTS(text=my_text, lang='en', slow=False)
    tts.save('converted-file.mp3')  # save file as ... (here saving as mp3)
    audio_file = open("converted-file.mp3", 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
st.title("Text to Speech converter")
textcontent= st.text_input('Write Text here to convert it into speech:')
if(st.button('Submit')):
    result = textcontent.title()
    st.success(result)
    text2Speech(textcontent)