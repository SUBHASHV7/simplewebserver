from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<h1>
<table align="center" border="1" bgcolor="cyan" cellpadding="10">
    <caption>LIST OF PROTOCOL IN TCP/IP PROTOCOLSUITE </caption>
    <tr ><th bgcolor="brown">S.No.</th><th bgcolor="brown">Name of the layers</th><th bgcolor="brown"> Name of the protocol</th></tr>
    <tr><td bgcolor="red">1</td><td bgcolor="red">Application Layer</td><td bgcolor="red">HTTP,FTP,DNS,Telnet & SS <br> </td></tr>
    <tr><td bgcolor="pink">2</td><td bgcolor="pink">Transport Layer </td><td bgcolor="pink">TCP & UDP <br> </td></tr>
    <tr><td bgcolor="red">3</td><td bgcolor="red"> Network Layer </td><td bgcolor="red">IPV4/IPV6 <br> </td></tr>
    <tr><td bgcolor="pink">4</td><td bgcolor="pink">Link Layer</td><td bgcolor="pink">Ethernet<br> </td></tr>
</table>
   
</h1>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()