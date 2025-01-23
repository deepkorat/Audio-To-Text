# In this code I creat a python custom webserver
# Reference: https://pythonbasics.org/webserver/

# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys

hostName = "localhost"
serverPort = 8080

# Server creation
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
          self.send_response(200)
          self.send_header("Content-type", "text/html")
          self.end_headers()

          self.wfile.write(bytes("<html><head><title>Deep Korat</title></head>", "utf-8"))
          self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
          self.wfile.write(bytes("<body>", "utf-8"))
          self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
          self.wfile.write(bytes("</body></html>", "utf-8"))

         
# main function          
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down...")
        webServer.server_close()  # Close the server
        print("Server stopped.")
        sys.exit(0)  #