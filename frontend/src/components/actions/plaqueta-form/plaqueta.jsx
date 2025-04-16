import FormInput from "../../login-form/input-form";
import "./plaqueta.css";
import { useState } from "react";

export default function PlaquetaForm({ onAddPlaquetas }) {
  const [sequencia, setSequencia] = useState(false);

  const handleCheckboxChange = (e) => {
    setSequencia(e.target.checked);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const form = new FormData(e.target);
    const init = parseInt(form.get("plaqueta-init"));
    const final = parseInt(form.get("plaqueta-final"));

    if (isNaN(init)) return;

    console.log(sequencia);
    if (sequencia) {
      if (isNaN(final) || final < init) return;
      const novaSequencia = [];
      for (let i = init; i <= final; i++) {
        novaSequencia.push(i.toString());
      }
      onAddPlaquetas(novaSequencia);
    } else {
      onAddPlaquetas([init.toString()]);
    }

    setTimeout(() => e.target.reset(), 0);
  };

  return (
    <form className="plaqueta-form" onSubmit={handleSubmit}>
      <FormInput
        placeholder="999999"
        className="action-form-input"
        type="number"
        name="plaqueta-init"
        id="plaqueta-init"
        required={true}
      />
      {sequencia && (
        <FormInput
          placeholder="999999"
          className="action-form-input"
          type="text"
          name="plaqueta-final"
          id="plaqueta-final"
          required
        />
      )}
      <button className="action-form-button" type="submit">
        Adicionar
      </button>

      <div className="sequencia-wrapper">
        <FormInput
          className="sequencia-form-input"
          type="checkbox"
          name="modo"
          checked={sequencia}
          id="sequencia"
          onChange={handleCheckboxChange}
          required={false}
        />
        <label htmlFor="sequencia">sequência</label>
      </div>
    </form>
  );
}
