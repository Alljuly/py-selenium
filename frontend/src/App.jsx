import "./index.css";
import "./App.css";
import SideMenu from "./components/side-menu";
import EjadeDashboard from "./components/main-components/dashboard/ejade-dashboard";
import { useState } from "react";
import axios from "axios";

function App() {
  const apiUrl = "http://127.0.0.1:5000" || import.meta.env.VITE_API_URL;

  const [userIsLogged, setUserIsLogged] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleLogin = async (username, password) => {
    setLoading(true);
    try {
      await axios.post(apiUrl + "/login", {
        username,
        password,
      });
      setUserIsLogged(true);
      setLoading(false);
    } catch (error) {
      if (error.response) {
        console.error("Erro no login:", error.response.data);
      } else {
        console.error("Erro de conexão:", error.message);
      }
      setUserIsLogged(false);
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <SideMenu onSubmit={handleLogin} />
      <EjadeDashboard isLogged={userIsLogged} loading={loading} />
    </div>
  );
}

export default App;
