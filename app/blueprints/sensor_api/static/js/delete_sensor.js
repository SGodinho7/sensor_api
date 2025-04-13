async function deleteSensor(url) {
	try {
		const response = await fetch(url, {
			method: 'DELETE',
		});
		window.location.reload();
		console.log(await response.json());
	} catch (e) {
		console.error(e);
	}
}
