import React from 'react'
import {Grid} from '@mui/material'
import TableDisplay from './Table'
import '../style/table.css';

const TablePage = ({rows}) => {
  return (
    <Grid container className='table-display-container'>
        <TableDisplay rows = {rows}/>
    </Grid>
  );
}

export default TablePage