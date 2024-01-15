import React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function ExhibitionCard({exhibition}) {
  console.log(exhibition)
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        sx={{ height: 140 }}
        image={exhibition.imageUrl ? exhibition.imageUrl : "https://picsum.photos/200/300"}
        title= {exhibition.title}
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {exhibition.title}
        </Typography>
        <Typography variant="body2" color="text.secondary">
         {exhibition.description}
        </Typography>
      </CardContent>
      <CardActions>
        <Button href={exhibition.websiteUrl} size="small">website</Button>
      </CardActions>
    </Card>
  );
}