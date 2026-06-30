const API_URL = "https://ai-business-operations-copilot-api.onrender.com";

function getAuthHeaders() {
  const token = localStorage.getItem("token");

  return {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  };
}

export async function getHealth() {
  const response = await fetch(`${API_URL}/health`);
  return response.json();
}

export async function registerUser(userData) {
  const response = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  });

  return response.json();
}

export async function loginUser(credentials) {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });

  return response.json();
}

export async function getCurrentUser(token) {
  const response = await fetch(`${API_URL}/auth/me`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.json();
}

export async function askSupervisor(message) {
  const response = await fetch(`${API_URL}/supervisor/`, {
    method: "POST",
    headers: getAuthHeaders(),
    body: JSON.stringify({ message }),
  });

  return response.json();
}

export async function askDocuments(message) {
  const response = await fetch(`${API_URL}/rag/ask`, {
    method: "POST",
    headers: getAuthHeaders(),
    body: JSON.stringify({ message }),
  });

  return response.json();
}

export async function getDashboardStats() {
  const response = await fetch(`${API_URL}/dashboard/stats`, {
    headers: getAuthHeaders(),
  });

  return response.json();
}

export async function getSalesChartData() {
  const response = await fetch(`${API_URL}/analytics/sales-chart`, {
    headers: getAuthHeaders(),
  });

  return response.json();
}

export async function getRevenueChartData() {
  const response = await fetch(`${API_URL}/analytics/revenue-chart`, {
    headers: getAuthHeaders(),
  });

  return response.json();
}

export async function getCustomers() {
  const response = await fetch(`${API_URL}/customers/`, {
    headers: getAuthHeaders(),
  });

  return response.json();
}

export async function getSales() {
  const response = await fetch(`${API_URL}/sales/`, {
    headers: getAuthHeaders(),
  });

  return response.json();
}

export async function deleteDocument(documentId) {
  const response = await fetch(`${API_URL}/documents/${documentId}`, {
    method: "DELETE",
    headers: getAuthHeaders(),
  });

  return response.json();
}