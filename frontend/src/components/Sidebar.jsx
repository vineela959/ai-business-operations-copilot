import {
  LayoutDashboard,
  Users,
  TrendingUp,
  FileText,
  Mail,
  Brain,
  BarChart3,
} from "lucide-react";

function Sidebar() {
  const items = [
    { label: "Dashboard", icon: LayoutDashboard },
    { label: "Customers", icon: Users },
    { label: "Sales", icon: TrendingUp },
    { label: "Reports", icon: FileText },
    { label: "Email", icon: Mail },
    { label: "Knowledge", icon: Brain },
    { label: "Analytics", icon: BarChart3 },
  ];

  return (
    <aside className="sidebar">
      <div className="brand">
        <div className="brand-icon">AI</div>
        <div>
          <h2>Ops Copilot</h2>
          <p>Business AI Suite</p>
        </div>
      </div>

      <nav>
        {items.map((item) => {
          const Icon = item.icon;
          return (
            <a key={item.label}>
              <Icon size={18} />
              <span>{item.label}</span>
            </a>
          );
        })}
      </nav>
    </aside>
  );
}

export default Sidebar;