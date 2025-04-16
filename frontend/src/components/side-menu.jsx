import "../index.css";
import "./side-menu.css";

import { AiOutlineRight } from "react-icons/ai";
import FormLogin from "./login-form/login-form";

export default function SideMenu({ onSubmit }) {
  return (
    <>
      <details className="dropdown">
        <summary>
          <span className="arrow-wrapper">
            <AiOutlineRight className="arrow-icon" />
          </span>
        </summary>
        <FormLogin onSubmit={onSubmit} />
      </details>
    </>
  );
}
