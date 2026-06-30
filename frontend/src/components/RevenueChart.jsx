import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  LabelList,
} from "recharts";
import { useEffect, useState } from "react";
import { getRevenueChartData } from "../services/api";

function RevenueChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function loadChartData() {
      const result = await getRevenueChartData();

      const cleaned = result.map((item) => ({
        product: item.product || "Unknown",
        revenue: Number(item.revenue || 0),
      }));

      setData(cleaned);
    }

    loadChartData();
  }, []);

  return (
    <div className="chart-card">
      <div className="chart-title-row">
        <div>
          <h3>Revenue by Product</h3>
          <p>Live revenue breakdown from PostgreSQL</p>
        </div>
      </div>

      <ResponsiveContainer width="100%" height={280}>
        <BarChart data={data} margin={{ top: 28, right: 24, left: 8, bottom: 24 }}>
          <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />

          <XAxis
            dataKey="product"
            tick={{ fontSize: 12 }}
            tickLine={false}
            axisLine={false}
          />

          <YAxis
            tick={{ fontSize: 12 }}
            tickLine={false}
            axisLine={false}
            tickFormatter={(value) => `₹${value / 1000}k`}
          />

          <Tooltip
            formatter={(value) => [`₹ ${Number(value).toLocaleString("en-IN")}`, "Revenue"]}
            labelStyle={{ fontWeight: 700 }}
          />

          <Bar dataKey="revenue" fill="#2563eb" radius={[12, 12, 0, 0]}>
            <LabelList
              dataKey="revenue"
              position="top"
              formatter={(value) => `₹ ${Number(value).toLocaleString("en-IN")}`}
              style={{ fontWeight: 700, fill: "#2563eb", fontSize: 12 }}
            />
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default RevenueChart;