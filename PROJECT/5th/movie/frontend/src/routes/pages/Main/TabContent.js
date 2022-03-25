import React, {useEffect, useState} from 'react';
import { Link, useHistory } from 'react-router-dom';


function TabContent(props){
    const movies = props.movies

    let [genre, genreChange]=useState(['공연실황', '드라마', '다큐멘터리', '애니메이션', '모험', '액션', 'SF', '멜로/로맨스', '전쟁', '범죄', '판타지', '서부', '한국', '뮤지컬', '공포', '미스터리', '스릴러' , '서스펜스', '느와르', '서사'])
    const changeCate=( name )=>{
        if( name === '공연실황') return 1
        else if( name === '드라마') return 2
        else if( name === '다큐멘터리') return 3
        else if( name === '애니메이션') return 4
        else if( name === '모험') return 5
        else if( name === '액션') return 6
        else if( name === 'SF') return 7
        else if( name === '멜로/로맨스') return 8
        else if( name === '전쟁') return 9
        else if( name === '범죄') return 10
        else if( name === '판타지') return 11
        else if( name === '가족') return 12
        else if( name === '코미디') return 13
        else if( name === '서부') return 14
        else if( name === '한국') return 15
        else if( name === '뮤지컬') return 16
        else if( name === '공포') return 17
        else if( name === '미스터리') return 18
        else if( name === '스릴러') return 19
        else if( name === '서스펜스') return 20
        else if( name === '느와르') return 21
        else if( name === '서사') return 22
    }
    const [clickValue, setClickValue] = useState()
    const FindClickValue = (e,i) =>{
        setClickValue(changeCate(i))
    }

    const movieFilter = (movie) => {
        console.log(movie)
        const filterMovie = movie.filter((item)=>(item.movie_genre == clickValue))
        return filterMovie
    }

    useEffect(()=>{
        props.changeSwtich(true);
        
    })

    if(props.tab===1){
        return (<div className='row'>
                <div className='movieposter'>
                {movies.map((movie,i)=>{
                    return(
                        <Link to={'/detail'}><img className='img-responsive2' src={movie.movie_poster} art="" /></Link>
                    )
                }) }
                </div>
            </div>)
    }
    else if(props.tab===0){
        return (<div>
            <nav defaultActiveKey="action">
                <ul className='genresearch'>
                    {
                        genre.map(function(i){
                            return <li onClick={(e)=>{FindClickValue(e,i)}}>{i}</li>
                        })
                    }
                </ul>
            </nav>
            <div className='movieposter'>
            {movieFilter(movies).map((a,i)=>{
                return(
                    <Link to={'/detail/'+i}><img className='img-responsive2' src={a.movie_poster} alt="" /></Link>
                )
            })}
            </div>
            
        </div>)
    }
    
 
}

export default TabContent