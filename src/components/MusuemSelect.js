import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

export default function MuseumSelect({onSelect}) {
  const [museum, setSelectedMuseum] = React.useState("");

  const handleChange = (event) => {
    setSelectedMuseum(event.target.value)
    onSelect(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Museum</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={museum}
          label="Museum"
          onChange={handleChange}
        >
          <MenuItem value={"harvard"}>Harvard Museum</MenuItem>
          <MenuItem value={"chicago"}>Chicago Institute of Art</MenuItem>
          <MenuItem value={"test"}>Test Museum</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}

/*
import * as React from 'react';
import Box from '@mui/material/Box';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import NativeSelect from '@mui/material/Select';
import { useNavigate } from 'react-router-dom';

export default function MuseumSelect({ exhibitions }) {
    const [museum, setSelectedMuseum] = React.useState("");
    const navigate = useNavigate();
  
    const handleChange = (event) => {
        console.log(event)
        console.log(exhibitions)
        setSelectedMuseum(event.target.value);
        const selectedExhibition = exhibitions.find(e => e.id === event.target.value);
        if (selectedExhibition) {
          navigate(`/${selectedExhibition.id}`);
        }
      };
  
    return (
      <Box sx={{ minWidth: 520 }}>
        <FormControl fullWidth>
          <InputLabel id="museum-select-label">Museum</InputLabel>
          <NativeSelect
            labelId="museum-select-label"
            id="museum-select-label"
            value={museum}
            label="Museum"
            onChange={handleChange}
          >
            <MenuItem value={10}>Chicago</MenuItem>
            <MenuItem value={20}>Harvard</MenuItem>
            <MenuItem value={30}>Test</MenuItem>
          </NativeSelect>
        </FormControl>
      </Box>
    );
  }*/