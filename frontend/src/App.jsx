import "./index.css";
import "./App.css";
import SideMenu from "./components/side-menu";
import EjadeDashboard from "./components/dashboard-content/ejade-dashboard";
import { useState } from "react";
import axios from "axios";


function App() {
  const [userIsLogged, setUserIsLogged] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleLogin = async (username, password) => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/login", {
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
