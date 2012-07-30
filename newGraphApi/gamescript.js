function gamescript(){
//	Start Setting up the Canvas Elements
	var CANVAS_WIDTH = 500;
	var CANVAS_HEIGHT = 500;
	var CENTERX = CANVAS_WIDTH/2;
	var CENTERY = CANVAS_HEIGHT/2;
	var canvasElement = $("<canvas width='" + CANVAS_WIDTH + "' height='"
			+ CANVAS_HEIGHT + "'></canvas>");
	var canvas = canvasElement.get(0).getContext("2d");
	canvasElement.appendTo('body');
// End Setting Up The Canvas
	
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
	}
	
//	Draw Loop - clears and repaints the screen every frame
	
	function draw() {
		canvas.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
		var angleOffset=0;
		
		Stars.forEach(function(star){
			var angle = calculateAngles(Stars)*Math.PI/180
			star.draw(angle*angleOffset);
			angleOffset++;
			
		});
		Planets.forEach(function(planet){
			var angle=Math.PI;
			planet.draw(angle+angleOffset);
			angleOffset++;
		});
		
		b.draw();
	}
	
	var Planets = [];
	var s = new Star({size:50,color:'green',distance:100, planets:[p]})
	var s2 = new Star({size:50,color:'yellow',distance:100,planets:['p2','p3']})
// 	var s3 = new Star({size:35, color:'blue', distance: 100})
// 	var s4 = new Star({size:35, color:'blue', distance: 100})
// 	var Stars = [s,s2,s3,s4];
	var Stars = [s,s2];
	
// 	var p = new Planet(Stars[0]);
// 	var p2 = new Planet(Stars[1]);
// 	var Planets = [p,p2];
	
	var b = new BlackHole({size:20})
	
//	collision logic
	function collides(a, b) {
		return a.x < b.x + b.width && a.x + a.width > b.x
				&& a.y < b.y + b.height && a.y + a.height > b.y;
	}
	
	var angle = calculateAngles(Stars);
	function Star(sunObject){
// 		this.name=sunObject.name
// 		this.ticker=sunObject.ticker
// 		this.value=sunObject.value
// 		this.adjacencies=sunObject.adjacencies;
		

		var planets = sunObject.planets;
		
		
		
		this.distance=sunObject.distance;
		this.color=sunObject.color
		this.size=sunObject.size
		var rotationHolder = 0;
		this.x=this.distance*Math.cos(angle+rotationHolder)+CENTERX;
		this.y=this.distance*Math.sin(angle+rotationHolder)+CENTERY;
		
		this.draw = function(angle){
				canvas.beginPath();
				var iangle=0;
				this.x = this.distance*Math.cos(angle+rotationHolder)+CENTERX;
				this.y = this.distance*Math.sin(angle+rotationHolder)+CENTERY;
				var eangle=Math.PI*2;
				canvas.arc(this.x,this.y,this.size,iangle,eangle, true);
				canvas.closePath();
				canvas.fillStyle=this.color;
				canvas.fill();
				rotationHolder += .02;
			};
			
		planets.forEach(function(planet){
			Planets.push(planet)
		});
	}
	
	function Planet(starOrigin){
		var planetaryOffset = starOrigin.size+25;
		var rotationHolder = 0;

		this.draw = function(angle){
			this.x=planetaryOffset*Math.sin(angle+rotationHolder)+starOrigin.x;
			this.y=planetaryOffset*Math.cos(angle+rotationHolder)+starOrigin.y;
			console.log(this.x)
			canvas.beginPath();
			var iangle=0;
			var eangle=Math.PI*2;
			canvas.arc(this.x,this.y,10,iangle,eangle,true);
			canvas.closePath();
			canvas.fillStyle='black';
			canvas.fill();
			rotationHolder += .05
			
		}
	}
		
	function BlackHole(sunObject){
// 		this.name=sunObject.name
// 		this.adjacencies=sunObject.adjacencies;
		this.distance=sunObject.distance;
		this.size=10;
		this.draw = function(angle){
				canvas.beginPath();
				var iangle=0;
				var x = CENTERX
				var y = CENTERY;
				var eangle=Math.PI*2;
				canvas.arc(x,y,this.size,iangle,eangle, true);
				canvas.closePath();
				canvas.fillStyle='black';
				canvas.fill();
			};
		}
		
// 	This function calculates the angle between nodes so that there is no colision
	function calculateAngles(nodeList){
		return 360/nodeList.length;
	}
		

		
	
}