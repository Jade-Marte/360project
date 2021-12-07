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
	let table = document.getElementById('timesheet')
	if (table.children.length != 0) return 
	for(let i = 1; i < 14; i ++){
		days = current_date.setDate(current_date.getDate() - 1)
		let dates = new Date(days).toDateString()
		let row = document.createElement('tr')
		row.innerHTML = `
			<td>${dates}</td>
			<td><input type="time" id="time_in"></td>
			<td><input type="time" id="time_out"></td>
		`
		table.appendChild(row)
	}
	
}

async function submit_timesheet(){
	let timesheet = []
	let tBody = document.getElementById('timesheet')
	for(let i = 0; i < tBody.children.length; i ++){
		let tr = tBody.children[i]
		let date = tr.children[0].innerText
		date = new Date(date)
		let timeIn = tr.children[1].firstChild.value
		let timeOut = tr.children[2].firstChild.value
		if(timeIn != '' && timeOut != '')
		timesheet.push({'date':date.toISOString().split('T')[0],'time_in':timeIn + ":00",'time_out':timeOut + ":00"})
	}
	const response = await fetch("./uploadTimesheet", {
	method: 'POST',
		body: JSON.stringify(timesheet)
		});

	response.json().then(data => {
	console.log(data);
	});  
	}



