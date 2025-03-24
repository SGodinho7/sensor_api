const form = document.querySelector('#sensor-form');

async function postSensor() {
	form_data = new FormData(form);

	try {
		const response = await fetch('/sensors/post_sensor', {
			method: 'POST',
			body: form_data,
		});
		console.log(await response.json());
	} catch (e) {
		console.error(e);
	}
}

form.addEventListener('submit', (event) => {
	event.preventDefault();
	postSensor();
});
