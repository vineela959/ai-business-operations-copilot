import { Bot, FileText, TrendingUp, Users } from "lucide-react";

function RecentActivity() {
  const activities = [
    {
      icon: Users,
      title: "CRM Agent analyzed customers",
      time: "Just now",
    },
    {
      icon: TrendingUp,
      title: "Sales Agent reviewed revenue data",
      time: "Today",
    },
    {
      icon: FileText,
      title: "Report Agent generated business report",
      time: "Today",
    },
    {
      icon: Bot,
      title: "Supervisor routed request to CRM Agent",
      time: "Recently",
    },
  ];

  return (
    <section className="activity-card">
      <h3>Recent AI Activity</h3>
      <p>Latest actions from your business agents</p>

      <div className="activity-list">
        {activities.map((item, index) => {
          const Icon = item.icon;

          return (
            <div className="activity-item" key={index}>
              <div className="activity-icon">
                <Icon size={18} />
              </div>

              <div>
                <h4>{item.title}</h4>
                <span>{item.time}</span>
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}

export default RecentActivity;