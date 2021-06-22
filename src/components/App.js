import React from "react";
import Nav from './Nav.js';
import Box from "./Box.js";
import cat from './media/cat.jpg';
import logo from './media/logo.jpg'
import './styles/Style.css'

function App(){
  let nav = [
    {name:'yahoo' , site:"https://www.google.com.sa/"},
    {name:'home' , site:'https://www.google.com/'}
  ]
  let gitLogo = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png'

  return(
     <div className='column'>
        <Nav logo={logo} nav={nav}/>
        <Box text='ipsom lorem' src={cat} reverse='true'/>
        <Box src={gitLogo}/>
    </div>
)}

export default App;