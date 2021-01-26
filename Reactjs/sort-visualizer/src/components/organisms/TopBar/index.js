import React from 'react';
import './style.css';

import Button from '../../atoms/Button';
import { MdMenu as Hamburger, MdClose as Close } from 'react-icons/md';

const TopBar = ({ drawerOpen, toggleDrawer, children }) => {
  return (
    <header className="TopBar">
      <div className="TopBar__Row">
        <section className="TopBar__Section">
          <Button
            icon={drawerOpen ? Close : Hamburger}
            className="TopBar__MenuButton"
            iconClass="TopBar__Icon"
            onClick={toggleDrawer}
          />
          <span className="TopBar__Title">Sorting Visualizer</span>
        </section>
        <section className="TopBar__Section TopBar__Section_align_end">
          {children}
        </section>
      </div>
    </header>
  );
};

export default TopBar;
