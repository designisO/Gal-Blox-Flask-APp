import speech_recognition as sr 
import pyttsx3
import psycopg2
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

# connection to db for signups
def get_db_connection():
    conn = psycopg2.connect(database="galblox", # the database in which I created in psql
                        host="postgres",
                        password="#",
                        port="5432")
    return conn


@app.route("/")
def home():
conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO gbemails (id, first_name, last_name, email)'
                    'VALUES (%s, %s, %s, %s)',
                    (id, first_name, last_name, email))
    members = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('base.html')
 

'''  
# GLBX AI code:
 
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Welcome to Gal-Blox')
engine.say('How may I help you today!')
engine.say('Say the word Token Price and see what happens.')
engine.runAndWait()

while True:

    try:
        # recording from mic and recording
        with sr.Microphone() as source:
        
            # ambient microphone setting
            listener.adjust_for_ambient_noice(mic, duration=0.5)
                
            # Infoming user that GLBX AI is listening.
            print('GLBX AI is Listening....')
            voice = listener.listen(source)
            # functions for voice to text
            command = listener.recognize_google(voice)
            command = listener.recongize_google(audio)
                
            # dictate if GLBX AI is there or not.
            # This will allow it to be called only when saying GLBX AI
            command = command.lower()
            if 'Token Price' in command:
                    print(command)
                    commandTwo = input("Type in the command if neeeded: ")
                    print(commandTwo)
    except:
        break

'''    
if __name__ == "__main__":
    app.run(debug=True)
    
