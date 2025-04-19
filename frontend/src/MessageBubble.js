import React from 'react';

function MessageBubble({ type, text, protocol }) {
  return (
    <div className={`bubble ${type}`}>
      <pre>{text}</pre>
      {protocol && (
        <div className="alert">📤 Alert: Prescription for <strong>{protocol}</strong> sent to Pharmacy!</div>
      )}
    </div>
  );
}

export default MessageBubble;
