import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './EditSchedule.css';

const EditSchedule = () => {
  const [classes, setClasses] = useState([]);
  const [subjects, setSubjects] = useState([]);
  const [schedule, setSchedule] = useState({
    class_name: '',
    subject: '',
    day_of_week: '',
    start_time: '',
    end_time: ''
  });

  useEffect(() => {
    axios.get('/api/classes/')
      .then(response => setClasses(response.data))
      .catch(error => console.error("There was an error fetching the classes!", error));

    axios.get('/api/subjects/')
      .then(response => setSubjects(response.data))
      .catch(error => console.error("There was an error fetching the subjects!", error));
  }, []);

  const handleChange = (e) => {
    setSchedule({
      ...schedule,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/schedules/', schedule)
      .then(response => {
        alert('Schedule added successfully!');
        setSchedule({
          class_name: '',
          subject: '',
          day_of_week: '',
          start_time: '',
          end_time: ''
        });
      })
      .catch(error => {
        console.error("There was an error adding the schedule!", error);
      });
  };

  return (
    <div className="edit-schedule">
      <h2>Edit Schedule</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Class</label>
          <select name="class_name" value={schedule.class_name} onChange={handleChange}>
            <option value="">Select Class</option>
            {classes.map((cls) => (
              <option key={cls.id} value={cls.id}>{cls.name}</option>
            ))}
          </select>
        </div>
        <div>
          <label>Subject</label>
          <select name="subject" value={schedule.subject} onChange={handleChange}>
            <option value="">Select Subject</option>
            {subjects.map((sub) => (
              <option key={sub.id} value={sub.id}>{sub.name}</option>
            ))}
          </select>
        </div>
        <div>
          <label>Day of Week</label>
          <select name="day_of_week" value={schedule.day_of_week} onChange={handleChange}>
            <option value="">Select Day</option>
            <option value="Monday">Monday</option>
            <option value="Tuesday">Tuesday</option>
            <option value="Wednesday">Wednesday</option>
            <option value="Thursday">Thursday</option>
            <option value="Friday">Friday</option>
          </select>
        </div>
        <div>
          <label>Start Time</label>
          <input type="time" name="start_time" value={schedule.start_time} onChange={handleChange} />
        </div>
        <div>
          <label>End Time</label>
          <input type="time" name="end_time" value={schedule.end_time} onChange={handleChange} />
        </div>
        <button type="submit">Save Schedule</button>
      </form>
    </div>
  );
};

export default EditSchedule;
