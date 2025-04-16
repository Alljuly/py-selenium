import React from "react";

import { Table, Button, Popconfirm, message } from "antd";

import "./table-view.css";
import "../../../App.css";
import "../../../index.css";

export default function TableView({ dataSource, setDataSource }) {
  const w = 120;

  const deleteRow = (key) => {
    setDataSource((prev) => prev.filter((item) => item.key !== key));
    message.success("Linha apagada com sucesso!");
  };

  const columns = [
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
          onCancel={() => console.log("Cancelado")}
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
          <Button
            style={{
              backgroundColor: "transparent",
              border: "1px solid transparent",
              fontSize: "10px",
              padding: "0.2rem",
            }}
            className="custom-btn"
          >
            Apagar
          </Button>
        </Popconfirm>
      ),
    },
    {
      title: "Patplaqueta",
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

  return (
    <Table
      dataSource={dataSource}
      pagination={false}
      columns={columns}
      scroll={{ y: 240 }}
    />
  );
}
