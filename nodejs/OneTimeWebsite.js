var http = require('http');
var fs = require('fs');

http.createServer(function (req, res) {
  var page = req.url; // remove the slash at the start of the page
  page = page.substring(1);

  fs.readFile(page, function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
  });
}).listen(8080);
