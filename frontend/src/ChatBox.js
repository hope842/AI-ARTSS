import React, { useState } from 'react';
import axios from 'axios';
import MessageBubble from './MessageBubble';

function ChatBox() {
  const [message, setMessage] = useState('');
  const [history, setHistory] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const res = await axios.post('http://localhost:5000/api/analyze', { note: message });
    setHistory([...history, { type: 'user', text: message }, { type: 'bot', text: JSON.stringify(res.data, null, 2), protocol: res.data.protocol }]);
    setMessage('');
  };

  return (
    <div className="chat-container">
      <div className="chat-window">
        {history.map((msg, idx) => (
          <MessageBubble key={idx} type={msg.type} text={msg.text} protocol={msg.protocol} />
        ))}
      </div>
      <div className="input-area">
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type clinical note here..."
          className="chat-input"
          rows="3"
        />
        <button onClick={sendMessage} className="send-btn">Send</button>
      </div>
    </div>
  );
}

export default ChatBox;
