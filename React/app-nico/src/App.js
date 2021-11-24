import {Router} from "@reach/router";
import './App.css';

import Register from "./views/register/Register";
import DashBoard from "./views/dashboard/Dashboard";
import VistaLikes from "./views/Ejercicio2/Vista2"
import ViewEjercicio3 from "./views/ViewEjercicio3";
import EjercicioVistas from "./views/EjercicioVistas/VistasEj3"

function App(){
  return (
   <Router>
     <Register path="/"/>
     <DashBoard path="/dashboard"/>
     <VistaLikes path='/Ejercicio2'/>
     <ViewEjercicio3 path='/Ejercicio3'/>
     <EjercicioVistas path='/Ejercicio-Peliculas'/>
   </Router>
  );
}

export default App;
