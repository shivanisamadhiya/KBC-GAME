#  🎯Kaun Banega Crorepati (KBC) Quiz Game
​An immersive, multimedia-rich quiz game built using Python. This application mimics the real-world TV show experience with background music, voice assistance for lifelines, and a progressive difficulty system.

## ​🚀 Key Features
### 1.)​Multimedia Integration:
* Audio: Uses pygame.mixer for background music and sound effects (calling, winning, losing).
##### ​i.)Voice Assistant:
Uses pyttsx3 (Text-to-Speech) for the "Phone-a-Friend" lifeline.
### 2.) ​Three Classic Lifelines:
##### i.)​50:50:
Dynamically hides two incorrect options based on the current question.
##### ii.)​Audience Poll:
Displays ttk.Progressbar widgets to simulate crowd voting.
##### iii.)​Phone-a-Friend:
Triggers a "call" sound and speaks the correct answer using an AI voice.
##### iv.)​Dynamic UI: 
The prize money sidebar (amountLable) updates visually as you progress through 15 levels.
##### v.)​Win/Loss Logic: 
Custom Toplevel windows for game-over scenarios with "Play Again" functionality.

## ​🛠️ Built With
##### i.) ​Python 3.x
##### ​ii.) Tkinter: For the main GUI and layout.
##### iii.) ​Pygame (Mixer): For managing the game's audio environment.
##### ​iv.) Pyttsx3: For offline Text-to-Speech synthesis.
##### ​v.) Standard Libraries: random and time for logic and delays.

## ​📂 Project Structure
​All core logic is contained within the main script for ease of use, supported by local assets:
#### KBC-Project/
│
#### ├── kbc_main.py         
Main Python script containing GUI and Game Logic
#### ├── kbc.mp3             
 Background theme music
#### ├── calling.mp3         
 Calling sound effect for Phone lifeline
#### ├── kbcwon.mp3          
 Victory sound effect
#### ├── questions.json      
 (Optional) Database for questions
#### └── assets/             
Folder for images (50-50.png, center.png, etc.)

## 🎮 How to Play
##### Clone the Repository
##### Install Dependencies
##### Run the Script

## 🧩 Code Logic Highlights
#### 1.) The Lifeline System
The lifelines are programmed to be used only once. For example, the 50:50 logic specifically checks the current question in the questionArea and clears the text of two specific incorrect buttons:


def lifeline50():


   lifeline50Button.config(image=image50x, state=DISABLED)


   
   if questionArea.get(1.0, 'end-1c') == questions[0]:


   
      optionButton1.config(text='')


      
      optionButton4.config(text='')




      

#### 2.) Voice Assistance
The "Phone-a-Friend" lifeline provides an audio-visual experience where the engine "speaks" the answer:


 def phoneclick():



 
   for i in range(15):


   
      if questionArea.get(1.0, 'end-1c') == questions[i]:


      
         engine.say(f'The answer is {correct_answers[i]}')




         
         engine.runAndWait()



         
         
