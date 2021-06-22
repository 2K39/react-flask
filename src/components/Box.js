import React from "react"
import Circle from "./Circle.js"

function Box(props) {
    let flexDirection
    let size = 200 + 'px'

    if(props.reverse == 'true'){
        flexDirection = 'row-reverse'
    }
    else{
        flexDirection = 'none'
    }

    let box = {
        width:'80%',
        height:'300px' ,
        display:'flex',
        alignItems:'center',
        justifyContent:"space-around",
        borderRadius:'30px',
        backgroundColor:'#ebebeb',
        flexDirection: flexDirection,
        fontSize:'30px',
        margin:'30px'
    }

    let text = {
        width:'60%'
    }

    return(
        <div style={box}>

            <Circle src={props.src} />

            <div style={text}>
            {props.text}
            </div>
        </div>
        )
}

Box.defaultProps = {text:""}
export default Box