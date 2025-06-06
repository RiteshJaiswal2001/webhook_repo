const API_BASE = import.meta.env.VITE_BACKEND_URL;

export const fetchEvents = async () => {
  const response = await fetch(`${API_BASE}/events`);
  return response.json();
};
