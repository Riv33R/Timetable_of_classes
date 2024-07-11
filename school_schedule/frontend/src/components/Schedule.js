import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Schedule.css';

const Schedule = () => {
  const [schedule, setSchedule] = useState([]);

  useEffect(() => {
    axios.get('/api/schedules/')
      .then(response => {
        setSchedule(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the schedule!", error);
      });
  }, []);

  return (
    <div className="schedule">
      <h2>Weekly Schedule</h2>
      <table>
        <thead>
          <tr>
            <th>Class</th>
            <th>Subject</th>
            <th>Day</th>
            <th>Start Time</th>
            <th>End Time</th>
          </tr>
        </thead>
        <tbody>
          {schedule.map(item => (
            <tr key={item.id}>
              <td>{item.class_name}</td>
              <td>{item.subject}</td>
              <td>{item.day_of_week}</td>
              <td>{item.start_time}</td>
              <td>{item.end_time}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Schedule;
