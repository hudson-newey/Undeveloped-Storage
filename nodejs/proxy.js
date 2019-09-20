var http = require('http');
var request = require("request");
var url = require('url');

http.createServer(function (req, res) {
  var q = url.parse(req.url, true).query; // parse what website the user wants
  var website = q.q;
  request({
    uri: website,
  }, function(error, response, body) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(("" + body).toString(36));
    res.end();
  });
}).listen(8080);
