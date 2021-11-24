import React from "react";
import Lista_likes from "../../content/listalikes"
import Imag from "../../Assets/img-cat.jpg"
import Stories from "../../content/stories"

var data= [
    {'imagen':Imag, 'likes':2},
    {'imagen':Imag, 'likes':5},
    {'imagen':Imag, 'likes':223},
    {'imagen':Imag, 'likes':2},
    {'imagen':Imag, 'likes':4},
    {'imagen':Imag, 'likes':312},
    {'imagen':Imag, 'likes':200},
]



export default function Vista2(){
    return(
       <div className='container'>
           <Stories/>
           <br/>
           {data.map((dato)=>(
               <Lista_likes datos={dato}/>
           ))}

       </div>
    )


}

