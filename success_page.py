from http.server import SimpleHTTPRequestHandler, HTTPServer

class RequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

def main():
    try:
        port = 8002  # You can change this port if needed
        server = HTTPServer(('localhost', port), RequestHandler)
        print(f'Starting server on port {port}...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')

if __name__ == '__main__':
    main()
