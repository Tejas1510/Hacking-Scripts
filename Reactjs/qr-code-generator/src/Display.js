import "./Display.css";
import DownloadLink from "react-download-link";

const Display = ({link}) => {

  return (
    <div className="qr-display">
      <div className="card">
        <img src={link} className="card-img-top"/>
      </div>
    </div>
  );
};

export default Display;
