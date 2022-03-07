import React, { useEffect, useState } from 'react';
import { Navbar, Nav, NavDropdown, Form, FormControl, Button } from 'react-bootstrap';
import axios from 'axios';

const MainPresenter = () => {
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
        await axios.get(`/api/`, config).then((response)=>{
            // console.log(response.data)
            setMovies(response.data)
        }); 
    }
    loadMovies();
  }, []);
  
  return (
   <>
    <Navbar bg="light" expand="lg">
      <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="#home">Home</Nav.Link>
          <Nav.Link href="#link">Link</Nav.Link>
          <NavDropdown title="Dropdown" id="basic-nav-dropdown">
            <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
            <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
            <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
          </NavDropdown>
        </Nav>
        <Form inline>
          <FormControl type="text" placeholder="Search" className="mr-sm-2" />
          <Button variant="outline-success">Search</Button>
        </Form>
      </Navbar.Collapse>
    </Navbar>
    <div>
      {movies.map((movie, i)=>(
        <div>
          {i+1}: {movie.movie_title}<br/>
        </div>
      ))}
    </div>
    </>
  );
};

export default MainPresenter;
