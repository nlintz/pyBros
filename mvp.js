var labelType, useGradients, nativeTextSupport, animate;


(function() {
  var ua = navigator.userAgent,
      iStuff = ua.match(/iPhone/i) || ua.match(/iPad/i),
      typeOfCanvas = typeof HTMLCanvasElement,
      nativeCanvasSupport = (typeOfCanvas == 'object' || typeOfCanvas == 'function'),
      textSupport = nativeCanvasSupport 
        && (typeof document.createElement('canvas').getContext('2d').fillText == 'function');
  // I'm setting this based on the fact that ExCanvas provides text support
	// for IE
  // and that as of today iPhone/iPad current text support is lame
  labelType = (!nativeCanvasSupport || (textSupport && !iStuff))? 'Native' : 'HTML';
  nativeTextSupport = labelType == 'Native';
  useGradients = nativeCanvasSupport;
  animate = !(iStuff || !nativeCanvasSupport);
})();

var Log = {
  elem: false,
  write: function(text){
    if (!this.elem) 
      this.elem = document.getElementById('log');
    this.elem.innerHTML = text;
    this.elem.style.left = (500 - this.elem.offsetWidth / 2) + 'px';
  }
};


function init(){
	


	var json = {
		id : "1",
		name : "blackHole",
		data : {
			$color: '#C17878',
			$dim : 500,
			pokemonPower : "turnYoSwagOn",
			tip: "protect ya neck"
		},
		children : [ {
			id : "2",
			name : "apple",
			data : {
				value : "200",
				inc : "2",
				$dim : 25,
			},
			children : [ {
				id : "21",
				name : "wiki",
				data : {
					link : "http://www.wikipedia.com"
				},
				children : []
			}, {
				id : "22",
				name : "bloomberg",
				data : {
					link : "http://www.bloomberg.com"
				},
				children : []
			} ]
		}, {
			id : "3",
			name : "faecbook",
			data : {
				$dim : 30,
				value : "300",
				inc : "3",
			},
			children : [ {
				id : "31",
				name : "wiki",
				data : {
					link : "http://www.wikipedia.com"
				},
				children : []
			} ]
		}, {
			id : "4",
			name : "microsoft",
			data : {
				$dim : 10,
				value : "400",
				inc : "4",
			},
			children : [ {
				id : "41",
				name : "wiki",
				data : {
					link : "http://www.wikipedia.com"
				},
				children : []
			} ]
		} ]
	}


	// init RGraph
	var rgraph = new $jit.RGraph({
		// Where to append the visualization
		injectInto : 'infovis',
		levelDistance : 750,
		// Add navigation capabilities:
		// zooming by scrolling and panning.


        // Add navigation capabilities:
        // zooming by scrolling and panning.


		Label: {
			overridable: true,
		    type: 'HTML', // Native or HTML
		    size: 20,  
		    style: 'bold'  
		  },  
		Navigation: {
          enable: true,
          panning: true,
          zooming: 10
        },
        // Set Node and Edge styles.
        Node : {
			color : '#0099FF',
			alpha : 1,
			'overridable' : true,
			allowVariableNodeDiameters : true,
			CanvasStyles: {
				strokeStyle: "0000CC"
			}
		},
		
		NodeStyles:{
			enable: true,
			type: 'auto',
			stylesHover: {  
			      color: '#fcc'  
			    },  
			duration: 600
		},
		
		

        
		Edge : {
			color : '#33FF33',
			alpha: .5,
			lineWidth : 1.5
		},
		Tips : {  
			  enable: true,  
			  type: 'auto',  
			  offsetX: 20,  
			  offsetY: 20,
			  onShow: function(tip, elem) {
			         tip.innerHTML = "<b>" + elem.name + "</b>: " + elem.data.tip;
			      }

			},

        

        onBeforeCompute: function(node){
            // Add the relation list in the right column.
            // This list is taken from the data property of each JSON node.
            $jit.id('inner-details').innerHTML = node.data.relation;
        },
        
        // Add the name of the node in the correponding label
        // and a click handler to move the graph.
        // This method is called once, on label creation.
        onCreateLabel: function(domElement, node){
            domElement.innerHTML = node.name;
            domElement.onclick = function(){
                rgraph.onClick(node.id, {
                    onComplete: function() {
                    }
                });
            };
        },
        // Change some label dom properties.
        // This method is called each time a label is plotted.
        onPlaceLabel: function(domElement, node){
            var style = domElement.style;
            style.display = '';
            style.cursor = 'pointer';

            if (node._depth <= 1) {
                style.fontSize = "0.8em";
                style.color = "#ccc";
            
            } else if(node._depth == 2){
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
      modes:['polar'],
      duration: 2000
    });
    // end
    // append information about the root relations in the right column
    $jit.id('inner-details').innerHTML = rgraph.graph.getNode(rgraph.root).data.relation;
}

