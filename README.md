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

### 0. Clone the Repository

```bash
git clone https://github.com/your-username/hcp-crm.git
cd hcp-crm
```

Or if you have SSH configured:
```bash
git clone git@github.com:your-username/hcp-crm.git
cd hcp-crm
```

### 1. Prerequisites
- **Python 3.10+** - [Download](https://www.python.org/downloads/)
- **Node.js & npm (v16+)** - [Download](https://nodejs.org/)
- **PostgreSQL 12+** - [Download](https://www.postgresql.org/download/)
- **Groq API Key** - [Get from Groq Console](https://console.groq.com/)
- **Git** - [Download](https://git-scm.com/)

### 2. Database Setup

1. **Start PostgreSQL** (if not already running)
2. **Create the database:**
   ```bash
   createdb hcp_db
   ```
   Or use pgAdmin GUI to create a new database named `hcp_db`

3. **Note your database credentials:**
   - Host: `localhost`
   - Port: `5432` (default)
   - Username: `postgres` (or your username)
   - Password: (your password)
   - Database: `hcp_db`

### 3. Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the `backend/` directory with the following:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   DATABASE_URL=postgresql://postgres:your_password@localhost:5432/hcp_db
   ```
   Replace `your_password` with your actual PostgreSQL password.

5. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The backend will be available at [http://localhost:8000](http://localhost:8000)

### 4. Frontend Setup

1. **In a new terminal, navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```
   The frontend will automatically open at [http://localhost:3000](http://localhost:3000)

## 🚀 Running the Application

### Quick Start (All Together)

**Terminal 1 - Start Backend:**
```bash
cd backend
source venv/Scripts/activate  # Windows: venv\Scripts\activate
uvicorn app.main:app --reload
```
✅ Wait for: `Application startup complete`

**Terminal 2 - Start Frontend:**
```bash
cd frontend
npm start
```
✅ Browser will auto-open to [http://localhost:3000](http://localhost:3000)

### Verification Checklist
- [ ] Backend running on [http://localhost:8000](http://localhost:8000) (shows Swagger docs)
- [ ] Frontend running on [http://localhost:3000](http://localhost:3000)
- [ ] PostgreSQL is running and `hcp_db` database exists
- [ ] `.env` file in `backend/` folder with correct `GROQ_API_KEY` and `DATABASE_URL`
- [ ] No error messages in either terminal

### Using the Application

1. **Form + Chat Interface:** Form on left, AI Assistant chat on right
2. **Describe your meeting:** Type a natural language description in the chat (e.g., "Met with Dr. Smith, discussed B-Complex benefits, very interested")
3. **AI Extracts Data:** The assistant automatically:
   - Logs the HCP interaction
   - Fills the form fields
   - Stores in the database
4. **Available Commands:** Ask the AI to:
   - "Log this interaction"
   - "Edit the HCP name to..."
   - "Show my meeting history"
   - "Schedule a follow-up for..."
   - "Tell me about B-Complex"

## 🔧 Troubleshooting

### Backend won't start
- **Error:** `ModuleNotFoundError: No module named...`
  - Solution: Ensure virtual environment is activated and `pip install -r requirements.txt` was run
- **Error:** `GROQ_API_KEY not set`
  - Solution: Check `.env` file exists in `backend/` folder with valid key
- **Error:** `Database connection failed`
  - Solution: Verify PostgreSQL is running and `DATABASE_URL` in `.env` is correct

### Frontend won't load
- **Error:** `Cannot reach backend`
  - Solution: Ensure backend is running on `http://localhost:8000`
- **Error:** `npm start` fails
  - Solution: Delete `node_modules/` and `package-lock.json`, then run `npm install` again

### Database issues
- **Database doesn't exist:** Run `createdb hcp_db` in terminal
- **Wrong credentials:** Check PostgreSQL default user is `postgres` with your set password

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

