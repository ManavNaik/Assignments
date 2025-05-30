const url = 'https://free-livescore-api.p.rapidapi.com/livescore-get-search?sportname=basketball&search=NBA%20upcoming%20Matches';
const options = {
	method: 'GET',
	headers: {
		'x-rapidapi-key': '129f2bebbemsh2a45f27b24535c8p10a1aajsne829e1fb4d34',
		'x-rapidapi-host': 'free-livescore-api.p.rapidapi.com'
	}
};
try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}