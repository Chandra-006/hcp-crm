import React from 'react';
import { useSelector } from 'react-redux';

const InteractionForm = () => {
    const data = useSelector((state) => state.interaction);
  
    return (
      <div style={{ padding: '20px', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
        <div>
          <label>HCP Name</label>
          <input type="text" value={data.hcp_name} readOnly style={inputStyle} />
        </div>
        <div>
          <label>Interaction Type</label>
          <select value={data.interaction_type} disabled style={inputStyle}>
              <option>Meeting</option>
          </select>
        </div>
        <div>
          <label>Date</label>
          <input type="text" value={data.date} readOnly style={inputStyle} />
        </div>
        <div>
          <label>Time</label>
          <input type="text" value={data.time} readOnly style={inputStyle} />
        </div>
        <div style={{ gridColumn: 'span 2' }}>
          <label>Topics Discussed</label>
          <textarea value={data.topics_discussed} readOnly style={{...inputStyle, height: '80px'}} />
        </div>
        <div>
  <label style={{ fontWeight: 'bold', display: 'block', marginBottom: '5px' }}>Sentiment</label>
  <div style={{ display: 'flex', gap: '15px', marginTop: '5px' }}>
    {['Positive', 'Neutral', 'Negative'].map(s => {
      // This checks if the sentiment from the AI contains our keyword
      // e.g., if AI says "very bad", it matches "Negative"
      const isChecked = 
        data.sentiment?.toLowerCase().includes(s.toLowerCase()) || 
        (s === 'Negative' && data.sentiment?.toLowerCase().includes('bad'));

      return (
        <label key={s} style={{ display: 'flex', alignItems: 'center', gap: '5px', cursor: 'default' }}>
          <input 
            type="radio" 
            checked={isChecked} 
            readOnly 
            style={{ cursor: 'default' }}
          /> 
          {s}
        </label>
      );
    })}
          </div>
        </div>
      </div>
    );
  };
  
  const inputStyle = { width: '100%', padding: '10px', marginTop: '5px', border: '1px solid #ddd', borderRadius: '4px', backgroundColor: '#fdfdfd' };

export default InteractionForm;