import TableView from "../table-view/table-view";
import PlaquetaForm from "../../actions/plaqueta-form/plaqueta";
import ActionForm from "../../actions/action-form/action-form";
import "./ejade-workspace.css";
import "../../login-form/style-form.css";
import { useState, useRef, useEffect } from "react";
import axios from "axios";
import { LoadingOutlined } from "@ant-design/icons";
import { Spin } from "antd";
import Papa from "papaparse";

export default function EjadeWorkspace() {
  const [plaquetas, setPlaquetas] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("Carregar csv");
  const [apiMessage, setApiMessage] = useState("");
  const [file, setFile] = useState();

  const inputRef = useRef();

  useEffect(() => {
    console.log("use effect", plaquetas);
  }, [plaquetas]);

  const handleReset = (e) => {
    e.preventDefault();
    setPlaquetas([]);
  };

  const handleSearch = async (plaquetas) => {
    setLoading(true);
    try {
      setApiMessage("Buscando");
      const response = await axios.post("http://localhost:5000/get_items", {
        plaquetas: plaquetas,
      });
      const resultData = response.data;
      resultData != null
        ? setPlaquetas(resultData)
        : setPlaquetas([]) && setApiMessage("Nenhum resultado encontrado");
    } catch (error) {
      if (error.response) {
        console.error("Erro na busca", error.response.data);
      } else {
        console.error("Erro de conexão:", error.message);
      }
      setUserIsLogged(false);
    } finally {
      setApiMessage('')
      setLoading(false);
    }
  };

  const handleTransference = async (destination, plaquetas) => {
    try {
      setApiMessage("Criando Transferencias");
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
      console.error("Erro na busca", error.response.data);
    } finally {
      setLoading(false);
      setApiMessage('')
    }
  };

  const handleUpdateTerm = async (num_term, plaquetas) => {
    try {
      setApiMessage("Incluindo items no termo...");
      const response = await axios.post(
        "http://localhost:5000/include_terms_items",
        {
          num_termo: num_term,
          plaquetas: plaquetas,
        }
      );
      const resultData = response.data;
      resultData != null
        ? setPlaquetas([]) && setApiMessage("Finalizado")
        : console.log("verifique o termo");
    } catch (error) {
      if (error.response) {
        console.error("Erro na busca", error.response.data);
      } else {
        console.error("Erro de conexão:", error.message);
      }
      console.error("Erro na busca", error.response.data);
    } finally {
      setApiMessage('')
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

  const handleChangeInput = (e) => {
    const selectedFile = e.target.files[0];

    if (selectedFile) {
      setFile(selectedFile);
      setMessage("Arquivo Pronto");
    }
  };

  const handleUploadCSV = () => {
    if (!file) return;

    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      complete(results) {
        console.log("CSV raw:", results.data);

        const rawPlaquetas = results.data
          .map((row) => row.plaquetas && row.plaquetas.trim())
          .filter(Boolean)
          .filter((p) => /^\d+$/.test(p));

        console.log("Plaquetas filtradas:", rawPlaquetas);
        handleAddPlaquetas(rawPlaquetas);
        setMessage("Carregar csv");
      },
      error(err) {
        console.error("Erro ao ler o CSV:", err);
        setMessage("Erro ao ler o arquivo.");
      },
    });
  };

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
          <div>
            <p>{apimessage}</p>
          </div>

          <button
            className="action-view-button"
            onClick={() => handleSearch(plaquetas)}
          >
            Buscar
          </button>
          <button className="action-view-button" onClick={handleReset}>
            Limpar
          </button>
          <div className="input-file-wrapper">
            <form onSubmit={handleUploadCSV}>
              <input
                ref={inputRef}
                id="file-input"
                type="file"
                accept=".csv"
                onChange={handleChangeInput}
              />
              <label htmlFor="file-input" className="custom-upload-label">
                {message}
              </label>
            </form>
          </div>
          <button
            className="action-view-button"
            onClick={() => handleUploadCSV()}
          >
            Enviar
          </button>
        </div>
        {loading ? (
          <Spin indicator={<LoadingOutlined spin />} size="large" />
        ) : (
          <TableView dataSource={plaquetas} setDataSource={setPlaquetas} />
        )}
      </div>
    </>
  );
}
