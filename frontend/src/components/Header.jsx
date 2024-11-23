import React from 'react';
import { Grid } from '@mui/material';
import '../style/header.css';

const Header = ({ logo}) => {
  return (
    <Grid container item xs={12} className="grid-header">
      <Grid item xs={1}>
          <a href={"/"}><img src={logo} className="nav-logo" alt="Logo"/></a>
      </Grid>
    </Grid>
  );
};

export default Header;