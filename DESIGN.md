📄 License
This project is licensed under the MIT License.

---

## 📐 DESIGN.md

```markdown
# 🧠 Lumina Design Document

## 🎯 Vision

Lumina aims to be an intelligent, terminal-based study companion that assists learners in organizing their study materials, setting and tracking goals, and receiving personalized feedback through AI integrations.

---

## 🏗️ Architecture Overview

### Core Modules

- `main.py`: Entry point presenting a CLI menu for user interaction.
- `core/notes.py`: Functions to add and display learning notes.
- `core/goals.py`: Functions to add and display long-term goals.
- `ai/review.py`: Handles AI-generated study reviews using Gemini.
- `ai/subgoalizer.py`: (Planned) Facilitates AI-driven subgoal generation.
- `utils/`: Contains utility functions for file handling and other helpers.

### Data Storage

- `data/notes.json`: Stores user-entered learning notes.
- `data/goals.json`: Stores user-defined long-term goals and subgoals.

---

## 🔄 Workflow

1. **Adding Notes and Goals:**

   - Users input learning notes and define long-term goals via the CLI.
   - Data is stored locally in JSON format for simplicity and privacy.

2. **AI-Generated Study Reviews:**

   - Users can request a study review.
   - The application compiles recent notes and sends them to the Gemini API.
   - The AI returns a summary with insights and suggestions.

3. **Subgoal Generation (Planned):**
   - Users select a long-term goal.
   - The application initiates an interactive session with Gemini to break down the goal into actionable subgoals.
   - Upon user confirmation, subgoals are added to `goals.json`.

---

## 🧪 Dependencies

- `google-generativeai`: Interface with Google's Gemini API.
- `python-dotenv`: Manage environment variables securely.
- Standard Python libraries: `json`, `pathlib`, `os`, etc.

---

## 🛣️ Future Enhancements

- **Interactive Subgoal Generation:**

  - Develop `ai/subgoalizer.py` to facilitate dynamic goal breakdowns.

- **Enhanced Terminal UI:**

  - Integrate libraries like Rich or Textual for a more engaging CLI experience.

- **Scheduling and Reminders:**

  - Implement features to schedule study sessions and send reminders.

- **Data Visualization:**
  - Provide visual representations of progress and goal completion.

---

## ⚠️ Considerations

- **Data Privacy:**

  - All user data is stored locally; no cloud storage is involved.

- **Extensibility:**

  - The modular design allows for easy addition of new features and integrations.

- **Error Handling:**
  - Implement robust error handling for file operations and API interactions.

---

## 📌 Status

- **Core Functionality:** Implemented
- **AI Study Reviews:** Implemented
- **Subgoal Generation:** Planned
- **Enhanced UI:** Planned
```
