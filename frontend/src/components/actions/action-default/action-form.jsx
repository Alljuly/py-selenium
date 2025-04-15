import FormInput from "../../form-login/form-input";
import "./action-form.css";
import { useState } from "react";

export default function ActionForm(props) {
  const { id, text, typeInput, onClick, placeholder, name, value } = props;
  const [inputValue, setInputValue] = useState(value || "");

  const handleChange = (e) => {
    const { value } = e.target;
    setInputValue(value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (onClick) {
      onClick(inputValue);
    }
  };

  return (
    <form className="action-form" onSubmit={handleSubmit}>
      <FormInput
        placeholder={placeholder}
        className="action-form-input"
        type={typeInput}
        name={name}
        id={id}
        value={inputValue}
        onChange={handleChange}
      />
      <button className="action-form-button" type="submit">
        {text}
      </button>
    </form>
  );
}
