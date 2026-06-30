import { useState } from "react";
import { loginUser } from "../services/api";

function Login({ onLogin, onSwitchToRegister }) {
  const [email, setEmail] = useState("vinni@example.com");
  const [password, setPassword] = useState("test12345");
  const [error, setError] = useState("");

  async function handleLogin(e) {
    e.preventDefault();
    setError("");

    const data = await loginUser({ email, password });

    if (data.access_token) {
      localStorage.setItem("token", data.access_token);
      onLogin(data.access_token);
    } else {
      setError(data.detail || "Login failed");
    }
  }

  return (
    <div className="auth-page">
      <form className="auth-card" onSubmit={handleLogin}>
        <h1>AI Ops Copilot</h1>
        <p>Login to your business operations dashboard</p>

        {error && <div className="auth-error">{error}</div>}

        <label>Email</label>
        <input value={email} onChange={(e) => setEmail(e.target.value)} />

        <label>Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit">Login</button>

        <button type="button" className="auth-link" onClick={onSwitchToRegister}>
          New user? Create account
        </button>
      </form>
    </div>
  );
}

export default Login;