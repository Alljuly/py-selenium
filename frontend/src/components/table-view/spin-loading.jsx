import React from "react";
import { LoadingOutlined } from "@ant-design/icons";
import { Spin } from "antd";

export default function SpinLoading() {
  return <Spin indicator={<LoadingOutlined spin />} size="large" />;
}
