const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://twitter241.p.rapidapi.com/user',
  params: {
    username: 'MrBeast'
  },
  headers: {
    'X-RapidAPI-Key': '9c33797ae9msh214c753802a05b9p1b7330jsn391debf27903',
    'X-RapidAPI-Host': 'twitter241.p.rapidapi.com'
  }
};

async function get_response() {
try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}
}

get_response();