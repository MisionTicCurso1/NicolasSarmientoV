import React, { Fragment, useEffect, useState } from "react";
import { connect } from "react-redux";

import ItemTaller from "../components/ItemTaller";

import { getCaracteres } from "../actions/dataAction";

function DatosTaller({
  getCaracteres,
  dataLoading,
  dataSuccess,
  dataError,
  ...props
}) {
  useEffect(() => {
    getCaracteres();
  }, []);

  console.log("Este es el estado de carga: ", dataLoading);
  console.log("Este es el estado de success: ", dataSuccess);
  console.log("Este es el estado de error: ", dataError);
  return (
    <Fragment>
      {dataSuccess.map((personajes) => (
        <ItemTaller
          key={personajes.id}
          name={personajes.name}
          image={personajes.image}
          id={personajes.id}
        />
      ))}
    </Fragment>
  );
}

const mapStateToProps = ({
  personajes: { dataLoading, dataSuccess, dataError },
}) => {
  return {
    dataLoading,
    dataSuccess,
    dataError,
  };
};

export default connect(mapStateToProps, { getCaracteres })(DatosTaller);