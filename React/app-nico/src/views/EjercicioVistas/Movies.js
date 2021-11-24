import React from 'react'
import {AllResults, NewMovies, TrendMovies, 
DramaMovies, RecomendMovies} from "./data/data"

export default function Movies({id}) {
    switch (id) {
        case 1:
            return (
                <div className='board'>
                    {AllResults.map((movie)=>(
                        <div id={movie.id} className='object'>
                            <div className='info'>
                                <h1>{movie.name}</h1>
                            </div>
                            <img src={movie.image} className='posters'/>
                         </div>
                    ))}
                </div>
            )
        case 2:
            return (
                <div className='board'>
                    {NewMovies.map((movie)=>(
                        <div id={movie.id} className='object'>
                            <div className='info'>
                                <h1>{movie.name}</h1>
                            </div>
                            <img src={movie.image} className='posters'/>
                        </div>
                    ))}
                </div>
            )
        case 3:
            return (
                <div className='board'>
                    {TrendMovies.map((movie)=>(
                        <div id={movie.id} className='object'>
                            <div className='info'>
                                <h1>{movie.name}</h1>
                            </div>
                            <img src={movie.image} className='posters'/>
                        </div>
                    ))}
                </div>
            )
        
        case 4:
            return (
                <div className='board'>
                    {DramaMovies.map((movie)=>(
                        <div id={movie.id} className='object'>
                            <div className='info'>
                                <h1>{movie.name}</h1>
                            </div>
                            <img src={movie.image} className='posters'/>
                        </div>
                    ))}
                </div>
            )
        
        case 5:
            return (
                <div className='board'>
                    {RecomendMovies.map((movie)=>(
                        <div id={movie.id} className='object'>
                            <div className='info'>
                                <h1>{movie.name}</h1>
                            </div>
                            <img src={movie.image} className='posters'/>
                        </div>
                    ))}
                </div>
            )

        default:
            return(
                <div/>
            )
    }
}
