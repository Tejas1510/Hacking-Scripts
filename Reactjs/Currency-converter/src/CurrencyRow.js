
import React from 'react'
import { makeStyles, withStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import NativeSelect from '@material-ui/core/NativeSelect';
import InputBase from '@material-ui/core/InputBase';
import { TextField } from '@material-ui/core';

const BootstrapInput = withStyles((theme) => ({
  root: {
    'label + &': {
      marginTop: theme.spacing(3),
    },
  },
  input: {
    borderRadius: 4,
    position: 'relative',
    backgroundColor: theme.palette.background.paper,
    border: '1px solid #ced4da',
    fontSize: 16,
    padding: '10px 26px 10px 12px',
    transition: theme.transitions.create(['border-color', 'box-shadow']),
    // Use the system font instead of the default Roboto font.
    fontFamily: [
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif',
      '"Apple Color Emoji"',
      '"Segoe UI Emoji"',
      '"Segoe UI Symbol"',
    ].join(','),
    '&:focus': {
      borderRadius: 4,
      borderColor: '#80bdff',
      boxShadow: '0 0 0 0.2rem rgba(0,123,255,.25)',
    },
  },
}))(InputBase);

const useStyles = makeStyles((theme) => ({
  margin: {
    margin: theme.spacing(1),
  },
}));

export default function CurrencyRow(props) {

  const {
        currencyOptions,
        selectedCurrency,
        onChangeCurrency,
        onChangeAmount,
        amount
      } = props

  const classes = useStyles();
  const [age, setAge] = React.useState('');
  const handleChange = (event) => {
    setAge(event.target.value);
  };
  return (
    <div className="currencyrow">
     
         <TextField id="standard-basic" label="Amount" 
          type="number" 
        value={amount}
         onChange={onChangeAmount} />
        
      
      <FormControl className={classes.margin}>
        <InputLabel htmlFor="demo-customized-select-native">Country</InputLabel>
        <NativeSelect
          id="demo-customized-select-native"
          
          value={selectedCurrency} onChange={onChangeCurrency}
          input={<BootstrapInput />}
        >
          {currencyOptions.map(option => (
          <option key={option} value={option}>{option}</option>
        ))}
        </NativeSelect>
      </FormControl>
    </div>
  );
}


  {/* <input type="number" className="input" value={amount} onChange={onChangeAmount} /> */}
 {/* <select value={selectedCurrency} onChange={onChangeCurrency}>
        {currencyOptions.map(option => (
          <option key={option} value={option}>{option}</option>
        ))}
      </select> */}

      // export default function CurrencyRow(props) {
      //   const {
      //     currencyOptions,
      //     selectedCurrency,
      //     onChangeCurrency,
      //     onChangeAmount,
      //     amount
      //   } = props