import { InputGroup } from 'react-bootstrap';
import StarRatings from 'react-star-ratings';

import React, { useState } from 'react';
//let [movie, setMovie] = useState(detailData);


const StarRating = (props, {voteAverage}) => {
  let [movieSatValue, setmovieSatValue] = useState(props.movie);
  //console.log(movieSatValue.comment[87].comment_point);
  
  return (
    <StarRatings
      //rating = {voteAverage/2}
      rating={movieSatValue.comment[props.i].comment_point / 2} 
      caption="Small"
      starRatedColor="yellow"
      starDimension="30px"
      starSpacing="0px"
    />
  );
};

export default StarRating
