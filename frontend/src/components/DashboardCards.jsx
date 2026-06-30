import { Users, TrendingUp, FileText, IndianRupee } from "lucide-react";
import { useEffect, useState } from "react";
import { getDashboardStats } from "../services/api";

function DashboardCards() {
  const [stats, setStats] = useState({
    customers: 0,
    sales: 0,
    reports: 0,
    revenue: 0,
  });

  useEffect(() => {
    async function loadStats() {
      const data = await getDashboardStats();
      setStats(data);
    }

    loadStats();
  }, []);

  const cards = [
    { title: "Customers", value: stats.customers, icon: Users },
    { title: "Sales", value: stats.sales, icon: TrendingUp },
    { title: "Reports", value: stats.reports, icon: FileText },
    { title: "Revenue", value: `₹ ${stats.revenue}`, icon: IndianRupee },
  ];

  return (
    <section className="cards">
      {cards.map((card) => {
        const Icon = card.icon;

        return (
          <div className="card" key={card.title}>
            <div className="card-icon">
              <Icon size={22} />
            </div>

            <p>{card.title}</p>
            <h2>{card.value}</h2>
          </div>
        );
      })}
    </section>
  );
}

export default DashboardCards;