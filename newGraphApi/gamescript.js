function gamescript(){
//	Start Setting up the Canvas Elements
	var CANVAS_WIDTH = window.innerWidth;
	var CANVAS_HEIGHT = window.innerHeight;
	var CENTERX = CANVAS_WIDTH/2;
	var CENTERY = CANVAS_HEIGHT/2;
	var canvasElement = $("<canvas id='container' width='" + window.innerWidth + "' height='"
			+ window.innerHeight + "'></canvas>");
	var canvas = canvasElement.get(0).getContext("2d");
	canvasElement.appendTo('body');
	
// 	Kinetic JS Elements

	var stage = new Kinetic.Stage({
          container: "container",
          width: window.innerWidth,
          height: window.innerHeight
        });
    var layer = new Kinetic.Layer();

// End Setting Up The Canvas


	canvas.fillStyle = "#FF0000";
	canvas.font = "bold 16px Arial";

	
//	Start setting up frame rate
// 	Dont edit me unless you need to change framerate or something like that
	var FPS = 30;
	setInterval(function() {
		update();
		draw();
	}, 1000 / FPS);
//	End setting up frame rate

//	Update Loop - Controls game logic IE carcurations
	function update() {
		var angleOffset=0;
		
		Stars.forEach(function(star){
			var angle = calculateAngles(Stars)
			star.draw(angle*angleOffset);
			angleOffset++;
		});
		Planets.forEach(function(planet){
			var angle=calculateAngles(planet.starOrigin.planets);
			planet.draw(angle*angleOffset);
			angleOffset++;
		});
	}
	
//	Draw Loop - clears and repaints the screen every frame
	
	function draw() {	
		canvas.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
		b.draw();
		stage.add(layer);
		stage.remove(layer);
	}
	
// 	Initialize the objects 
// 	%TODO% make an interface to enter in all the objects from a json object
// 	var s = new Star({size:50,color:'green',distance:200, name: "apple", price: "10", ticker:"AAPL", orbitalVelocity:.02})
// 	var s2 = new Star({size:50,color:'yellow',distance:140, name: "starbucks", price: "20", ticker:"SB", orbitalVelocity:.05})
// 	var s3 = new Star({size:35, color:'blue', distance: 140, name: "microsoft", price: "30", ticker:"MC", orbitalVelocity:.01})
// 	var s4 = new Star({size:35, color:'blue', distance: 300, name: "ubisoft", price: "100", ticker:"UB", orbitalVelocity:.01})
// 	var Stars = [s,s2,s3,s4];

	Stars=[]
	for (var i=0; i<50; i++){
		Stars.push(new Star({size:50,color:'green',distance:200+i*10, name: "apple", price: "10", ticker:"AAPL", orbitalVelocity:.02}))
	};
	console.log(Stars);
	
	var p = new Planet(Stars[0]);
	var p2 = new Planet(Stars[1]);
	var p3 = new Planet(Stars[1]);
	var p4 = new Planet(Stars[1]);
	var p5 = new Planet(Stars[1]);



	var Planets = [p,p2,p3,p4,p5];
	
	var b = new BlackHole({size:20})
	b.draw();
// 	Objects initialized
	
	
//	collision logic
	function collides(a, b) {
		return a.x < b.x + b.width && a.x + a.width > b.x
				&& a.y < b.y + b.height && a.y + a.height > b.y;
	}
	
	var angle = calculateAngles(Stars);
	function Star(sunObject){
		this.name=sunObject.name
		this.ticker=sunObject.ticker
		this.price=sunObject.price
// 		this.adjacencies=sunObject.adjacencies;
		this.planets=[];		
		this.orbitalVelocity = sunObject.orbitalVelocity;
		this.distance=sunObject.distance;
		this.color=sunObject.color
		this.size=sunObject.size
		var rotationHolder = 0;
		this.x=this.distance*Math.cos(angle+rotationHolder)+CENTERX;
		this.y=this.distance*Math.sin(angle+rotationHolder)+CENTERY;
		this.text=this.name+ "::" + this.ticker +"::" + "$" + this.price;
		this.draw = function(angle){
// 				canvas.beginPath();
// 				var iangle=0;
// 				var eangle=Math.PI*2;
// 				canvas.arc(this.x,this.y,this.size,iangle,eangle, true);
// 				canvas.closePath();
// 				canvas.fillStyle=this.color;
// 				canvas.fill();
// 				rotationHolder += .02;
			this.x = this.distance*Math.cos(angle+rotationHolder)+CENTERX;
			this.y = this.distance*Math.sin(angle+rotationHolder)+CENTERY;
			var label = new Kinetic.Text({
          		x: this.x,
          		y: this.y,
          		text: this.name+"\n"+this.ticker+"\n"+this.price,
          		fontSize: 12,
          		fontFamily: "Arial",
          		textFill: "gray"
        	});
			var star = new Kinetic.Circle({
          		x: this.x,
          		y: this.y,
          		radius: this.size,
          		fill: this.color,
       	 	});
       	 	star.on('click', function(){
       	 		console.log('hello, world!');
       	 	});
       	 	
       		rotationHolder += this.orbitalVelocity;
			layer.add(star);
			layer.add(label);
			};
		}
	
	function Planet(starOrigin){
		this.starOrigin = starOrigin;
		var planetaryOffset = starOrigin.size+25;
		var rotationHolder = 0;
		starOrigin.planets.push(this);
		this.draw = function(angle){
// 		This was how i implemented circles before, its clearly not the right way to do it
// 			canvas.beginPath();
// 			var iangle=0;
// 			this.x=planetaryOffset*Math.cos(angle+rotationHolder)+starOrigin.x;
// 			this.y=planetaryOffset*Math.sin(angle+rotationHolder)+starOrigin.y;
// 			var eangle=Math.PI*2;
// 			canvas.arc(this.x,this.y,10,iangle,eangle,true);
// 			canvas.closePath();
// 			canvas.fillStyle='red';
// 			canvas.fill();

		var planet = new Kinetic.Circle({
        	x: planetaryOffset*Math.cos(angle+rotationHolder)+starOrigin.x,
        	y: planetaryOffset*Math.sin(angle+rotationHolder)+starOrigin.y,
        	radius: 10,
        	fill: "red",
			});
       	rotationHolder += .05
		layer.add(planet);
		}
		
	}
		
	function BlackHole(sunObject){
// 		this.name=sunObject.name
// 		this.adjacencies=sunObject.adjacencies;
		this.color='gray'
		this.distance=sunObject.distance;
		this.size=100;
		this.draw = function(angle){
// 				canvas.beginPath();
// 				var iangle=0;
// 				var x = CENTERX
// 				var y = CENTERY;
// 				var eangle=Math.PI*2;
// 				canvas.arc(x,y,this.size,iangle,eangle, true);
// 				canvas.closePath();
// 				canvas.fillStyle='black';
// 				canvas.fill();
// 				canvas.fillStyle='white';
// 				canvas.fillText('Im a fucking BLACKHOLE',x-90,y);
			this.x = CENTERX;
			this.y = CENTERY;
			var blackHoleLabel = new Kinetic.Text({
          		x: this.x-99,
          		y: this.y,
          		text: "Im a fucking black hole",
          		fontSize: 14,
          		fontFamily: "Arial",
          		textFill: "white"
        	});
			var blackhole = new Kinetic.Circle({
          		x: this.x,
          		y: this.y,
          		radius: this.size,
          		fill: this.color,
       	 	});
			layer.add(blackhole);
			layer.add(blackHoleLabel);

			};
		}
		
// 	This function calculates the angle between nodes so that there is no colision
	function calculateAngles(nodeList){
		return (2*Math.PI)/nodeList.length;
	}
		

		
	
}