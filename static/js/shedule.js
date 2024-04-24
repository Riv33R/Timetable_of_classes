axios.get('/schedule')
    .then(function (response) {
        const schedule = response.data;
        const days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'];
        const table = document.getElementById('schedule');
        let maxRows = 0;
        days.forEach(day => maxRows = Math.max(maxRows, schedule[day].length));
        for (let i = 0; i < maxRows; i++) {
            const row = table.insertRow(-1);
            days.forEach(day => {
                const cell = row.insertCell(-1);
                if (schedule[day][i]) {
                    const divName = document.createElement('div');
                    divName.className = 'lesson-name';
                    divName.textContent = schedule[day][i].Предмет;
                    const divTime = document.createElement('div');
                    divTime.className = 'lesson-time';
                    divTime.textContent = schedule[day][i].Время;
                    cell.appendChild(divName);
                    cell.appendChild(divTime);
                } else {
                    cell.textContent = "-";
                }
            });
        }
    })
    .catch(function (error) {
        console.log(error);
    });