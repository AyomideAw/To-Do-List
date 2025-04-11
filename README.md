# 📝 To-Do List Application

A simple desktop To-Do List application built using Python's Tkinter library. This program allows users to add and delete tasks with ease, maintaining a persistent list stored in a local text file. Designed with a clean graphical interface and basic file operations, it's a great utility for managing daily tasks efficiently.

# 📦 Tech Stack

Language: Python

GUI Framework: Tkinter

Image Handling: PIL (Python Imaging Library)

# 🚀 Features

✅ Add tasks to a persistent list

❌ Delete selected tasks from the list

💾 Local storage of tasks in tasklist.txt

🖼️ Custom window icon using task.png

🎨 User-friendly interface with labels, buttons, and listbox

# 📂 Folder Structure

├── main.py              # Main application logic

├── tasklist.txt         # Persistent storage for tasks

├── Image/

│   └── task.png         # Application icon

# 🛠️ Getting Started

- Prerequisites

Python 3.x installed

PIL library (install via pip install pillow)

Run the Application

python main.py

# 🧠 How It Works

- On launch, the app loads any existing tasks from tasklist.txt.
- Users can type in a new task and click Add to store it.
- Clicking Delete removes the selected task from both the list and the file.

# 🧼 Notes

- Make sure tasklist.txt and task.png are present in the same directory as main.py.
- This app is for local use and does not support multi-user or online syncing.

# 🙌 Acknowledgements

Built using Python’s Tkinter library
