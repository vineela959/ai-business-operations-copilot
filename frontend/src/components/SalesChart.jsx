import {
  Area,
  AreaChart,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";
import { useEffect, useState } from "react";
import { getSalesChartData } from "../services/api";

function SalesChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function loadChartData() {
      const result = await getSalesChartData();

      const cleaned = result.map((item, index) => ({
        label: item.label || `Sale ${index + 1}`,
        amount: Number(item.amount || 0),
      }));

      setData(cleaned);
    }

    loadChartData();
  }, []);

  return (
    <div className="chart-card">
      <div className="chart-title-row">
        <div>
          <h3>Sales Performance</h3>
          <p>Live sales data from PostgreSQL</p>
        </div>
      </div>

      <ResponsiveContainer width="100%" height={280}>
        <AreaChart data={data} margin={{ top: 20, right: 24, left: 8, bottom: 24 }}>
          <defs>
            <linearGradient id="salesGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#2563eb" stopOpacity={0.25} />
              <stop offset="95%" stopColor="#2563eb" stopOpacity={0.02} />
            </linearGradient>
          </defs>

          <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />

          <XAxis
            dataKey="label"
            tick={{ fontSize: 12 }}
            tickLine={false}
            axisLine={false}
            interval={0}
          />

          <YAxis
            tick={{ fontSize: 12 }}
            tickLine={false}
            axisLine={false}
            tickFormatter={(value) => `₹${value / 1000}k`}
          />

          <Tooltip
            formatter={(value) => [`₹ ${Number(value).toLocaleString("en-IN")}`, "Sales"]}
            labelStyle={{ fontWeight: 700 }}
          />

          <Area
            type="monotone"
            dataKey="amount"
            stroke="#2563eb"
            strokeWidth={3}
            fill="url(#salesGradient)"
            dot={{ r: 5 }}
            activeDot={{ r: 7 }}
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}

export default SalesChart;