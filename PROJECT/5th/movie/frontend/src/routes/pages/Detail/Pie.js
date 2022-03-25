import React from 'react';
import { PieChart } from 'react-minimal-pie-chart';

// function Pie(props){
function Pie(props){
    const data=[
        { title: '여자', value: 100-props.gender.gender_man, color: '#F88158' },
        { title: '남자', value: props.gender.gender_man, color: '#43C6DB' },
    ];
    return(<PieChart className='PieChart'
        data={data}
        label={({dataEntry})=>dataEntry.value + '%'}
    />)
}

export default Pie