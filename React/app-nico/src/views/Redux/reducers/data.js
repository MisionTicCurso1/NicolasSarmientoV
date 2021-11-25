import { type } from "../actions/Types/index";

const estadoInicial = {
  dataLoading: false,
  dataSuccess: [],
  dataError: null,
};

function Data(state = estadoInicial, action) {
  switch (action.type) {
    case type.GET_DATA_LOADING: {
      return {
        ...state,
        dataLoading: true,
        dataSuccess: [],
        dataError: null,
      };
    }
    case type.GET_DATA_SUCCESS: {
      return {
        ...state,
        dataLoading: false,
        dataSuccess: action.payload.personajes,
        dataError: null,
      };
    }
    case type.GET_DATA_ERROR: {
      return {
        ...state,
        dataLoading: false,
        dataSuccess: [],
        dataError: action.payload.error,
      };
    }
    default:
      return state;
  }
}

export default Data;