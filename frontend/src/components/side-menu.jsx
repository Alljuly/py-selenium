import "../index.css";
import "../App.css";

import { AiOutlineRight } from "react-icons/ai";
import FormLogin from "./form-login/form-login";

export default function SideMenu({onSubmit}) {
  return (
    <>
      <details className="dropdown">
        <summary>
          <span className="arrow-wrapper">
            <AiOutlineRight className="arrow-icon" />
          </span>
        </summary>
        <FormLogin onSubmit={onSubmit}/>
      </details>

    </>
  );
}
