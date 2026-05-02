# 🐾 PawPal+ AI System

PawPal+ is an AI-powered pet care scheduling system that helps pet owners organize tasks, detect conflicts, and receive intelligent recommendations for safer and more effective pet care.

---

## 🚀 Features

- Add and manage pets  
- Create and track pet care tasks  
- Automatically sort tasks by time  
- Detect scheduling conflicts  
- AI-powered insights and recommendations  
- Streamlit interactive UI  
- Automated testing with pytest  

---

## 🧠 System Architecture

![System Diagram](assets/system_diagram.png)

---

## 🧩 How It Works

### Core Components

- **Task** → Represents a pet care activity  
- **Pet** → Stores tasks per pet  
- **Owner** → Manages multiple pets  
- **Scheduler** → Sorts tasks and detects conflicts  
- **AI Engine (NEW)** → Analyzes schedule and provides intelligent insights  

---

## 🔄 Data Flow

1. User inputs tasks through the UI  
2. Scheduler organizes tasks and detects conflicts  
3. AI Engine retrieves relevant pet care knowledge  
4. AI generates warnings, suggestions, and explanations  
5. Results are displayed to the user  

---

## 🛡️ Reliability & Testing

- Pytest ensures core logic correctness  
- AI guardrails prevent unsafe or invalid outputs  
- Conflict detection ensures schedule integrity  

---

## 🗂️ Project Structure
flowchart TD

    A[User Input] --> B[Streamlit UI (app.py)]

    B --> C[Scheduler]
    C --> D[Sorted Tasks + Conflicts]

    D --> E[AI Engine]

    E --> F[Retriever (Knowledge Base)]
    F --> G[Pet Care Knowledge]

    G --> E

    E --> H[AI Analysis]
    H --> I[Final Output]

    I --> J[User Display]

    %% Testing + Reliability
    D --> K[Pytest Tests]
    E --> L[AI Validation / Guardrails]

    K --> M[Verified Logic]
    L --> M

    M --> J
    # 🐾 PawPal+ AI: Intelligent Pet Care Assistant

## 📌 Title & Summary

PawPal+ AI is an intelligent pet care scheduling system that helps pet owners manage daily tasks while providing AI-powered recommendations for safety and efficiency. 

Unlike a basic scheduler, this system analyzes task timing, detects conflicts, retrieves relevant pet care knowledge, and generates actionable insights to improve pet well-being.

---

## 🔁 Original Project (Modules 1–3)

The original project, **PawPal+**, was a pet care scheduling application built in Python using Streamlit.

It allowed users to:
- Add pets and assign tasks (feeding, walking, vet visits)
- Sort tasks by time
- Detect scheduling conflicts

The system focused on clean design, modular classes (Task, Pet, Owner, Scheduler), and correctness through testing, but did not include any AI-based reasoning or decision-making.

---

## 🧠 Architecture Overview

The system is composed of several key components working together:

- **Streamlit UI (app.py)** → Handles user input and displays results  
- **Scheduler** → Sorts tasks and detects conflicts  
- **AI Engine (NEW)** → Analyzes tasks and generates intelligent insights  
- **Knowledge Base (RAG)** → Stores pet care best practices  
- **Testing Layer (pytest)** → Ensures correctness and reliability  

### Data Flow:
1. User inputs tasks  
2. Scheduler organizes and detects conflicts  
3. AI Engine retrieves relevant knowledge  
4. AI generates warnings and suggestions  
5. Results are displayed to the user  

![System Diagram](assets/system_diagram.png)

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/applied-ai-system-project.git
cd applied-ai-system-project