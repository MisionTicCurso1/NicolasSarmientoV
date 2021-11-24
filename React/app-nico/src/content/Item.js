import React from "react";

//Styles, Assets
import { ImgProd, InfProd } from "./styles/styles";
//Componente nombrado, cuando lo use donde lo quiero importar debo traerlo entre {}
export const Item = ({ image, path, name = "?" }) => (
  <InfProd href={path}>
    <ImgProd src={image} />
    {name}
  </InfProd>
);
