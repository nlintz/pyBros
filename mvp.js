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
			"adjacencies": ["239"], "data": {"is_star":true,"value": null, "name":"intuit","jitid":"herroi","value":"9000"}, "name": "intuit", "id": "Az9"
			},
			{
				"adjacencies": ["Az9"], "data": {"is_star":false,"value": null, "name":"mars","jitid":"","value":"", "fin info":"100"}, "name": "intuit", "id": "239"
			}
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
			color : '#0099FF',
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
