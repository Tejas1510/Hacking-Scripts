import {useState} from "react";

import "./SearchBox.css";
import Display from "./Display";

const SearchBox = () => {
  const [Text, setText] = useState("");
  const [Link, setLink] = useState("");

  const clicked = (e) => {
    if (Text === "") {
      alert("Please enter some content");
      return;
    } else {
      setLink("https://api.qrserver.com/v1/create-qr-code/?data=" + Text);
    }
  };

  return (
    <div className="search">
      <label htmlFor="basic-url" className="form-label">
        Enter the content for the QR
      </label>
      <div className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          id="basic-url"
          aria-describedby="basic-addon3"
          onChange={(e) => {
            setText(e.target.value);
          }}
        />
      </div>

      <button type="button" className="btn btn-success" onClick={clicked}>
        Generate
      </button>

      <Display id="qr" link={Link} />
    </div>
  );
};

export default SearchBox;
