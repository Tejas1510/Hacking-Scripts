import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './style.css';

// Sub components
import Backdrop from '../../atoms/Backdrop';
import {
  MdExpandMore as AngleDown,
  MdExpandLess as AngleUp
} from 'react-icons/md';
import Button from '../../atoms/Button';

const MenuList = ({ open, items, onSelect }) => {
  return open ? (
    <ul className="Menu__List">
      {items.map((item, i) => (
        <li
          key={`${item}_${i}`}
          onClick={(evt) => {
            onSelect(evt, item);
          }}
          className="Menu__Item"
        >
          {item}
        </li>
      ))}
    </ul>
  ) : null;
};

class Menu extends Component {
  state = {
    open: this.props.open || false
  };

  close = (evt) => {
    evt.preventDefault();
    this.setState({ open: false });
  };

  toggle = (evt) => {
    evt.preventDefault();
    this.setState((prevState) => ({ open: !prevState.open }));
  };

  render() {
    const {
      className,
      selected,
      onSelect,
      placeholder,
      items,
      noDropIcon
    } = this.props;

    return (
      <div>
        <Backdrop show={this.state.open} onClick={this.close} />
        <div className={`Menu ${className}`}>
          <header className="Menu__Header">
            {noDropIcon ? (
              <Button
                onClick={this.toggle}
                notCased
                className={selected ? null : 'Menu__Placeholder'}
              >
                {selected ? selected : placeholder}
              </Button>
            ) : (
              <div
                className={
                  selected ? 'Menu__SelectedItem' : 'Menu__Placeholder'
                }
              >
                {selected ? selected : placeholder}
              </div>
            )}
            {noDropIcon ? null : (
              <Button
                icon={this.state.open ? AngleUp : AngleDown}
                onClick={this.toggle}
              />
            )}
          </header>
          <MenuList
            open={this.state.open}
            items={items}
            onSelect={(evt, item) => {
              onSelect(item);
              this.close(evt);
            }}
          />
        </div>
      </div>
    );
  }
}

Menu.propTypes = {
  className: PropTypes.string,
  selected: PropTypes.string,
  onSelect: PropTypes.func,
  placeholder: PropTypes.string,
  items: PropTypes.arrayOf(PropTypes.string),
  noDropIcon: PropTypes.bool
};

export default Menu;
