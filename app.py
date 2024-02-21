from http.server import HTTPServer, SimpLeHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpLeHTTPRequestHandler):
    try:
        server_address = ('', 8000)
        httpd = server_class(server_addres, handler_class)
        print('Iniciando servidor web en http://localhost:8000/')
        httpd.server_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socked.close()

if _name_ == "_main_":
    run()