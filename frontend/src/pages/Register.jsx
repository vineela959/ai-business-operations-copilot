import { useState } from "react";
import { registerUser } from "../services/api";

function Register({ onSwitchToLogin }) {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function handleRegister(e) {
    e.preventDefault();
    setMessage("");
    setError("");

    const data = await registerUser({
      full_name: fullName,
      email,
      password,
    });

    if (data.id) {
      setMessage("Account created successfully. Please login.");
      setFullName("");
      setEmail("");
      setPassword("");
    } else {
      setError(data.detail || "Registration failed");
    }
  }

  return (
    <div className="auth-page">
      <form className="auth-card" onSubmit={handleRegister}>
        <h1>Create Account</h1>
        <p>Start using your AI operations dashboard</p>

        {message && <div className="auth-success">{message}</div>}
        {error && <div className="auth-error">{error}</div>}

        <label>Full Name</label>
        <input value={fullName} onChange={(e) => setFullName(e.target.value)} />

        <label>Email</label>
        <input value={email} onChange={(e) => setEmail(e.target.value)} />

        <label>Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit">Create Account</button>

        <button type="button" className="auth-link" onClick={onSwitchToLogin}>
          Already have an account? Login
        </button>
      </form>
    </div>
  );
}

export default Register;