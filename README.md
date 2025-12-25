🎯 KBC-Style Quiz Game
A fully functional, GUI-based Kaun Banega Crorepati (KBC) clone built with Python. This project simulates the thrill of the popular TV game show, featuring a progression-based difficulty system, interactive lifelines, and a polished user interface.

✨ Key Features

1.) Interactive GUI: A clean and user-friendly interface built using Tkinter.
2.) Level-Based Progression: Questions increase in difficulty as the prize money grows, mirroring the real show's format.
3.) Authentic Lifelines: * 50:50: Eliminates two incorrect options.
4.) Audience Poll: Simulates weighted random logic to suggest the most likely answer.
5.) Skip Question: Allows the player to move to the next question without penalty.
6.) Dynamic Question Bank: Uses a JSON backend for easy management and expansion of questions.
7.) Visual Feedback: Immediate color-coded feedback for correct and incorrect answers.

🛠️ Technologies & Libraries Used

1.) Python (Core Logic): Used for game state management and Object-Oriented Programming (OOP).
2.) Tkinter: For building the graphical user interface.
3.) JSON: To store and retrieve a structured database of questions.
4.) Random & Time: For shuffling options and creating realistic delays for interactivity.

📂 Project Structure
├── main.py              # Entry point to start the game
├── quiz_logic.py        # Core logic for scoring and lifelines
├── ui_design.py         # Tkinter layout and styling
├── questions.json       # Structured question database
└── assets/              # Icons and images used in the GUI
