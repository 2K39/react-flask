import React from "react";
import Circle from './Circle.js'
import './styles/nav.css'

function Nav(props){

 return ( 
  <nav className='nav'>
  <Circle src={props.logo} size='100px' />
    <ul>   
      {props.nav.map(i =><a href={i.link}> <li>{i.name}</li></a>)} 
    </ul>
  </nav>
);
} 

export default Nav;