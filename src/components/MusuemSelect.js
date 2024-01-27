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
    <Box sx={{ p: 3 }}>
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