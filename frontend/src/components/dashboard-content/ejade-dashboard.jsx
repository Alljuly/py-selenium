import "../../index.css";

import "./ejade-dashboard.css";

import EjadeWorkspace from "./ejade-workspace";
import LoginReminder from "../login-reminder";
import SpinLoading from "../table-view/spin-loading";

export default function EjadeDashboard(props) {
  const { isLogged, loading } = props;

  return (
    <main>
      {loading ? (
        <SpinLoading />
      ) : (
        <div className="dashboard-content">
          {isLogged ? <EjadeWorkspace /> : <LoginReminder />}
        </div>
      )}
    </main>
  );
}
