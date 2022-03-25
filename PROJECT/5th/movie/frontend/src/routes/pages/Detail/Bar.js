import React from "react";
import { BarChart, Bar, XAxis, YAxis } from 'recharts';



export default function BarGraph(props) {
  const data = [
    {
      name: "10대",
      age_view: props.age.age_view10,
  
    },
    {
      name: "20대",
      age_view: props.age.age_view20,
  
    },
    {
      name: "30대",
      age_view: props.age.age_view30,
  
    },
    {
      name: "40대",
      age_view: props.age.age_view40,
    },
    {
      name: "50대+",
      age_view: props.age.age_view50,
    }
  ];

  return (
    props.age.age_view10 !== 999 ?
    <BarChart 
    width={300} 
    height={180} 
    data={data}
    barSize={30}
    margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5,
      }} >
      <Bar 
      dataKey="age_view" 
      fill="#43C6DB" 
      background={{ fill: '#eee' }}
      label={{ 
          position: 'top', 
          fontSize:'10pt',
          fill:'#0275d8',
          fontWeight:'bold'
      }}/>
      <XAxis dataKey="name" scale="point" padding={{ left: 5, right: 5 }} />
      <YAxis type="number" domain={[0, 100]} hide={true} />
    </BarChart>: null
  );
}