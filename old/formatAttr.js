51={Classes:{Events:#68=(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;}), Tips:#64=(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;}), NodeStyles:(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;}), Navigation:(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;})}, constructor:#46=(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;}), config:#47={$extend:true, injectInto:"infovis", type:"2D", width:false, height:false, useCanvas:false, withLabels:true, background:false, Scene:{Lighting:{enable:false, ambient:[1, 1, 1], directional:{direction:{x:-100, y:-100, z:-100}, color:[0.5, 0.3, 0.1]}}}, Node:#54={$extend:false, overridable:true, type:"circle", color:"#ddeeff", alpha:0.9, dim:3, height:20, width:90, autoHeight:false, autoWidth:false, lineWidth:1, transform:true, align:"center", angularWidth:1, span:1, CanvasStyles:{}}, Edge:#55={$extend:false, overridable:true, type:"line", color:"#C17878", lineWidth:1, dim:15, alpha:1, epsilon:7, CanvasStyles:{}}, fps:40, duration:2500, transition:#6=(function (pos) {return pos <= 0.5 ? transition(2 * pos, params) / 2 : (2 - transition(2 * (1 - pos), params)) / 2;}), clearCanvas:true, onBeforeCompute:(function (node) {Log.write("centering " + node.name + "...");$jit.id("inner-details").innerHTML = node.data.relation;}), onAfterCompute:#3=(function () {}), onCreateLabel:(function (domElement, node) {domElement.innerHTML = node.name;domElement.onclick = function () {rgraph.onClick(node.id, {onComplete: function () {Log.write("done");}});};}), onPlaceLabel:(function (domElement, node) {var style = domElement.style;style.display = "";style.cursor = "pointer";if (node._depth <= 1) {style.fontSize = "0.8em";style.color = "#ccc";} else if (node._depth == 2) {style.fontSize = "0.7em";style.color = "#494949";} else {style.display = "none";}var left = parseInt(style.left);var w = domElement.offsetWidth;style.left = left - w / 2 + "px";}), onComplete:#3#, onBeforePlotLine:(function (adj) {}), onAfterPlotLine:#3#, onBeforePlotNode:#3#, onAfterPlotNode:#3#, request:false, Tips:#66={$extend:false, enable:false, type:"auto", offsetX:20, offsetY:20, force:false, onShow:#3#, onHide:#3#}, NodeStyles:{$extend:false, enable:false, type:"auto", stylesHover:false, stylesClick:false}, Events:#69={$extend:false, enable:false, enableForEdges:false, type:"auto", onClick:#3#, onRightClick:#3#, onMouseMove:#3#, onMouseEnter:#3#, onMouseLeave:#3#, onDragStart:#3#, onDragMove:#3#, onDragCancel:#3#, onDragEnd:#3#, onTouchStart:#3#, onTouchMove:#3#, onTouchEnd:#3#, onMouseWheel:#3#}, Navigation:{$extend:false, enable:true, type:"auto", panning:true, zooming:40}, Label:{$extend:false, overridable:false, type:"HTML", style:" ", size:10, family:"sans-serif", textAlign:"center", textBaseline:"alphabetic", color:"#fff"}, 
		interpolation:"linear", levelDistance:100, me:#4=({}), labelContainer:"infovis-label"}


, controller:#47#, canvas:#65={canvases:[{translateOffsetX:0, translateOffsetY:0, scaleOffsetX:1, scaleOffsetY:1, constructor:#48=(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;}), viz:{config:#49={idSuffix:"-canvas", injectInto:"infovis", width:1680, height:863}, plot:(function (base) {viz.fx.plot();}), resize:(function () {viz.refresh();})}, opt:#49#, size:{width:1680, height:863}, canvas:({}), ctx:({}), $$family:"class"}], pos:false, element:({}), labelContainer:#56=({}), translateOffsetX:0, translateOffsetY:0, scaleOffsetX:1, scaleOffsetY:1, constructor:#50=(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;}), viz:#51#, config:#47#, opt:#47#, id:"infovis", $$family:"class"}, 
		graphOptions:{klass:#52=(function (theta, rho) {this.theta = theta || 0;this.rho = rho || 0;}), 
			Node:{selected:false, exist:true, drawn:true}}, graph:{constructor:#53=(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;}), Node:#54#, Edge:#55#, Label:(void 0), opt:{klass:#52#, Node:{selected:false, exist:true, drawn:true}}, nodes:{}, edges:{}, nodeList:{getData:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), setData:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), setDataset:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), removeData:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), getCanvasStyle:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), setCanvasStyle:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), setCanvasStyles:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), removeCanvasStyle:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), getLabelData:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), setLabelData:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), setLabelDataset:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});}), removeLabelData:(function () {var args = Array.prototype.slice.call(arguments);that.eachNode(function (n) {n[p].apply(n, args);});})}, $$family:"class"}, labels:#62={labelsHidden:false, labelContainer:#56#, labels:{}, constructor:#57=(function () {for (var key in this) {if (typeof this[key] != "function") {this[key] = $.unlink(this[key]);}}this.constructor = klass;if (Class.prototyping) {return this;}var instance = this.initialize ? this.initialize.apply(this, arguments) : this;this.$$family = "class";return instance;}), viz:#51#, $$family:"class"}, fx:{nodeHelper:{none:{render:#3#, contains:#8=(function () {return value;})}, circle:{render:#9=(function (type, pos, radius, canvas) {var ctx = canvas.getCtx();ctx.beginPath();ctx.arc(pos.x, pos.y, radius, 0, Math.PI * 2, true);ctx.closePath();ctx[type]();}), contains:#10=(function (npos, pos, radius) {var diffx = npos.x - pos.x, diffy = npos.y - pos.y, diff = diffx * diffx + diffy * diffy;return diff <= radius * radius;})}, ellipse:{render:#11=(function (type, pos, width, height, canvas) {var ctx = canvas.getCtx(), scalex = 1, scaley = 1, scaleposx = 1, scaleposy = 1, radius = 0;if (width > height) {radius = width / 2;scaley = height / width;scaleposy = width / height;} else {radius = height / 2;scalex = width / height;scaleposx = height / width;}ctx.save();ctx.scale(scalex, scaley);ctx.beginPath();ctx.arc(pos.x * scaleposx, pos.y * scaleposy, radius, 0, Math.PI * 2, true);ctx.closePath();ctx[type]();ctx.restore();}), contains:#12=(function (npos, pos, width, height) {var radius = 0, scalex = 1, scaley = 1, diffx = 0, diffy = 0, diff = 0;if (width > height) {radius = width / 2;scaley = height / width;} else {radius = height / 2;scalex = width / height;}diffx = (npos.x - pos.x) * (1 / scalex);diffy = (npos.y - pos.y) * (1 / scaley);diff = diffx * diffx + diffy * diffy;return diff <= radius * radius;})}, square:{render:#13=(function (type, pos, dim, canvas) {canvas.getCtx()[type + "Rect"](pos.x - dim, pos.y - dim, 2 * dim, 2 * dim);}), contains:#14=(function (npos, pos, dim) {return Math.abs(pos.x - npos.x) <= dim && Math.abs(pos.y - npos.y) <= dim;})}, rectangle:{render:#15=(function (type, pos, width, height, canvas) {canvas.getCtx()[type + "Rect"](pos.x - width / 2, pos.y - height / 2, width, height);}), contains:#16=(function (npos, pos, width, height) {return Math.abs(pos.x - npos.x) <= width / 2 && Math.abs(pos.y - npos.y) <= height / 2;})}, triangle:{render:#17=(function (type, pos, dim, canvas) {var ctx = canvas.getCtx(), c1x = pos.x, c1y = pos.y - dim, c2x = c1x - dim, c2y = pos.y + dim, c3x = c1x + dim, c3y = c2y;ctx.beginPath();ctx.moveTo(c1x, c1y);ctx.lineTo(c2x, c2y);ctx.lineTo(c3x, c3y);ctx.closePath();ctx[type]();}), contains:
}