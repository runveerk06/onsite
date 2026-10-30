import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

type Worker = {
  id: number;
  full_name: string;
  hourly_rate: string;
};

export default function App() {
  const [workers, setWorkers] = useState<Worker[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API_URL}/workers`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`API returned ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setWorkers(data.workers))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return (
    <main style={{ fontFamily: "system-ui, sans-serif", padding: "2rem" }}>
      <h1>OnSite</h1>
      <h2>Workers</h2>

      {loading && <p>Loading workers.</p>}
      {error && <p>Could not reach the API: {error}</p>}

      {!loading && !error && (
        <table cellPadding={8}>
          <thead>
            <tr>
              <th align="left">Name</th>
              <th align="left">Hourly rate</th>
            </tr>
          </thead>
          <tbody>
            {workers.map((worker) => (
              <tr key={worker.id}>
                <td>{worker.full_name}</td>
                <td>${worker.hourly_rate}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  );
}
