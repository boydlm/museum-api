import React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';
import IconButton from '@mui/material/IconButton';
import Collapse from '@mui/material/Collapse';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
  duration: theme.transitions.duration.shortest,
  }),
}));

export default function ExhibitionCard({ exhibition }) {
  const [expanded, setExpanded] = React.useState(false);
  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
  console.log(exhibition)
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        sx={{ height: 250 }}
        image={exhibition.imageUrl ? exhibition.imageUrl : `https://picsum.photos/seed/${Math.random()}/200/300`}
        title={exhibition.title}
      />
      <CardContent>
        <Button href={exhibition.websiteUrl} size="small">website</Button>
      </CardContent>
      <CardContent gutterBottom variant="h6" component="div" style={{ height: 45 }}>
        <Typography sx={{ fontSize: 'h6.fontSize' }}>
          {exhibition.title}
        </Typography>
      </CardContent>
      <CardActions>
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <KeyboardArrowDownIcon />
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          <Typography variant="body2" color="text.secondary">
            {exhibition.description ? exhibition.description : "No details available. Click website link."}
          </Typography>
        </CardContent>
      </Collapse>
    </Card>
  );
}