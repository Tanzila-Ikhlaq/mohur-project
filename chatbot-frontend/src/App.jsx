import React, { useState } from "react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const handleAsk = async () => {
    if (!input.trim()) return;

    const res = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: input }),
    });
    const data = await res.json();

    setMessages((prev) => [
      ...prev,
      { sender: "user", text: input },
      { sender: "bot", text: data.answer },
    ]);
    setInput("");
  };

  return (
    <div className="app-container">
      <div className="chatbox">

        <div className="chat-header">🤖 Mini AI Chatbot</div>

        <div className="chat-messages">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`message ${msg.sender}`}
            >
              <div className="message-content">{msg.text}</div>
            </div>
          ))}
        </div>

        <div className="chat-input-area">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleAsk()}
            placeholder="Type a message..."
          />
          <button onClick={handleAsk}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
