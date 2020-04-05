var loading = true;
var states = [];

getStates();
getData('New York');

function getData(state){
    let dataAr = [];
    $.getJSON( "https://covid19.perrinresearch.com/api/v1/confirmed?state="+state, function( data ) {
        console.log(data);
        for(datum of data.data){
	    dataAr.push({
		name: datum.Admin2,
		//name: datum.Province_State + ', ' + datum.Country_Region,
		data: datum.ConfirmedCount
            })
        }
	//dataAr = data.data;
	console.log(dataAr);
	loading = false;
	document.getElementById("loading").style.display = "None";
	document.getElementById("loaded").style.display = "block";
	loadChart(dataAr,state);
	return dataAr;
    });
}

function getStates() {
    $.getJSON( "https://covid19.perrinresearch.com/api/v1/options/state", function( data ) {
        console.log(data);
        states = data.data;
	let selector = document.getElementById("states");
	for (state of data.data){
           let option = document.createElement("option");
           option.text = state;
           if (state === 'New York'){
	      option.selected = true;
           }
           selector.options.add(option);
        }
    });
}
