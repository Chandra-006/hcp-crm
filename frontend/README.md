# HCP CRM Frontend

The React frontend for the AI-Powered HCP CRM Assistant. This component provides a split-screen interface with an interaction form and an AI chat assistant.

## 🚀 Features

- **Split-Screen UI:** Real-time reactive interface with form on the left and AI assistant on the right.
- **Redux State Management:** Keeps the form synchronized with the backend database.
- **Responsive Design:** Clean, modern UI built with React.

## 🛠️ Tech Stack

- **React:** Frontend framework
- **Redux Toolkit:** State management
- **Axios:** HTTP client for API calls
- **CSS Modules:** Styling

## ⚙️ Setup & Installation

### Prerequisites
- Node.js 14+ and npm
- Backend server running (see root README)

### Installation
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The app will open at [http://localhost:3000](http://localhost:3000).

## 📁 Project Structure

```
src/
├── components/
│   ├── ChatAssistant.jsx    # AI chat interface
│   └── InteractionForm.jsx  # HCP interaction form
├── store/
│   ├── index.js             # Redux store configuration
│   └── interactionSlice.js  # Interaction state slice
├── App.js                  # Main app component
└── index.js                # App entry point
```

## 🧪 Testing

Run tests with:
```bash
npm test
```

## 📦 Build for Production

```bash
npm run build
```

This creates an optimized build in the `build` folder.

## 🤝 Contributing

See the main project README for contribution guidelines.

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
