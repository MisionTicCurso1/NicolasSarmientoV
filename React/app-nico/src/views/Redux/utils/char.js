class DataCaracteres {
    async getCaracteres() {
      const consulta = await fetch("https://rickandmortyapi.com/api/character", {
        method: "GET",
      });
  
      const personajes = await consulta.json()
      return personajes
    }
  }
  
  export default new DataCaracteres