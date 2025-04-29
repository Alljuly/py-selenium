import React from "react";

import { Table } from "antd";

import "./table-view.css";
import "../../../App.css";
import "../../../index.css";
import getColumns from "./table-columns";

export default function TableView({ dataSource, setDataSource }) {
  return (
    <Table
      dataSource={dataSource}
      pagination={false}
      columns={getColumns(setDataSource)}
      scroll={{ y: 240 }}
    />
  );
}
