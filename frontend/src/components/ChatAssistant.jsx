import React, { useState } from 'react';
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { updateFields } from '../store/interactionSlice';

const ChatAssistant = () => {
  const [input, setInput] = useState('');
  // Local state to store chat bubbles
  const [messages, setMessages] = useState([{ text: "Hello! I'm your AI CRM assistant.", sender: 'ai' }]);
  const dispatch = useDispatch();

  const handleSend = async () => {
    if (!input.trim()) return;

    // 1. Add the user's message to the UI immediately
    setMessages(prev => [...prev, { text: input, sender: 'user' }]);
    setInput('');

    try {
      // 2. Call the FastAPI backend
      const response = await axios.post('http://127.0.0.1:8000/api/chat', { message: input });
      
      const { response: aiReply, extracted_data } = response.data;

      // 3. Add the AI's spoken reply to the UI
      setMessages(prev => [...prev, { text: aiReply, sender: 'ai' }]);

      // 4. SYNC: If the AI updated the database, we update our Redux store
      // This is what makes the left-side form fill up automatically!
      if (extracted_data) {
        dispatch(updateFields(extracted_data));
      }
    } catch (error) {
      setMessages(prev => [...prev, { text: "Connection error. Is backend running?", sender: 'ai' }]);
    }
  };

  return (
    <div className="chat-container" style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      {/* Scrollable message area */}
      <div className="messages-box" style={{ flex: 1, overflowY: 'auto', marginBottom: '10px' }}>
        {messages.map((m, i) => (
          <div key={i} style={{ textAlign: m.sender === 'user' ? 'right' : 'left', margin: '8px' }}>
            <span style={{ 
              background: m.sender === 'user' ? '#007bff' : '#f1f1f1', 
              color: m.sender === 'user' ? '#fff' : '#000',
              padding: '10px', borderRadius: '15px', display: 'inline-block', maxWidth: '80%'
            }}>{m.text}</span>
          </div>
        ))}
      </div>
      {/* Input area */}
      <div className="input-row" style={{ display: 'flex', gap: '5px' }}>
        <input 
          value={input} 
          onChange={(e) => setInput(e.target.value)} 
          onKeyDown={(e) => e.key === 'Enter' && handleSend()} // Allow sending via Enter key
          placeholder="Type your interaction details..."
          style={{ flex: 1, padding: '10px', borderRadius: '5px', border: '1px solid #ccc' }}
        />
        <button onClick={handleSend} style={{ padding: '10px', background: '#28a745', color: '#fff', border: 'none', borderRadius: '5px' }}>Send</button>
      </div>
    </div>
  );
};

export default ChatAssistant;