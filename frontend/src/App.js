import logo from './fun_logo.png';
import {React, useState} from 'react';
import { Grid } from '@mui/material';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import './App.css';
import HomePage from './components/Homepage';
import TablePage from './components/TablePage';

function App() {
  const [rowData, setRowData] = useState([])
  console.log(rowData)
  return (
    <Router>
      <div className="App">
        <Grid container className="grid-container">
          <Grid item>
            <Header logo={logo} />
          </Grid>
          <Routes>
            <Route exact path="/" element={<HomePage setRowData={setRowData}/>} />
            <Route path="/table" element={<TablePage rows={rowData}/>} />
          </Routes>
        </Grid>
      </div>
    </Router>
  );
}

export default App;
