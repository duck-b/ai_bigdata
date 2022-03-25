import React, { PureComponent } from 'react';
import { withRouter } from 'react-router-dom';
import {
  Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Legend
} from 'recharts';

const Rader = (props) => {
    const data = [
        {
          subject: '연기', A: props.point.point_act, fullMark: 30,
        },
        {
          subject: '연출', A: props.point.point_dir, fullMark: 30,
        },
        {
          subject: 'OST', A: props.point.point_ost, fullMark: 30,
        },
        {
          subject: '스토리', A: props.point.point_sto, fullMark: 30,
        },
        {
          subject: '영상미', A: props.point.point_vis, fullMark: 30,
        }
      ];
    return (
      <RadarChart cx={125} cy={125} outerRadius={80} width={250} height={250} data={data}>
        <PolarGrid />
        <PolarAngleAxis dataKey="subject" fill="#FFFFFF"/>
        {/* <PolarRadiusAxis  /> */}
        <Radar dataKey="A" stroke="#8884d8" fill="#8884d8" fillOpacity={0.8}/>
      </RadarChart>
    );
}
export default withRouter(Rader)