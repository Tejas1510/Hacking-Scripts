import React from 'react';
import PropTypes from 'prop-types';
import './style.css';

const ProgressBar = ({ width }) => (
  <div className="ProgressBar">
    <div
      className="ProgressBar__Active"
      style={{
        width: `${width}%`
      }}
    ></div>
  </div>
);

ProgressBar.propTypes = {
  width: PropTypes.number.isRequired
};

export default ProgressBar;
