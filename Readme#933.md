# Expense Tracker

## Introduction
```
This application is developed to track the expenses the user makes. The changes that have been implemented in this PR is to add charts functionality that will show the user the graph of savings and expenses that have been made.
```

## Third party NPM libraries
```
Recharts
```

## How to install the library
```
npm i recharts
```

## How to use it
The main purpose of this library is to help you to write charts in React applications without any pain. Main principles of Recharts are:

1. Simply deploy with React components.
2. Native SVG support, lightweight depending only on some D3 submodules.
3. Declarative components, components of charts are purely presentational.
 
### Example

 ```
 <LineChart
  width={400}
  height={400}
  data={data}
  margin={{ top: 5, right: 20, left: 10, bottom: 5 }}
>
  <XAxis dataKey="name" />
  <Tooltip />
  <CartesianGrid stroke="#f5f5f5" />
  <Line type="monotone" dataKey="uv" stroke="#ff7300" yAxisId={0} />
  <Line type="monotone" dataKey="pv" stroke="#387908" yAxisId={1} />
</LineChart>
```

