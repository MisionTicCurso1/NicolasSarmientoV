import React from "react";

export default function Lista_likes({datos}){
    return(
        <div>
            <img src={datos.imagen} className='post'/>
            <p> <i> "j" </i> {datos.likes}</p>
        </div>
    )
}