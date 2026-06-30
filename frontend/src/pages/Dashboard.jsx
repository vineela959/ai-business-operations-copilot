import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import DashboardCards from "../components/DashboardCards";
import DashboardStats from "../components/DashboardStats";
import ChatBox from "../components/ChatBox";
import RecentActivity from "../components/RecentActivity";
import AIInsights from "../components/AIInsights";
import CustomersTable from "../components/CustomersTable";
import SalesTable from "../components/SalesTable";
import DocumentsPanel from "../components/DocumentsPanel";

function Dashboard() {
  return (
    <div className="app-layout">
      <Sidebar />

      <main className="main-content">
        <Header />
        <DashboardCards />
        <DashboardStats />

        <div className="tables-grid">
          <CustomersTable />
          <SalesTable />
        </div>

        <div className="dashboard-grid">
          <ChatBox />

          <div className="side-panels">
            <DocumentsPanel />
            <RecentActivity />
            <AIInsights />
          </div>
        </div>
      </main>
    </div>
  );
}

export default Dashboard;