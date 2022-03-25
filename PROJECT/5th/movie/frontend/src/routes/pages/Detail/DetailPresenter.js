import React, { useEffect, useState } from 'react';
import SampleComponent from 'components/sample/SampleComponent';
import { withRouter } from 'react-router-dom';
import axios from 'axios';
import { useHistory, useParams } from 'react-router-dom';
import StarRating from './StarRating.js';
import Pie from './Pie.js';
import BarGraph from './Bar.js';
import Radar from './Radar.js';
import Wordcloud from './Wordcloud.js';


const DetailPresenter = (props) => {
  const [loading, setLoading] = useState(true)
  const [movie, setMovie] = useState({
      "movie_id": 10001,
      "movie_title": "",
      "movie_url": "",
      "movie_aud": 9.63,
      "movie_net": 9.33,
      "movie_rep": 8.38,
      "movie_poster": "",
      "movie_genre": 2,
      "movie_country": 10,
      "movie_runtime": 124,
      "movie_release": "2020-04-22",
      "movie_director": "쥬세페 토르나토레",
      "movie_age": 4,
      "movie_content": "어린 시절 영화가 세상의 전부였던 소년 토토는 학교 수업을 마치면 마을 광장에 있는 낡은 시네마 천국이라는 극장으로 달려가 영사 기사 알프레도와 친구로 지내며 어깨너머로 영사기술을 배운다. 어느 날 관객들을 위해 광장에서 야외 상영을 해주던 알프레도가 그만 화재 사고로 실명하게 되고 토토가 그의 뒤를 이어 시네마 천국의 영상기사로 일하게 된다. 실명한 후에도 토토의 친구이자 아버지로 든든한 정신적 지주가 되어준 알프레도는 청년이 된 토토가 사랑하는 여자 엘레나의 부모님의 반대로 좌절하자 넓은 세상으로 나가서 더 많은 것을 배우라며 권유하는데...",
      "comment": [

      ],
      "gender" : [],
      "age": [],
      "cast": [],
      "point": [],
      "keyword": []
  })
  useEffect(() => {  
    const loadMovies = async() => {
      const config = {
                headers: {
                  "content-type": "application/json"
                }
            };
            await axios.get(`/api/${props.match.params.id}/`, config).then((response)=>{ 
                setMovie(response.data)
                setTimeout(() => {
                  setLoading(false)
                }, 3000);
            }); 
    }
    loadMovies();
  }, []);
  const movieGenreText = (genre) => {
    switch(genre){
      case 1: return '공연실황'
      case 2: return '드라마'
      case 3: return '다큐멘터리'
      case 4: return '애니메이션'
      case 5: return '모험'
      case 6: return '액션'
      case 7: return 'SF'
      case 8: return '멜로/로멘스'
      case 9: return '전쟁'
      case 10: return '범죄'
      case 11: return '판타지'
      case 12: return '가족'
      case 13: return '코미디'
      case 14: return '서부'
      case 15: return '한국'
      case 16: return '뮤지컬'
      case 17: return '공포'
      case 18: return '미스터리'
      case 19: return '스릴러'
      case 20: return '서스펜스'
      case 21: return '느와르'
      case 22: return '서사'
      default: return '-'
    }
  }
  const movieCountryText = (country) => {
    switch(country){
      case 1: return '한국'
      case 2: return '미국'
      case 3: return '레바논'
      case 4: return '일본'
      case 5: return '중국'
      case 6: return '인도'
      case 7: return '이탈리아'
      case 8: return '홍콩'
      case 9: return '뉴질랜드'
      case 10: return '프랑스'
      case 11: return '영국'
      case 12: return '러시아연방'
      case 13: return '이란'
      case 14: return '덴마크'
      case 15: return '대만'
      case 16: return '노르웨이'
      case 17: return '독일'
      case 18: return '오스트레일리아'
      case 19: return '스웨덴'
      case 20: return '독일(구 서독)'
      case 21: return '아일랜드'
      case 22: return '캐나다'
      case 23: return '이스라엘'
      case 24: return '멕시코'
      case 25: return '스페인'
      case 26: return '브라질'
      case 27: return '스위스'
      case 28: return '체코'
      case 29: return '오스트리아'
      case 30: return '네덜란드'
      case 31: return '벨기에'
      case 32: return '그리스'
      case 33: return '아르헨티나'
      case 34: return '인도네시아'
      case 35: return '태국'
      case 36: return '폴란드'
      case 37: return '아이슬란드'
      case 38: return '핀란드'
      default: return '-'
    }
  }
  const movieAgeText = (age) => {
    switch(age){
      case 1: return '전체관람가'
      case 2: return '12세 관람가'
      case 3: return '15세 관람가'
      case 4: return '전체 관람가'
      case 5: return '청소년 관람불가'
      case 6: return 'PG-13'
      case 7: return 'NR'
      case 8: return 'PG'
      case 9: return 'R'
      default: return '-'
    }
  }
  const [commentView, setCommentView] = useState(false)
  const handleClickComment = () =>{
    setCommentView(!commentView)
  }
  const handleClickLink = (url) =>{
    if(url){
      window.location.href = url
    }else{
      alert('준비중 입니다')
    }
  }
  return(
    <>
    {loading || movie.movie_poster === "" ?
    <div>
        Loading...
    </div>
    :
    <div className='detail-content'>    
      <div>
        <div>
          <div className='detail-box'>
            <div className='col-md-12 title-box'>
              <h1>{movie.movie_title}</h1>
            </div>
            <div className='col-md-7 title-box pt-0'>
              <h4>영화 정보</h4>
              <table style={{width: '100%'}}>
                <tr>
                  <th style={{width: '50%'}}>감독</th><td>{movie.movie_director}</td>
                </tr>
                <tr>
                  <th style={{width: '50%'}}>장르</th><td>{movieGenreText(movie.movie_genre)}</td>
                </tr>
                <tr>
                  <th style={{width: '50%'}}>국가</th><td>{movieCountryText(movie.movie_country)}</td>
                </tr>
                <tr>
                  <th style={{width: '50%'}}>상영시간</th><td>{movie.movie_runtime}분</td>
                </tr>
                <tr>
                  <th style={{width: '50%'}}>개봉일</th><td>{movie.movie_release}</td>
                </tr>
                <tr>
                  <th style={{width: '50%'}}>관람연령</th><td>{movieAgeText(movie.movie_age)}</td>
                </tr>
              </table>
              <br/>
              <h4>출연</h4>
              {movie.cast.map((cast, i)=>(
                <div>
                  <b>{cast.cast_actor}</b>{cast.cast_cast ? `: ${cast.cast_cast} 역` : null}
                </div>
              ))}
              <br/>
            </div>
            <div className='col-md-5 detail-poster'>
              <img className='img-detail' src={movie.movie_poster} width='100%' alt='movie1'/>
            </div>
          </div>
          <div className='col-md-7 synopsis p-0'>
            <h4>줄거리</h4>
            <div className='summary'>
              <p>{movie.movie_content}</p>
            </div>
          </div>
          <div className='sex_age_graph'>
            <div className='Graph_1'>
              <h5>성별 선호도</h5>
              {movie.gender[0]?
              <Pie gender={movie.gender[0]}/>
              :null}
            </div>
            
            <div className='Graph_2'>
              <h5>연령 선호도</h5>
              {movie.age[0] ?
              <BarGraph age={movie.age[0]}/>
              :null}
            </div>
            {movie.gender[0]?
            <div className='col-md-12 Graph_3'>
              <div className='circle-m'></div>
              <p className='desc-m'>남자</p>
              <div className='circle-f'></div>
              <p className='desc-f'>여자</p>
            </div>:null}
          </div>
          <div className='sex_age_graph radar_graph'>
            <div className='Graph_1'>
              <h5>감상 포인트</h5>
              {movie.point[0]?
              <Radar point={movie.point[0]}/>
              :null}
            </div>
            
            <div className='Graph_2'>
              <h5>연령 평가</h5>
              {movie.age[0] ?
              <table>
                <tr><th>10 대 </th><td>: ★ {movie.age[0].age_sati10}</td></tr>
                <tr><th>20 대 </th><td>: ★ {movie.age[0].age_sati20}</td></tr>
                <tr><th>30 대 </th><td>: ★ {movie.age[0].age_sati30}</td></tr>
                <tr><th>40 대 </th><td>: ★ {movie.age[0].age_sati40}</td></tr>
                <tr><th>50 대 +</th><td>: ★ {movie.age[0].age_sati50}</td></tr>
              </table>:null}
            </div>
          </div>
          </div>
          <div className='col-md-7 synopsis'>
            <div className='Tag-box'>
              <h5>Wordcloud</h5>
              <Wordcloud keyword={movie.keyword}/>
            </div>
            <br/>
            <div className='review-box'>
              <h5>평점/후기</h5>
              {movie.comment.map((m,i)=>{
                return(
                  commentView || i < 10 ?
                  <li className='comment_list'>
                    <StarRating movie={movie} i={i}/> {movie.comment[i].comment_point}/10
                    <h5>{m.comment_username}</h5>
                    <h5>{m.comment_contents}</h5>
                    <br/>
                  </li>
                  :null
                )
              })} 
              <div className='col-12' style={{textAlign: 'center'}}>
                <a href='javascript:;' onClick={handleClickComment}>{commentView ? '닫기' : '전체보기'}</a>
              </div>
            </div>
          </div>
        </div> 
        <br/>
        <div className='button-box'>
          <button className='btn naver' onClick={() => handleClickLink(movie.movie_url)}> Naver 바로가기 </button>
          {/* <button className='btn netflix' onClick={() => handleClickLink()}> Netflix 바로가기 </button>
          <button className='btn watcha' onClick={() => handleClickLink()}> Watcha 바로가기 </button> */}
        </div>
      </div>
    }
    </>
  );
};

export default withRouter(DetailPresenter);