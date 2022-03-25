import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';

import { Link, useHistory, withRouter } from 'react-router-dom';
import {DropdownButton, Dropdown, Button, Card} from 'react-bootstrap';


// axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
// axios.defaults.xsrfCookieName = "XCSRF-TOKEN";
// axios.defaults.withCredentials = true

const MainPresenter = (props) => {
  let [genre, genreChange]=useState(['공연실황', '드라마', '다큐멘터리', '애니메이션', '모험', '액션', 'SF', '멜로/로맨스', '전쟁', '범죄', '판타지', '가족', '코미디', '서부', '한국', '뮤지컬', '공포', '미스터리', '스릴러' , '서스펜스', '느와르', '서사'])

    let history = useHistory();
    const [movies, setMovies] = useState([
        {
          "movie_id": 10001,
          "movie_title": "시네마 천국",
          "movie_url": "https://movie.naver.com/movie/bi/mi/basic.naver?code=10001",
          "movie_aud": 9.63,
          "movie_net": 9.33,
          "movie_rep": 8.38,
          "movie_poster": "https://movie-phinf.pstatic.net/20210409_134/16179547654813MHq5_JPEG/movie_image.jpg?type=m203_290_2",
          "movie_genre": 2,
          "movie_country": 10,
          "movie_runtime": 124,
          "movie_release": "2020-04-22",
          "movie_director": "쥬세페 토르나토레",
          "movie_age": 4,
          "movie_content": "어린 시절 영화가 세상의 전부였던 소년 토토는 학교 수업을 마치면 마을 광장에 있는 낡은 시네마 천국이라는 극장으로 달려가 영사 기사 알프레도와 친구로 지내며 어깨너머로 영사기술을 배운다. 어느 날 관객들을 위해 광장에서 야외 상영을 해주던 알프레도가 그만 화재 사고로 실명하게 되고 토토가 그의 뒤를 이어 시네마 천국의 영상기사로 일하게 된다. 실명한 후에도 토토의 친구이자 아버지로 든든한 정신적 지주가 되어준 알프레도는 청년이 된 토토가 사랑하는 여자 엘레나의 부모님의 반대로 좌절하자 넓은 세상으로 나가서 더 많은 것을 배우라며 권유하는데..."
        }
      ]);
    ;
    useEffect(() => {
        const loadMovies = async() => {
            const config = {
                headers: {
                    "content-type": "application/json"
                }
            };
            await axios.get(`/api/`, config).then((response)=>{//전체 영화데이터
                // console.log(response.data)
                setMovies(response.data)
            }); 
        }
        loadMovies();
      }, []);
    const [checkedMovie, setCheckedMovie] = useState([])
    const handleClickImage = (movie) => {
        if (checkedMovie.length < 3){
            let checked = false;
            let i = 0;
            for(i; i < checkedMovie.length; i++){
                if(checkedMovie[i].movie_id === movie.movie_id){
                    checked = true;
                    break;
                }
            }
            if(checked){
                const updateCheckedMovies = [...checkedMovie]
                updateCheckedMovies.splice(i, 1)
                setCheckedMovie(updateCheckedMovies)
            }else{
                const updateCheckedMovies = [...checkedMovie]
                updateCheckedMovies.push(movie)
                setCheckedMovie(updateCheckedMovies)
            }
        }else{
            alert('3개까지만 선택 가능합니다!')
        }
    }
    const handleClickCancle = (i) => {
        const updateCheckedMovies = [...checkedMovie]
        updateCheckedMovies.splice(i, 1)
        setCheckedMovie(updateCheckedMovies)
    }
 
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
    const [genreValue, SetGenreValue] = useState();
    
    const FindGenreValue= (e,j) =>{
        SetGenreValue(changeCate(j))
        setCheckedMovie([])
    }

    const genreFilter = (movies) =>{
        const filterGenre = movies.filter((item)=> item.movie_genre == genreValue)
        return filterGenre
    }

    const handleClickSearch = () => {
        props.history.push(`/recommend/${genreValue}/${checkedMovie[0].movie_id}/${checkedMovie[1].movie_id}/${checkedMovie[2].movie_id}/`)
    }
    
    return(
        <div className='content'>
            <div className='goBack'><img onClick={()=>{ history.goBack(); }} src="img/back.svg" alt="" /></div>
            <div className='recommendation'>
                <h1>좋아하는 콘텐츠를 3개 선택하세요!</h1>
                <p>회원님이 좋아하실 만한 영화를 더 많이 추천해드릴 수 있습니다. 마음에 드는 콘텐츠를 선택하세요.<br/><Link to={'/search'}> 알아서 볼게요!! &lt; Click</Link></p>
            </div>
            <div className='movie-list'>
                <DropdownButton id="dropdown-item-button" title={genreValue ? genre[genreValue-1] :"장르를 선택하세요"}>
                    {genre.map(function(j){
                        return <Link><Dropdown.Item onClick={(e)=>{FindGenreValue(e,j)}}>{j}</Dropdown.Item></Link>
                    })}
                </DropdownButton>
                <div className='row ml-0 mt-1 mb-1'>
                    {checkedMovie.map((movie, i) =>(                    
                        <Card style={{ width: '33.3%', display: 'inline-block' }}>
                            <Card.Img variant="top" src={movie.movie_poster} height='200px'/>
                            <Card.Body>
                                <Card.Title>{movie.movie_title}</Card.Title>
                                <Card.Text>
                                    {movie.movie_content.substr(0, 90)}
                                    {movie.movie_content.length > 90 ? '...' : ''}
                                </Card.Text>
                                <Button variant="outline-primary" className="mr-1" onClick={() => props.history.push('/'+movie.movie_id)}>바로보기</Button>
                                <Button variant="outline-danger" onClick={() => handleClickCancle(i)}>선택취소</Button>
                            </Card.Body>
                        </Card>
                    ))}
                </div>
                {checkedMovie.length === 3 ?
                <button className='btn clickrecomm' onClick={handleClickSearch}>내 취향에 맞게 추천받기!</button>:
                <button className='btn clickrecomm_disable disable' onClick={() => alert('영화 '+(3-checkedMovie.length)+'개를 더 선택해야합니다.')}>내 취향에 맞게 추천받기!</button>
                }
                <div className='row'>
                    <div className='movieposter'>
                        {genreFilter(movies).map((movie, i)=>(
                            <img className='img-responsive' src={movie.movie_poster} alt={i} onClick={() => { handleClickImage(movie); }}/>
                        ))}  
                    </div>     
                </div>
            </div>
        </div>
    )
};

export default withRouter(MainPresenter);
