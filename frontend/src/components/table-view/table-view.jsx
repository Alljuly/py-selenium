import React from "react";

import { Table } from "antd";

import "./table-view.css";
import "../../App.css";
import "../../index.css";
export default function TableView({ dataSource }) {
  const w = 120;
  const h = 50;
  const columns = [
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

  console.log(dataSource);

  return (
    <Table
      dataSource={dataSource}
      pagination={false}
      columns={columns}
      scroll={{ y: 240 }}
    />
  );
}
