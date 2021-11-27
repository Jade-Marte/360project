// let xhttp = new XMLHttpRequest();
// xhttp.open('GET','./get_all_employee',true)
// console.log(xhttp.responseText)

fetch('/get_all_employee').then(function (response) {
	// The API call was successful!
	return response.json();
}).then(function (data) {
	// This is the JSON from our response
	console.log(data.name);
}).catch(function (err) {
	// There was an error
	console.warn('Something went wrong.', err);
});