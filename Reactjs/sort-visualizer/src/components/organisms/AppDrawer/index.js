import React, { Fragment } from 'react';
import './style.css';

import Backdrop from '../../atoms/Backdrop';

const AppDrawer = ({ open, children, closeDrawer }) => {
  let className = 'AppDrawer';
  className += open ? ` AppDrawer_open` : ` AppDrawer_closed`;
  return (
    <Fragment>
      <div className={className}>
        <div className="AppDrawer__Content">{children}</div>
      </div>
      <Backdrop show={open} onClick={closeDrawer} />
    </Fragment>
  );
};

export default AppDrawer;
