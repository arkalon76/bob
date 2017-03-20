import socketserver, os
from configparser import ConfigParser

"""
Byte
[1] = Action 255 items
"""


class BOBServer(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    config_filename = 'bobsrv-config.ini'

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024)
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data)

    def crete_init_configfile():
        config = ConfigParser()
        config['Server'] = {'port': 7766,
                            'host': "localhost"}
        with open(BOBServer.config_filename, 'w') as configfile:
            config.write(configfile)
        config.read_file(open(BOBServer.config_filename))
        return config

    """
    Load's the server config file. If it cannot find one, it will create a basic one
    """
    def load_config_file():
        config = ConfigParser()
        try:
            config.read_file(open(BOBServer.config_filename))
            return config
        except FileNotFoundError:
            return BOBServer.crete_init_configfile();

if __name__ == "__main__":
    """
    Let's setup the configuration
    """
    config = loadConfigFile()
    HOST, PORT = config['server']['host'], config['server']['port']

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), BOBServer) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
