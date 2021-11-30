// let xhttp = new XMLHttpRequest();
// xhttp.open('GET','./get_all_employee',true)
// console.log(xhttp.responseText)

fetch('/test').then(function (response) {
	// The API call was successful!
	return response.json();
}).then(function (data) {
	// This is the JSON from our response
	console.log(data);
}).catch(function (err) {
	// There was an error
	console.warn('Something went wrong.', err);
});