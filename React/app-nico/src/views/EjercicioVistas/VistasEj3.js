import React, {useState}from 'react'
import "./Styles.css"
import {MovieCategories} from './data/data'

import Movies from './Movies'

export default function VistasEj3() {
    const [type, setType]=useState('')

    function ChoosenCategory(id) {
        setType(id)
    }

    return (
        <div>
            <div className="list">
                <ul>
                    {MovieCategories.map((item)=>(
                        <li onClick={()=>ChoosenCategory(item.id)} className={type===item.id? 'actived': ''}> {item.name}</li>
                    ))}            
        
                </ul>
            </div>
            <div className='box'>

                <Movies id={type}/>
                
            </div>
        </div>
    )
}
