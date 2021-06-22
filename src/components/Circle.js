import React from "react"

function Circle(props){
    let size = props.size

    let wrapper = {
        width:size,
        height:size,
        borderRadius:'100%',      
        overflow:'hidden'
        }

    let img = {
        width:size,
        height:size,
    }

    return(
        <div style={wrapper}>
            <img src={props.src} style={img}/>
        </div>
    )
}

Circle.defaultProps = { size:'200px' }

export default Circle