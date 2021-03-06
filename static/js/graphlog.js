var node_urls = [
  "http://phoenixbureau.org/",
  "http://www.phoenixbureau.org/",
  "http://firequery.blogspot.com/",
  "http://denebii:5000/",
  "http://openkeyval.org/",
  "https://wiki.ubuntu.com/",
  "https://twitter.com/SimonForman",
  "https://github.com/PhoenixBureau/DendNet"
];

var bumps = {
  "https://wiki.ubuntu.com/": [
    [
      "https://twitter.com/SimonForman", 
      "http://phoenixbureau.org/"
    ], 
    [
      "http://firequery.blogspot.com/", 
      "https://twitter.com/SimonForman"
    ]
  ], 
  "http://denebii:5000/": [
    [
      "http://www.phoenixbureau.org/", 
      "https://github.com/PhoenixBureau/DendNet"
    ]
  ], 
  "http://openkeyval.org/": [
    [
      "http://www.phoenixbureau.org/", 
      "https://github.com/PhoenixBureau/DendNet"
    ]
  ], 
  "http://phoenixbureau.org/": [
    [
      "http://phoenixbureau.org/", 
      "http://firequery.blogspot.com/"
    ], 
    [
      "http://firequery.blogspot.com/", 
      "http://phoenixbureau.org/"
    ], 
    [
      "http://firequery.blogspot.com/", 
      "https://twitter.com/SimonForman"
    ]
  ]
}

var NodeClass = function(x, y, url) {
    this.x = x;
    this.y = y;
    this.url = url;
}

var w = 420,
    h = 380,
    k = 4,
    chance = 0.08,
    links = [],
    colors = d3.scale.linear().domain([1, k]).range(
        ["hsl(350, 50%, 50%)", "hsl(250, 100%, 50%)"]
        ).interpolate(d3.interpolateHsl);


function update_select() {
  _.each(bumps, function(value, key) {
    var opt = $("<option></option>", {value: key, text: key});
    $('#meme_selector').append(opt);
  });
}

$(function() {

var nodes = _.map(node_urls, function(node_url) {
  var node = new NodeClass((w/2) + (Math.random() - 0.5) * 10,
                           (h/2) + (Math.random() - 0.5) * 10,
                           node_url);
  return node
});

function get_node_from_url(url) {
  return _.find(nodes, function(node) {
    return node.url == url;
  })
}

$('#meme_selector').change(function() {
  var meme = $(this).val();
  var meme_graph = bumps[meme];
  links.length = 0;
  restart();
  _.each(meme_graph, function(pair) {
    var from_ = get_node_from_url(pair[0]);
    var to_ = get_node_from_url(pair[1]);
    links.push({source: from_, target: to_})
  });
  restart();
})

var vis = d3.select(".hull").append("svg:svg")
    .attr("width", w)
    .attr("height", h);

var force = d3.layout.force()
    .nodes(nodes)
    .links(links)
    .linkDistance(17)
    .size([w, h]);

force.on("tick", function() {
  vis.selectAll("line.link")
      .attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  vis.selectAll("circle.node")
      .attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; })
      .attr("fill", function(d) { return colors(2); });
});

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
      .attr("fill", "grey")
      .call(force.drag);

  force.start();
}

update_select();
restart();

});

