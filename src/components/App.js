import React from "react";
import Nav from './Nav.js';
import Box from "./Box.js";
import cat from './media/cat.jpg';
import logo from './media/logo.jpg'
import './styles/Style.css'

function App(){
  let nav = []

  return(
     <div className='column'>
        <Nav nav={nav} logo={cat}/>
    </div>
)}

export default App;