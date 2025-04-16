import FormInput from "./input-form";
import { useRef, useState } from "react";
import "./style-form.css";

export default function FormLogin({ onSubmit }) {
  const formRef = useRef();
  const [inputs, setInputs] = useState({ username: "", password: "" });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputs((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const form = formRef.current;
    const formData = new FormData(form);

    const username = formData.get("username");
    const password = formData.get("password");

    if (onSubmit) {
      onSubmit(username, password);
    }
  };

  return (
    <form ref={formRef} onSubmit={handleSubmit}>
      <FormInput
        placeholder="usuario"
        className="login-form-input"
        type="text"
        name="username"
        id="username"
        value={inputs.username}
        onChange={handleChange}
      />
      <FormInput
        placeholder="senha"
        className="login-form-input"
        type="password"
        name="password"
        id="password"
        value={inputs.password}
        onChange={handleChange}
      />

      <button className="form-button" type="submit">
        Acessar
      </button>
    </form>
  );
}
