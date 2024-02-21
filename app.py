from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    try:
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()
    except KeyboardInterupt:
        print('apagando server')
        http.socket.close()
        
if __name__ == "__main__":
    run()