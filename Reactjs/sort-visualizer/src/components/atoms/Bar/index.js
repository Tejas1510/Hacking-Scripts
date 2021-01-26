import React from 'react';
import './style.css';

const Bar = ({
  width,
  height,
  val,
  stateA,
  stateB,
  stateC,
  stateD,
  sorted,
  style
}) => {
  let classNames = 'Bar';
  if (sorted) classNames += ' Bar_sorted';
  if (stateD) classNames += ' Bar_stateD';
  else if (stateC) classNames += ' Bar_stateC';
  else if (stateB) classNames += ' Bar_stateB';
  else if (stateA) classNames += ' Bar_stateA';

  let BarStyle = { ...style, width: `${width}%`, height: `${height}%` };
  if (stateA || stateB || stateC || stateD) {
    BarStyle['marginRight'] = `${0.3 * width}%`;
    BarStyle['marginLeft'] = `${0.3 * width}% `;
  }

  return (
    <div style={BarStyle} className={classNames}>
      <span className="Bar__Text">{val}</span>
    </div>
  );
};

export default Bar;
