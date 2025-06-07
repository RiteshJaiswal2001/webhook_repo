import React, { useEffect, useState } from "react";
import { fetchEvents } from "../api";

const EventsTable = () => {
  const [events, setEvents] = useState([]);

  const loadEvents = async () => {
    const data = await fetchEvents();
    setEvents(data);
  };

  useEffect(() => {
    loadEvents();
    const interval = setInterval(loadEvents, 15000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">GitHub Events</h1>
      <table className="w-full border border-gray-300">
        <thead>
          <tr className="bg-gray-100">
            <th>Author</th>
            <th>Action</th>
            <th>From</th>
            <th>To</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          {events.map((e, i) => (
            <tr key={i} className="text-center">
              <td>{e.author}</td>
              <td>{e.action}</td>
              <td>{e.from_branch}</td>
              <td>{e.to_branch}</td>
              <td>{new Date(e.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EventsTable;
