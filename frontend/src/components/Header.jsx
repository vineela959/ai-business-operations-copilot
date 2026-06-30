import { LogOut, Sparkles } from "lucide-react";

function Header() {
  function handleLogout() {
    localStorage.removeItem("token");
    window.location.reload();
  }

  return (
    <header className="header">
      <div>
        <div className="eyebrow">
          <Sparkles size={16} />
          Multi-Agent AI Operations Platform
        </div>

        <h1>AI Business Operations Copilot</h1>

        <p>
          Manage customers, analyze sales, generate reports, draft emails, and
          automate business workflows using AI agents.
        </p>
      </div>

      <div className="header-actions">
        <div className="status-pill">
          <span></span>
          Live System
        </div>

        <button className="logout-btn" onClick={handleLogout}>
          <LogOut size={16} />
          Logout
        </button>
      </div>
    </header>
  );
}

export default Header;