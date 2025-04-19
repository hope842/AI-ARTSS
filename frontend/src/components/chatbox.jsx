import React, { useState } from 'react';
import axios from 'axios';

function ChatBox() {
  const [message, setMessage] = useState('');
  const [responses, setResponses] = useState([]);

  const sendMessage = async () => {
    const res = await axios.post('http://localhost:5000/api/analyze', {
      note: message
    });
    setResponses(prev => [...prev, { message, response: res.data }]);
    setMessage('');
  };

  return (
    <div>
      <textarea
        rows="4"
        cols="60"
        placeholder="Type clinical note here..."
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
      <br />
      <button onClick={sendMessage}>Send</button>

      <ul>
        {responses.map((entry, idx) => (
          <li key={idx}>
            <strong>You:</strong> {entry.message}<br />
            <strong>Bot:</strong>
            <pre>{JSON.stringify(entry.response, null, 2)}</pre>
            {entry.response.protocol && (
              <p>📤 Alert: Prescription for {entry.response.protocol} sent to Pharmacy!</p>
            )}
            <hr />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ChatBox;
