import "../../index.css";

import "./ejade-dashboard.css";
import { LoadingOutlined } from "@ant-design/icons";
import { Spin } from "antd";

import EjadeWorkspace from "./ejade-workspace";
import LoginReminder from "../login-reminder";

export default function EjadeDashboard(props) {
  const { isLogged, loading } = props;

  return (
    <main>
      {loading ? (
        <Spin indicator={<LoadingOutlined spin />} size="large" />
      ) : (
        <div className="dashboard-content">
          {isLogged ? <EjadeWorkspace /> : <LoginReminder />}
        </div>
      )}
    </main>
  );
}
