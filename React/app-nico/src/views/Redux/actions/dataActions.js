import { type } from "./types";
import Consulta from "../utils/char";

export const getCaracteres = () => (dispatch) => {
  dispatch({ type: type.GET_DATA_LOADING });
  Consulta.getCaracteres()
    .then((informacion) => {
      if (informacion.results) {
        dispatch({
          type: type.GET_DATA_SUCCESS,
          payload: { personajes: informacion.results },
        });
      }
    })
    .catch((error) => {
      dispatch({
        type: type.GET_DATA_SUCCESS,
        payload: { error: "Ups ocurrio un problema" },
      });
    });
};