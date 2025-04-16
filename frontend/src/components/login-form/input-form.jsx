import "./style-form.css";

export default function FormInput(props) {
  const {
    placeholder,
    checked,
    name,
    className,
    type,
    id,
    value,
    onChange,
    required,
  } = props;

  const inputProps = {
    placeholder,
    className,
    type,
    name,
    id,
    value,
    onChange,
    required,
  };

  if (type === "checkbox" || type === "radio") {
    inputProps.checked = checked;
  }

  return <input {...inputProps} />;
}
