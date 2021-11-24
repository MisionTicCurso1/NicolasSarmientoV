import React, { useRef, useEffect, useState } from "react";


export default function Lista({id, name, image}){
  const elemento = useRef(null);

  const [show, setShow] = useState(false);

  useEffect(() => {
    console.log(elemento.current);
    const observer = new window.IntersectionObserver(function (entradas) {
      // console.log(entradas)
      const { isIntersecting } = entradas[0];
      console.log(isIntersecting);
      if (isIntersecting) {
        setShow(isIntersecting);
        observer.disconnect()
      }
    });

    observer.observe(elemento.current);
  }, [elemento]);
    return(
    <div className='card' ref={elemento} >
      <img src={image} className = "img"/>
      <p>{name}</p>
      {/* <p>{datos.city}</p> */}
    </div>
    )
}