import React, { Fragment, useEffect, useState } from "react";


//Styled Component
import { List, ItemList } from "./styles/styles";


export default function Stories(){

  const [showFixed, setShowFixed] = useState(false)

  useEffect(() => {
    const onScroll = e =>{
      const newShowFixed = window.scrollY;
      showFixed !== newShowFixed && setShowFixed(newShowFixed)
    }
    
    document.addEventListener('scroll', onScroll)

    return () => document.removeEventListener('scroll', onScroll)
  })


  const renderList = (fixed) => (
    <List fixed = {fixed}>
     
        <ItemList>
          <div> Hola</div>
        </ItemList>
      )
    </List>
  );

  return( <Fragment>
    {renderList()}
    {renderList(true) }
  </Fragment>);
};
