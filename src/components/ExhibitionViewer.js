import React, { useState, useEffect } from 'react';
import ExhibitionCard from './ExhibitionCard';
import { Grid, Box } from '@mui/material';

export default function ExhibitionViewer({ museum }) {

  const [exhibitions, setExhibitions] = useState([]);

  useEffect(() => {
    if (museum) {
      fetch(`/exhibitions/${museum}`)
        .then(res => res.json())
        .then(data => setExhibitions(data))
    }
  }, [museum]);

  return (
    <Box sx={{ p: 3 }}   >
      <Grid container spacing={{ xs: .5, md: 1 }} columns={{ xs: 4, sm: 8, md: 12 }}>
        {Array.from(exhibitions).map((exhibition, index) => (
          <Grid item xs={2} sm={4} md={3} key={index}>
            <ExhibitionCard
              exhibition={exhibition}
            />
          </Grid>
        ))}
      </Grid>
    </Box>

  );
}