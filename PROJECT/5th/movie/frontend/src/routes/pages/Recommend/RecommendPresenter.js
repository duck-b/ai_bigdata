import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';

import { Link, useHistory, withRouter } from 'react-router-dom';
import {DropdownButton, Dropdown, Button, Card} from 'react-bootstrap';


// axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
// axios.defaults.xsrfCookieName = "XCSRF-TOKEN";
// axios.defaults.withCredentials = true

const RecommendPresenter = (props) => {

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
    const [loading, setLoading] = useState(false);
    useEffect(() => {
        const loadRecommend = async() => {
            setLoading(true)
            const config = {
                headers: {
                    "content-type": "application/json",
                    // "xsrfHeaderName": 'X-CSRFToken'
                }
            };
            await axios.get(`/api/recommend/${props.match.params.genre}/${props.match.params.movie1}/${props.match.params.movie2}/${props.match.params.movie3}/`, config).then((response)=>{//전체 영화데이터
                setMovies(response.data)
                setTimeout(() => {
                    setLoading(false)
                }, 2000)
            }); 
        }
        loadRecommend();
      }, []);
    
    const handleClickReset = () => {
        props.history.goBack()
    }
    const handleClickShare = () => {
        const dummy   = document.createElement("input");
        const text    = window.location.href;
        
        document.body.appendChild(dummy);
        dummy.value = text;
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
        alert(`URL이 복사되었습니다.`);
    }
    return(
        <div className='content'>
            {loading?
            <div>
                Loading...
            </div>
            :
            <>
            <div className='recommendation'>
                <h1>회원님에게 추천된 영화입니다.</h1>
                <p>회원님이 좋아하실 만한 영화를 더 많이 추천해드릴 수 있습니다. <Link onClick={handleClickReset}>다시 선택하기</Link><br/><Link to={'/search'}> 알아서 볼게요!! &lt; Click</Link></p>
                <p>추천 받은 영화가 마음에 드셨다면 지인들과 <Link onClick={handleClickShare}>공유</Link>해 보세요.</p>
            </div>
            <div className='movieposter'>
            {movies.map((movie,i)=>{
                return(
                    <Link to={`/${movie.movie_id}`}><img className='img-responsive2' src={movie.movie_poster} alt="" /></Link>
                )
            })}
            </div>
            </>
            }
        </div>
    )
};

export default withRouter(RecommendPresenter);
