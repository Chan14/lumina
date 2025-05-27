# ✨ Lumina: Your AI-Powered Learning Companion

**Lumina** is a terminal-based study assistant designed to help you track learning notes, set long-term goals, and receive intelligent, personalized feedback—all powered by Google's Gemini AI.

---

## 🚀 Features

- 📚 Add and view structured learning notes
- 🎯 Define and manage long-term learning goals
- 🧠 Receive AI-generated study reviews based on your notes
- 🤖 Interactive subgoal generation (coming soon)
- 💾 Local JSON-based data storage for privacy and simplicity

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Google Generative AI (Gemini API)**
- Modular architecture with `core/`, `ai/`, `data/`, and `utils/` directories
- Environment configuration via `.env` files

---

## 📂 Project Structure

lumina/
├── ai/ # AI integrations and logic
├── core/ # Core application logic (notes, goals)
├── data/ # JSON files storing notes and goals
├── utils/ # Utility functions
├── main.py # Entry point for the application
├── .env # Environment variables (not committed)
├── .gitignore # Specifies files to ignore in version control
├── README.md # Project overview and setup instructions
└── DESIGN.md # Detailed design and architecture documentation

---

## ⚙️ Getting Started

1. **Clone the repository:**h
   git clone https://github.com/Chan14/lumina.git
   cd lumina

2. Set up a virtual environment:
   python3 -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure environment variables:
   Create a .env file in the root directory.
   Add your Gemini API key:
   GEMINI_API_KEY=your_actual_key_here

5. Run the application:
   python main.py

📈 Roadmap
Implement interactive subgoal generation with Gemini

Enhance terminal UI with libraries like Rich or Textual

Integrate scheduling and reminders

Expand AI capabilities for deeper learning insights

👤 Maintainer
Chanchal Goyal (GitHub: @Chan14)
