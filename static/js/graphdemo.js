
var NodeClass = function(x, y) {
    this.x = x;
    this.y = y;
    this.contacts = [];
    this.newbie = true;
}

var w = 420,
    h = 380,
    k = 4,
    chance = 0.08,
    nodes = [],
    links = [],
    colors = d3.scale.linear().domain([1, k]).range(
        ["hsl(350, 50%, 50%)", "hsl(250, 100%, 50%)"]
        ).interpolate(d3.interpolateHsl);
;

var root_node = new NodeClass(w/2, h/2);
nodes.push(root_node);

$(function() {

var vis = d3.select(".hull").append("svg:svg")
    .attr("width", w)
    .attr("height", h);
/*
vis.append("svg:rect")
    .attr("width", w)
    .attr("height", h);
*/
var force = d3.layout.force()
    .nodes(nodes)
    .links(links)
    .linkDistance(7)
    .size([w, h]);

var cursor = vis.append("svg:circle")
    .attr("r", 30)
    .attr("transform", "translate(-100,-100)")
    .attr("class", "cursor");

force.on("tick", function() {
  vis.selectAll("line.link")
      .attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  vis.selectAll("circle.node")
      .attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; })
      .filter(function(d) { return ! d.newbie; })
      .attr("fill", function(d) { return colors(d.contacts.length); });
});

vis.on("mousemove", function() {
//  cursor.attr("transform", "translate(" + d3.svg.mouse(this) + ")");
});

function new_node() {
  var node = new NodeClass(Math.random() * w, Math.random() * h),
      shufd = _.shuffle(nodes);

  // add links to any nearby nodes
  for (var i = 0; i < shufd.length; i++) {
    var target = shufd[i];
//    console.log(target);
    if (target.contacts.length < k) {
      links.push({source: node, target: target});
      target.contacts.push(node);
      break;
    }
  }
  nodes.push(node);
  restart();
}

function new_nodesss() {
    var n = Math.ceil(Math.log(nodes.length));
//    console.log(n);
    if (n <= 0) { n = 1; };
    for (;n>0;n--) {
        new_node();
    }
}

function new_node_2() {
  var newnodes = [];
  for (var i = 0; i < nodes.length; i++) {
    var target = nodes[i];
    var ratio = target.contacts.length / k; //(target.contacts.length == 0)
    var n = 1 - ratio;
    if (target.contacts.length < k && ((n * Math.random()) <= chance)) {
      var node = new NodeClass(
        target.x + (Math.random() - 0.5) * 10,
        target.y + (Math.random() - 0.5) * 10
      );
      links.push({source: node, target: target});
      target.contacts.push(node);
      node.contacts.push(target);
      newnodes.push(node);
    }
  }
  _.each(newnodes, function(n){ nodes.push(n);});
  restart();
  return newnodes;
}

function runloop() {
//    window.setTimeout(runloop, 1000);
    var newnodes;
    while (true) {
        newnodes = new_node_2();
        var count = newnodes.length;
        if (count > 0) {
            console.log(count);
            break;
        }
    };

}

//runloop();
//vis.on("mousedown", new_nodesss);
vis.on("mousedown", runloop);


restart();

function restart() {

  vis.selectAll("line.link")
      .data(links)
    .enter().insert("svg:line", "circle.node")
      .attr("class", "link")
      .attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  vis.selectAll("circle.node")
      .data(nodes)
    .enter().insert("svg:circle", "circle.cursor")
      .attr("class", "node")
      .attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; })
      .attr("r", 5)
      .attr("fill", "yellow")
      .call(force.drag)
    .transition()
      .duration(150)
      .attr("fill", function(d) { return colors(d.contacts.length); })
      .each("end", function(d) {
        d.newbie = false;
      });

  force.start();
}

});

