import { DeleteOutlined } from "@ant-design/icons";
import { Popconfirm, message } from "antd";

const getColumns = (setDataSource) => {
  const w = 120;

  const deleteRow = (key) => {
    setDataSource((prev) => prev.filter((item) => item.key !== key));
    message.success("Linha apagada com sucesso!");
  };

  return [
    {
      title: "",
      dataIndex: "",
      key: "x",
      width: 100,
      render: (_, record) => (
        <Popconfirm
          title="Confirma exclusão?"
          onConfirm={() => deleteRow(record.key)}
          okText="Sim"
          cancelText="Não"
          onCancel={() => console.log(record.key, "Cancelado")}
          style={{
            top: 100,
            borderRadius: "10px",
            padding: "20px",
            fontFamily: "Inter, sans-serif",
          }}
          okButtonProps={{
            style: {
              backgroundColor: "#626f47",
              color: "white",
              fontFamily: "Inter, sans-serif",
            },
          }}
          cancelButtonProps={{
            style: {
              fontFamily: "Inter, sans-serif",
            },
          }}
        >
          <DeleteOutlined
            style={{
              backgroundColor: "transparent",
              border: "None",
              padding: "0.2rem",
              fontSize: "20px",
            }}
            className="custom-btn"
          />
        </Popconfirm>
      ),
    },
    {
      title: "patplaqueta",
      dataIndex: "patplaqueta",
      key: "patplaqueta",
      width: w,
    },
    { title: "Status", dataIndex: "status", key: "status", width: 100 },
    {
      title: "Organograma Name",
      dataIndex: "organograma_name",
      key: "organograma_name",
      width: w,
    },
    {
      title: "Material ID",
      dataIndex: "material_id",
      key: "material_id",
      width: w,
    },
    {
      title: "Material Name",
      dataIndex: "material_name",
      key: "material_name",
      width: w,
    },
    {
      title: "Nota Fiscal",
      dataIndex: "nota_fiscal",
      key: "nota_fiscal",
      width: w,
    },
    {
      title: "Série Nota Fiscal",
      dataIndex: "serie_nota_fiscal",
      key: "serie_nota_fiscal",
      width: w,
    },
    {
      title: "Incluído Por",
      dataIndex: "incluido_por",
      key: "incluido_por",
      width: w,
    },
    {
      title: "Incluído Em",
      dataIndex: "incluido_em",
      key: "incluido_em",
      width: w,
    },
    {
      title: "Modificado Por",
      dataIndex: "modificado_por",
      key: "modificado_por",
      width: w,
    },
    {
      title: "Última Modificação",
      dataIndex: "ultima_modificacao",
      key: "ultima_modificacao",
      width: w,
    },
  ];
};

export default getColumns;
