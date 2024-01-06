import React, { useState, useEffect } from 'react';
import './App.css';
import { Link } from '@mui/material';

function App() {
  const [exhibitions, setExhibitions] = useState([]);

  useEffect(() => {
    fetch('/exhibitions/harvard').then(res => res.json()).then(data => {
      setExhibitions(data.records);
      console.log(data)
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        {exhibitions.map((exhibition) => (
          <Link href={exhibition.url}> {exhibition.title} </Link>  
  ))}
       
      </header>
    </div>
  );
}

export default App;
