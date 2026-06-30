import { useEffect, useState } from "react";
import { getSales } from "../services/api";

function SalesTable() {
  const [sales, setSales] = useState([]);

  useEffect(() => {
    async function loadSales() {
      const data = await getSales();
      setSales(data);
    }

    loadSales();
  }, []);

  return (
    <section className="activity-card">
      <h3>Recent Sales</h3>
      <p>Live sales records from PostgreSQL</p>

      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Product</th>
              <th>Amount</th>
              <th>Date</th>
            </tr>
          </thead>

          <tbody>
            {sales.slice(0, 5).map((sale) => (
              <tr key={sale.id}>
                <td>{sale.product}</td>
                <td>₹ {sale.amount}</td>
                <td>{sale.sale_date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export default SalesTable;