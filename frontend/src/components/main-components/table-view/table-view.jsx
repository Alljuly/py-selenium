import React from "react";

import { Table, Button, Popconfirm, message } from "antd";

import "./table-view.css";
import "../../../App.css";
import "../../../index.css";
import columns from "./table-columns";  

export default function TableView({ dataSource, setDataSource }) {

  return (
    <Table
      dataSource={dataSource}
      pagination={false}
      columns={columns}
      scroll={{ y: 240 }}
    />
  );
}
