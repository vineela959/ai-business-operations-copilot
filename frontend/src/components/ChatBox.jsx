import { useEffect, useRef, useState } from "react";
import { Bot, Send, User, Loader2, FileSearch, Network } from "lucide-react";
import { askSupervisor, askDocuments } from "../services/api";

function ChatBox() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);
  const [mode, setMode] = useState("business");
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat, loading]);

  async function handleAsk() {
    if (!message.trim() || loading) return;

    const userMessage = message.trim();
    setMessage("");

    setChat((prev) => [
      ...prev,
      {
        role: "user",
        content: userMessage,
      },
    ]);

    setLoading(true);

    try {
      const data =
        mode === "documents"
          ? await askDocuments(userMessage)
          : await askSupervisor(userMessage);

      setChat((prev) => [
        ...prev,
        {
          role: "ai",
          content: data.response || "No response received.",
          route: data.route || mode,
        },
      ]);
    } catch (error) {
      setChat((prev) => [
        ...prev,
        {
          role: "ai",
          content:
            "Unable to reach the AI backend. Please check if FastAPI is running.",
          route: "error",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleAsk();
    }
  }

  return (
    <section className="chat-box">
      <div className="chat-header">
        <div>
          <h2>AI Copilot Chat</h2>
          <p>Switch between business agents and document Q&A.</p>
        </div>

        <div className="mode-toggle">
          <button
            className={mode === "business" ? "active" : ""}
            onClick={() => setMode("business")}
          >
            <Network size={15} />
            Business
          </button>

          <button
            className={mode === "documents" ? "active" : ""}
            onClick={() => setMode("documents")}
          >
            <FileSearch size={15} />
            Documents
          </button>
        </div>
      </div>

      <div className="chat-window">
        {chat.length === 0 && (
          <div className="empty-chat">
            <Bot size={44} />
            <h3>How can I help your business today?</h3>
            <p>
              Business: “Analyze our CRM customers” · Documents: “What is the
              monthly revenue?”
            </p>
          </div>
        )}

        {chat.map((item, index) => (
          <div key={index} className={`message ${item.role}`}>
            <div className="avatar">
              {item.role === "user" ? <User size={18} /> : <Bot size={18} />}
            </div>

            <div className="message-content">
              {item.route && (
                <span className={`agent-badge ${item.route}`}>
                  Agent: {item.route}
                </span>
              )}

              <p>{item.content}</p>
            </div>
          </div>
        ))}

        {loading && (
          <div className="message ai">
            <div className="avatar">
              <Bot size={18} />
            </div>

            <div className="message-content thinking">
              <Loader2 size={16} className="spin" />
              <p>AI agent is thinking...</p>
            </div>
          </div>
        )}

        <div ref={chatEndRef}></div>
      </div>

      <div className="chat-input">
        <textarea
          placeholder={
            mode === "documents"
              ? "Ask about your uploaded documents..."
              : "Ask your business copilot..."
          }
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
        />

        <button onClick={handleAsk} disabled={loading}>
          <Send size={18} />
        </button>
      </div>
    </section>
  );
}

export default ChatBox;