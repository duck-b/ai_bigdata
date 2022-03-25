import React from 'react';
import { withRouter } from 'react-router-dom';

import ReactWordcloud from 'react-wordcloud';
 
const Wordcloud = (props) => {

    // console.log(Object.values(props.keyword))
    const words = [];
    for(let i = 0; i<Object.keys(props.keyword).length; i++){
        // console.log(Object.keys(props.keyword)[i])
        words.push({text: Object.keys(props.keyword)[i], value: Object.values(props.keyword)[i]})
    }
    // const words = 
    // const words = [
    //     {
    //       text: 'told',
    //       value: 64,
    //     },
    //     {
    //       text: 'mistake',
    //       value: 11,
    //     },
    //     {
    //       text: 'thought',
    //       value: 16,
    //     },
    //     {
    //       text: 'bad',
    //       value: 17,
    //     },
    //   ]
    const options = {
        fontSizes: [15, 100]
    }
  return <ReactWordcloud words={words} options={options}/>
}

export default withRouter(Wordcloud)