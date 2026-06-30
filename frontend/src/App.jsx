import { useEffect, useState } from "react";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import Register from "./pages/Register";
import { getCurrentUser } from "./services/api";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [loading, setLoading] = useState(true);
  const [authMode, setAuthMode] = useState("login");

  useEffect(() => {
    async function verifyUser() {
      if (!token) {
        setLoading(false);
        return;
      }

      const user = await getCurrentUser(token);

      if (user.detail) {
        localStorage.removeItem("token");
        setToken(null);
      }

      setLoading(false);
    }

    verifyUser();
  }, [token]);

  if (loading) {
    return <div className="loading-screen">Loading...</div>;
  }

  if (!token && authMode === "login") {
    return (
      <Login
        onLogin={setToken}
        onSwitchToRegister={() => setAuthMode("register")}
      />
    );
  }

  if (!token && authMode === "register") {
    return <Register onSwitchToLogin={() => setAuthMode("login")} />;
  }

  return <Dashboard />;
}

export default App;