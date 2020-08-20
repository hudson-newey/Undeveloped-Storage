let getTime = () => {
	let timeOUT = "";
	let ampm = "AM";
	const d = new Date();
	
	// convert out of 24 hour time
	if (d.getHours() > 12) {
		timeOUT += (d.getHours() - 12);
		ampm = "PM";
	} else {
		timmeOUT += d.getHours();
	}

	// minutues
	timeOUT += ":"+d.getMinutes();
	timeOUT += ampm;
	return timeOUT;
}

let timeApp = new Vue({
	el: ".app",
	data: {
		time: getTime()
	}
})