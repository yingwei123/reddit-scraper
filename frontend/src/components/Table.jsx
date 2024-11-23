import  React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

const TableDisplay = ({rows}) => {
    return (
    <TableContainer component={Paper} className='table-container'>
      <Table aria-label="simple table" className='table'>
        <TableHead>
          <TableRow>
            <TableCell align="center" sx={{fontWeight: 'bold'}}>Author</TableCell>
            <TableCell align="center" sx={{fontWeight: 'bold'}}>Body</TableCell>
            <TableCell align="center" sx={{fontWeight: 'bold'}}>Created At</TableCell>
            <TableCell align="center" sx={{fontWeight: 'bold'}}>ID</TableCell>
            <TableCell align="center" sx={{fontWeight: 'bold'}}>Parent ID</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row, i) => (
            <TableRow
              key={i}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row" sx={{ width: '10%' }} align="center">{row.author} </TableCell>
              <TableCell sx={{ width: '60%' }} align="center">{row.body}</TableCell>
              <TableCell sx={{ width: '10%' }} align="center">{row.created_utc}</TableCell>
              <TableCell sx={{ width: '10%' }} align="center">{row.id}</TableCell>
              <TableCell sx={{ width: '10%' }} align="center">{row.parent_id}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default TableDisplay