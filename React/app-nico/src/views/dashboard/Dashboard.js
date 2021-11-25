import React,{Fragment} from 'react'
import {Link} from "@reach/router"
import Lista from "../../content/Lista"
import Imagen from "../../Assets/img1.jpg"

import "./imgstyles.css"

var word= "Cualquier palabra"
const objecto=[{nomb:word, imagen: Imagen, city:'Tokyo'},
    {nomb:word, imagen: Imagen,city:'Tunja'},
    {nomb:word, imagen: Imagen,city:'Bogota'},
    {nomb:word, imagen: Imagen,city:'Manizales'},
    {nomb:word, imagen: Imagen, city:'Pereira'},
    {nomb:word, imagen: Imagen, city:'Buenos aires'}]

export default function DashBoard() {
    return (
        <div>
            <p>DashBoard</p>
            <br/>
            <div className='Container'>
                {objecto.map((dato)=>(
                <Lista datos={dato}/>
                ))}
            </div>
            
        </div>
    )
}
