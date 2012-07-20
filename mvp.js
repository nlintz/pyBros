var labelType, useGradients, nativeTextSupport, animate;

(function() {
	var ua = navigator.userAgent, iStuff = ua.match(/iPhone/i)
			|| ua.match(/iPad/i), typeOfCanvas = typeof HTMLCanvasElement, nativeCanvasSupport = (typeOfCanvas == 'object' || typeOfCanvas == 'function'), textSupport = nativeCanvasSupport
			&& (typeof document.createElement('canvas').getContext('2d').fillText == 'function');
	// I'm setting this based on the fact that ExCanvas provides text support
	// for IE
	// and that as of today iPhone/iPad current text support is lame
	labelType = (!nativeCanvasSupport || (textSupport && !iStuff)) ? 'Native'
			: 'HTML';
	nativeTextSupport = labelType == 'Native';
	useGradients = nativeCanvasSupport;
	animate = !(iStuff || !nativeCanvasSupport);
})();

var Log = {
	elem : false,
	write : function(text) {
		if (!this.elem)
			this.elem = document.getElementById('log');
		this.elem.innerHTML = text;
		this.elem.style.left = (500 - this.elem.offsetWidth / 2) + 'px';
	}
};

function init() {

	var json =
			[
			{
			"adjacencies": ["1","2","3","4","5","6","7","8","9"], "data": {$dim:300, $color:"grey", "is_star":true,"value": null, "name":"IM A BLACK HOLE","jitid":"","value":""}, "name": "intuit", "id": "0"
			},
			{
			"adjacencies": ["0","10","11"], "data": {$color:"D0D9C8",$dim:100,is_star:true,"value": "100", "name":"mars","jitid":"MA","fin info":"100"}, "name": "mars", "id": "1"
			},
			{
			"adjacencies": ["0","20","21"], "data": {$color:"FDBD27",$dim:75,is_star:true,"value": "150", "name":"pluto","jitid":"Pl","fin info":"100"}, "name": "pluto", "id": "2"
			},
			{
				"adjacencies": ["0","30","31"], "data": {$color:"DA5915",$dim:200,"is_star":true,"value": "150", "name":"saturn","jitid":"S","fin info":"100"}, "name": "saturn", "id": "3"
			},
			{
				"adjacencies": ["0","40","41"], "data": {$color:"4813A4",$dim:140,"is_star":true,"value": "200", "name":"uranus","jitid":"U","fin info":"100"}, "name": "uranus", "id": "4"
			},
			{
				"adjacencies": ["0","50","51"], "data": {$color:"1581F5",$dim:59,"is_star":true,"value": "10", "name":"venus","jitid":"V","fin info":"100"}, "name": "venus", "id": "5"
			},
			{
				"adjacencies": ["0","60","61"], "data": {$color:"333333",$dim:80,"is_star":true,"value": "1500", "name":"neptune","jitid":"NE","fin info":"100"}, "name": "neptune", "id": "6"
			},
			{
				"adjacencies": ["0","70","71"], "data": {$color:"5FFF00",$dim:60,"is_star":true,"value": "1950", "name":"HG","jitid":"Merc","fin info":"100"}, "name": "HG", "id": "7"
			},
			{
				"adjacencies": ["0","80","81"], "data": {$color:"808099",$dim:25,is_star:true,"value": "20", "name":"Jupiter","jitid":"JU","fin info":"100"}, "name": "Jupiter", "id": "8"
			},
			{
				"adjacencies": ["0","90","91"], "data": {$color:"003399",$dim:130,"is_star":true,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"100"}, "name": "NathanVille", "id": "9"
			},
			
			
			{
				"adjacencies": ["1"], "data": {$dim:60,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "10"
			},
			{
				"adjacencies": ["1"], "data": {$dim:60,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "11"
			},
			
			{
				"adjacencies": ["2"], "data": {$dim:30,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "20"
			},
			{
				"adjacencies": ["2"], "data": {"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "21"
			},
			
			{
				"adjacencies": ["3"], "data": {$dim:30,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "30"
			},
			{
				"adjacencies": ["3"], "data": {$dim:60,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "31"
			},
			
			{
				"adjacencies": ["4"], "data": {"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "40"
			},
			{
				"adjacencies": ["4"], "data": {$dim:30,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "41"
			},
			
			{
				"adjacencies": ["5"], "data": {"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "50"
			},
			{
				"adjacencies": ["5"], "data": {$dim:60,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "51"
			},
			
			{
				"adjacencies": ["6"], "data": {"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "60"
			},
			{
				"adjacencies": ["6"], "data": {$dim:30,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "61"
			},
			
			{
				"adjacencies": ["7"], "data": {"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "70"
			},
			{
				"adjacencies": ["7"], "data": {$dim:60,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "71"
			},
			
			{
				"adjacencies": ["8"], "data": {"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "80"
			},
			{
				"adjacencies": ["8"], "data": {$dim:30,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "81"
			},
			
			{
				"adjacencies": ["9"], "data": {$dim:60,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"Stock Went up 100!"}, "name": "NathanVille", "id": "90"
			},
			{
				"adjacencies": ["9"], "data": {$dim:30,"is_star":false,"value": "160", "name":"NathanVille","jitid":"NV","fin info":"New CEO!"}, "name": "NathanVille", "id": "91"
			},
			
			
			
			]
	
			
	
	// init RGraph
	var rgraph = new $jit.RGraph({
		// Where to append the visualization
		injectInto : 'infovis',
		levelDistance : 400,
		// Add navigation capabilities:
		// zooming by scrolling and panning.

		// Add navigation capabilities:
		// zooming by scrolling and panning.

		// My Attempt At Orbits

		Label : {
			overridable : true,
			type : 'HTML', // Native or HTML
			size : 20,
			style : 'bold'
		},
		Navigation : {
			enable : true,
			panning : true,
			zooming : 10
		},
		// Set Node and Edge styles.
		Node : {
			alpha : 1,
			'overridable' : true,
			allowVariableNodeDiameters : true,
			CanvasStyles : {
				strokeStyle : "0000CC"
			}
		},

		NodeStyles : {
			enable : true,
			type : 'auto',
			stylesHover : {
				color : '#fcc'
			},
			duration : 600
		},

		Edge : {
			color : '#33FF33',
			alpha : .5,
			lineWidth : 1.5
		},
		Tips : {
			enable : true,
			type : 'auto',
			offsetX : 20,
			offsetY : 20,
			onShow : function(tip, elem) {
				if (elem.data.is_star){
					tip.innerHTML = "Name: \n"+elem.name+" Ticker: \n" +elem.data.jitid +"Value: \n"+elem.data.value
				}
				else{
					tip.innerHTML = "Financial Information"+elem.data["fin info"];
				}
				
				
			}

		},

		onBeforeCompute : function(node) {
			// Add the relation list in the right column.
			// This list is taken from the data property of each JSON node.
			$jit.id('inner-details').innerHTML = node.data.relation;
		},

		// Add the name of the node in the correponding label
		// and a click handler to move the graph.
		// This method is called once, on label creation.
		onCreateLabel : function(domElement, node) {
			domElement.innerHTML = node.name;
			domElement.onclick = function() {
				rgraph.onClick(node.id, {
					onComplete : function() {
					}
				});
			};
		},
		// Change some label dom properties.
		// This method is called each time a label is plotted.
		onPlaceLabel : function(domElement, node) {
			var style = domElement.style;
			style.display = '';
			style.cursor = 'pointer';

			if (node._depth <= 1) {
				style.fontSize = "0.8em";
				style.color = "#ccc";

			} else if (node._depth == 2) {
				style.fontSize = "0.7em";
				style.color = "#494949";

			} else {
				style.display = 'none';
			}

			var left = parseInt(style.left);
			var w = domElement.offsetWidth;
			style.left = (left - w / 2) + 'px';
		}
	});
	// load JSON data
	rgraph.loadJSON(json);
	// trigger small animation
	rgraph.graph.eachNode(function(n) {
		var pos = n.getPos();
		pos.setc(-200, -200);
	});

	rgraph.compute('end');
	 rgraph.fx.animate({
	 modes : [ 'polar' ],
	 duration : 4000
	 });
	 

	// end

	// append information about the root relations in the right column
	$jit.id('inner-details').innerHTML = rgraph.graph.getNode(rgraph.root).data.relation;



}
