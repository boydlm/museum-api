import React, { useState, useEffect } from 'react';
import ExhibitionCard from './ExhibitionCard';
import { Grid } from '@mui/material';

export default function ExhibitionViewer({ museum }) {
  const [exhibitions, setExhibitions] = useState([]);

  useEffect(() => {
    if (museum) {
      console.log("I am in the if statement")
      fetch(`/exhibitions/${museum}`)
        .then(res => res.json())
        .then(data => setExhibitions(data))
    } 
  }, [museum]);

  const exhibitionList = exhibitions.map((exhibition) =>
    <ExhibitionCard
      exhibition={exhibition}
    />);
  return (
    <Grid>
      {exhibitionList}
    </Grid>
  );
}