import { useEffect, useState } from "react";
import { getCustomers } from "../services/api";

function CustomersTable() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    async function loadCustomers() {
      const data = await getCustomers();
      setCustomers(data);
    }

    loadCustomers();
  }, []);

  return (
    <section className="activity-card">
      <h3>Recent Customers</h3>
      <p>Live CRM records from PostgreSQL</p>

      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Company</th>
              <th>Email</th>
            </tr>
          </thead>

          <tbody>
            {customers.slice(0, 5).map((customer) => (
              <tr key={customer.id}>
                <td>{customer.name}</td>
                <td>{customer.company}</td>
                <td>{customer.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export default CustomersTable;