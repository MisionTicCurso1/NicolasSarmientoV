import React, { useEffect, useState } from 'react'
import Lista from '../content/Lista'



export default function ViewEjercicio3() {
    const [data,setData]=useState([])

    useEffect(function () {
        fetch('https://myheroacademiaapi.com/api/character?page=10', { method: 'GET' })
            .then((ans) => {
                return ans.json()
            }).then((data) => {
                console.log(data.result)
                setData(data.result)
            })
            .catch((err => { console.log(err) }))
    }, [])

    

    return (
        <div>
            {data.map((data) => (
                <Lista key={data.id} image={data.images[0]} id={data.id} name={data.name}/>
                
            ))}
        </div>
    )
}
