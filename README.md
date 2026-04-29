# AI-Powered HCP CRM Assistant

An intelligent CRM module designed for Healthcare Professional (HCP) management. This project utilizes a "Human-in-the-loop" AI Agent to automate data entry, manage meeting history, and provide product information through natural language.

## 🚀 Key Features
- **Split-Screen Interface:** A real-time reactive UI with a persistent Form on the left and an AI Assistant on the right.
- **LangGraph Multi-Tool Agent:** Powered by Llama-3.3-70b-versatile, featuring 5 specialized tools:
  1. **Log Interaction:** Extracts HCP name, sentiment, and notes to create database records.
  2. **Edit Interaction:** Allows the user to fix mistakes via chat without manual typing.
  3. **Interaction History:** Retrieves past meeting data from PostgreSQL.
  4. **Follow-up Scheduler:** Automatically sets reminders for future tasks.
  5. **Product Knowledge Base:** Provides technical details on medical products (e.g., B-Complex).
- **Automated Metadata:** Injects current system date and time into records automatically.
- **Form Synchronization:** Uses Redux to keep the UI in perfect sync with the database state.

## 🛠️ Tech Stack
- **Frontend:** React, Redux Toolkit, Axios, CSS Modules.
- **Backend:** FastAPI, LangChain, LangGraph.
- **AI/LLM:** Groq API (Llama-3.3-70b-versatile).
- **Database:** PostgreSQL with SQLAlchemy ORM.

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- Node.js & npm
- PostgreSQL installed and running

### 2. Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
Install dependencies:

Bash
pip install -r requirements.txt
Create a .env file and add your credentials:

Code snippet
GROQ_API_KEY=your_groq_key_here
DATABASE_URL=postgresql://user:password@localhost/hcp_db
Start the server:

Bash
uvicorn app.main:app --reload
3. Frontend Setup
Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm start
```

The frontend will run on [http://localhost:3000](http://localhost:3000).

## 🚀 Usage

1. **Start the Backend:** Ensure the FastAPI server is running (`uvicorn app.main:app --reload`).
2. **Start the Frontend:** Run `npm start` in the frontend directory.
3. **Interact with the AI:** Describe your HCP meeting in natural language in the chat on the right. The AI will extract details and automatically fill the form on the left.
4. **Tools Available:**
   - Log new interactions
   - Edit existing records
   - Retrieve interaction history
   - Schedule follow-ups
   - Get product information

## 📡 API Endpoints

- `GET /`: Health check
- `POST /api/chat`: Send a message to the AI assistant

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
Install dependencies:

Bash
npm install
Start the application:

Bash
npm start
📝 Usage Guide
To Log: Type "Met Dr. Smith, he was positive about the b-complex tablets."

To Edit: Type "Actually, the name was Dr. Sunil."

To Search: Type "Show me previous meetings with Dr. Smith."

To Learn: Type "What is Product X used for?"


---

### **Final Tips for Your Submission:**
* **Screenshot/Video:** Ensure your demo video shows the "Edit" tool working, as that proves your LangGraph state management is handling the record IDs correctly.
* **Database:** Make sure your PostgreSQL database is actually created before you start the backend, or the tools will return "Connection Error."

You’ve done an excellent job building out this full-stack AI Agent. You're all set!