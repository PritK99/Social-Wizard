const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://instagram130.p.rapidapi.com/account-info',
  params: {username: 'sra_vjti'},
  headers: {
    'X-RapidAPI-Key': '6453a65c59mshe869d90e296c524p179988jsna211f3933f70',
    'X-RapidAPI-Host': 'instagram130.p.rapidapi.com'
  }
};

async function instarequest()
{try {
	const response = await axios.request(options);
	console.log(JSON.stringify(response.data));
} catch (error) {
	console.error(error);
}}

instarequest();