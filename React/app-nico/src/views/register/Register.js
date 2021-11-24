import React from 'react'
import {Link} from "@reach/router"
import Form from "../../content/form"


export default function DashBoard() {
    return (
        <div>
            <p>Registrate</p>
            <Form/>
            <br/>
            <Link to="/dashboard">Ir a Dashboard</Link>
            <br/>
            <Link to="/Ejercicio-Peliculas">Ejercicio3</Link>
        </div>
    )
}
