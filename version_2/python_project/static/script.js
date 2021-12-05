// let xhttp = new XMLHttpRequest();
// xhttp.open('GET','./get_all_employee',true)
// console.log(xhttp.responseText)

// fetch('/test').then(function (response) {
// 	// The API call was successful!
// 	return response.json();
// }).then(function (data) {
// 	// This is the JSON from our response
// 	console.log(data);
// }).catch(function (err) {
// 	// There was an error
// 	console.warn('Something went wrong.', err);
// });

function get_session(button){
	let id = button.id
	fetch('/sessions/'+ id).then(function (response) {
		// The API call was successful!
		return response.json();
	}).then(function (data) {
		// This is the JSON from our response
		display_data(data)
		console.log(data);
	}).catch(function (err) {
		// There was an error
		console.warn('Something went wrong.', err);
	});
	
}
function display_data(session_data){
	// remember session_data is a list of objects
	let table = document.getElementById('sessions')

	for(let i = 0; i < session_data.length; i++){
		// template literals allow a bunch of code
		let row = document.createElement('tr')
		row.innerHTML = `
						<td>${session_data[i].date}</td>
						<td>${session_data[i].time_in}</td>
						<td>${session_data[i].time_out}</td>
						<td>${session_data[i].total_hours}</td>
					`
		table.appendChild(row)
	}

}

function display_timesheet(){
	// starting from today backtrack two weeks for timesheet
	let current_date = new Date()
	let days = new Date()
	let today = current_date.toDateString()
	for(let i = 1; i < 14; i ++){
		days = current_date.setDate(current_date.getDate() - 1)
		let dates = new Date(days).toDateString()
		let table = document.getElementById('timesheet')
		let row = document.createElement('tr')
		row.innerHTML = `
			<td>${dates}</td>
			<td><input type="time" id="time_in"></td>
			<td><input type="time" id="time_out"></td>
		`
		table.appendChild(row)
	}
	let input = document.getElementById('timesheet')
	let submit = document.createElement('tr')
	submit.innerHTML = `
		<input type="submit" value="+" id='add'>
	`
	input.appendChild(submit)
	

	

}

