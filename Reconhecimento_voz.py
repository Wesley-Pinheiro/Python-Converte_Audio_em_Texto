#pinheirocfc@gmail.com
#Orientacoes em: https://youtu.be/vjXsa0I_dtc

#Essenciais
#pip install SpeechRecognition

#Extras
#pip install pipwin
#pipwin install pyaudio

import speech_recognition as sr

def reconhecer_fala():    
    microfone = sr.Recognizer() #Habilita o microfone
    with sr.Microphone() as source:        
        microfone.adjust_for_ambient_noise(source)#Reducao de ruido disponivel na speech_recognition        
        print("Diga alguma coisa: ")        
        audio = microfone.listen(source) #guarda o audio falado na variavel 'audio', o audio é finalizado nas pausas grandes
        try:
            frase = microfone.recognize_google(audio,language='pt-BR') #audio sera interpretado na lingua portuguesa            
            print("Você disse: " + frase)        
        except:
            print("Não entendi o que você disse!")
        return frase

reconhecer_fala()