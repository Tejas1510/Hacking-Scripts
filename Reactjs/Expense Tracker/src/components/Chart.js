import React, { useContext } from "react";
import {
  AreaChart,
  Area,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  YAxis,
} from "recharts";
import { GlobalContext } from "../context/GlobalState";

let data = [];
for (let i = 30; i >= 0; i--) {
  data.push({
    value: i,
    input: i * Math.random(),
  });
}

const Charts = (props) => {
  const { transactions } = useContext(GlobalContext);
  let transac;
  if (props.type === "p") {
    transac = transactions.filter((x) => x.amount >= 0);
  } else if (props.type === "n") {
    transac = transactions.filter((x) => x.amount < 0);
  }

  return (
    <ResponsiveContainer width="100%" height={400}>
      <AreaChart data={transac}>
        <defs>
          <linearGradient id="color" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#303841" stopOpacity={0.4} />
            <stop offset="75%" stopColor="#3A4750" stopOpacity={0.01} />
          </linearGradient>
        </defs>
        <Area dataKey="amount" stroke="#dedede" />
        <YAxis dataKey="amount" />
        <Tooltip />
        <CartesianGrid />
      </AreaChart>
    </ResponsiveContainer>
  );
};

export default Charts;
