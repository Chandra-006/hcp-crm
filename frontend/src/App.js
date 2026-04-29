import React from 'react';
import InteractionForm from './components/InteractionForm';
import ChatAssistant from './components/ChatAssistant';

/**
 * Main App component for the HCP CRM interface.
 *
 * Renders a split-screen layout with the interaction form on the left
 * and the AI chat assistant on the right.
 */
function App() {
  return (
    <div style={{ display: 'flex', height: '100vh', fontFamily: 'sans-serif' }}>
      {/* Left Panel: Form */}
      <div style={{ flex: 1, padding: '20px', borderRight: '1px solid #ccc', backgroundColor: '#f9f9f9' }}>
        <h2>Interaction Details</h2>
        <InteractionForm />
      </div>

      {/* Right Panel: AI Chat */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', padding: '20px' }}>
        <h2>AI Assistant</h2>
        <ChatAssistant />
      </div>
    </div>
  );
}

export default App;