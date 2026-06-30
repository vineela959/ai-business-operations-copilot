import SalesChart from "./SalesChart";
import RevenueChart from "./RevenueChart";

function DashboardStats() {
  return (
    <section className="dashboard-stats">
      <SalesChart />
      <RevenueChart />
    </section>
  );
}

export default DashboardStats;