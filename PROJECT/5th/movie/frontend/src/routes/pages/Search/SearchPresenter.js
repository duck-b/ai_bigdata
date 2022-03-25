import React, { useEffect, useState } from 'react';
import axios from 'axios';

import { FormControl, InputGroup, Nav} from 'react-bootstrap';
import TabContent from './TabContent';
import { CSSTransition } from 'react-transition-group';
import { Link } from 'react-router-dom';

const SearchPresenter = () => {
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
  ])
  useEffect(() => {
    const loadMovies = async() => {
        const config = {
            headers: {
                "content-type": "application/json"
            }
        };
        await axios.get(`/api/`, config).then((response)=>{//전체 영화데이터
          setMovies(response.data)
        }); 
    }
    loadMovies();
  }, []);


const [ search, setSearch] = useState("");
const handleChangeSearch = (e) =>{
    setSearch(e.target.value)
}


let [tab, tabChange]=useState(0);
let [swtich, changeSwtich]= useState(false);

return(
<div>
    <InputGroup className="mt-5 col-sm-12">
        <FormControl className='searchbox' 
        placeholder="제목으로 검색"
        aria-describedby="basic-addon2"
        value={search}
        onChange={handleChangeSearch}
        />
        
    </InputGroup>
    <div className='backtorecommend'>
            <strong id='question'><p>취향에 맞는 영화를 못 고르시겠다구요?!  </p>
            <Link to={'/'}><button className='btn clickrecomm'>내 취향에 맞게 추천받기</button></Link>
            </strong>
        </div>
    <div className='movie-list'>
            <div className='detail-search'>
                <Nav fill variant="tabs" defaultActiveKey="link-0" className='search-nav'>
                    <Nav.Item > 
                        <Nav.Link eventKey="link-0" onClick={()=> {changeSwtich(false);tabChange(0)} }>장르</Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Nav.Link eventKey="link-1" onClick={()=> {changeSwtich(false);tabChange(1)} }>전체 보기</Nav.Link>
                    </Nav.Item>
                    
                </Nav>
                <CSSTransition in={swtich} classNames="tabani" timeout={500}>
                    <TabContent tab={tab} changeSwtich={changeSwtich} search={search} movies={movies}/>
                </CSSTransition>
               
            </div>
                
        </div>

</div>
);
};

export default SearchPresenter;
