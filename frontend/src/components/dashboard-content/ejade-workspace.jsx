import TableView from "../table-view/table-view";
import PlaquetaForm from "../actions/plaqueta";
import ActionForm from "../actions/action-default/action-form";
import "./ejade-workspace.css";
import "../form-login/form-style.css";
import { useState } from "react";
import { Spin } from "antd";
import axios from "axios";
import SpinLoading from "../table-view/spin-loading";

export default function EjadeWorkspace() {
  const [plaquetas, setPlaquetas] = useState([]);
  const [loading, setLoading] = useState(false);


  const handleReset = (e) => {
    e.preventDefault();
    setPlaquetas([]);
  };

  const handleSearch = async (plaquetas) => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/get_items", {
        plaquetas: plaquetas,
      });
      const resultData = response.data;
      resultData != null ? setPlaquetas(resultData) : setPlaquetas([]);
    } catch (error) {
      if (error.response) {
        console.error("Erro na busca", error.response.data);
      } else {
        console.error("Erro de conexão:", error.message);
      }
      setUserIsLogged(false);
    } finally {
      setLoading(false);
    }
  };

  const handleTransference = async (destination, plaquetas) => {
    try {
      const response = await axios.post(
        "http://localhost:5000/create_transference_and_update",
        {
          destination: destination,
          plaquetas: plaquetas,
        }
      );
      const resultData = response.data;
      resultData != null
        ? setPlaquetas([])
        : console.log("verifique as transferencias");
    } catch (error) {
      if (error.response) {
        console.error("Erro na busca", error.response.data);
      } else {
        console.error("Erro de conexão:", error.message);
      }
      setUserIsLogged(false);
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateTerm = async (num_term, plaquetas) => {
    try {
      const response = await axios.post(
        "http://localhost:5000/include_terms_items",
        {
          num_termo: num_term,
          plaquetas: plaquetas,
        }
      );
      const resultData = response.data;
      resultData != null
        ? setPlaquetas([])
        : console.log("verifique o termo");
    } catch (error) {
      if (error.response) {
        console.error("Erro na busca", error.response.data);
      } else {
        console.error("Erro de conexão:", error.message);
      }
      setUserIsLogged(false);
    } finally {
      setLoading(false);
    }
  };


  const handleAddPlaquetas = (novasPlaquetas) => {
    const novas = novasPlaquetas.map((p, idx) => ({
      key: String(plaquetas.length + idx + 1),
      patplaqueta: p,
      status: "",
      organograma_name: "",
      material_id: "",
      material_name: "",
      nota_fiscal: "",
      serie_nota_fiscal: "",
      incluido_por: "",
      incluido_em: "",
      modificado_por: "",
      ultima_modificacao: "",
    }));
    setPlaquetas((prev) => [...prev, ...novas]);
  };

  fetch;

  return (
    <>
      <div className="workspace-actions">
        <PlaquetaForm onAddPlaquetas={handleAddPlaquetas} />
        <ActionForm
          placeholder="ex.:4334"
          typeInput="number"
          id="transferece"
          text="Transferir"
          name="transference"
          onClick={(destination) => handleTransference(destination, plaquetas)}
        />
        <ActionForm
          typeInput="number"
          placeholder="nº termo"
          text="Preencher"
          name="termo"
          onClick={(num_term) => handleUpdateTerm(num_term, plaquetas)}
          id="termo"
        />
      </div>
      <div className="workspace-view">
        <div className="workspace-view-actions">
          <button
            className="action-view-button"
            onClick={() => handleSearch(plaquetas)}
          >
            Buscar
          </button>
          <button className="action-view-button" onClick={handleReset}>
            Limpar
          </button>
          <button className="action-view-button">Gerar CSV</button>
        </div>
        {loading ? <SpinLoading /> : <TableView dataSource={plaquetas} />}
      </div>
    </>
  );
}
