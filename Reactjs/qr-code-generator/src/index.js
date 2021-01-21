import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import Header from "./Header";
import SearchBox from "./SearchBox";

ReactDOM.render(
  <React.StrictMode>
    <Header />
    <SearchBox />
  </React.StrictMode>,
  document.getElementById("root")
);
