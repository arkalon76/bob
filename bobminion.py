import socket, sys, time, argparse

class BOBMinion():

    HOST, PORT = "localhost", 7766

    data = bytearray([0x33,0x66,0xFF])

    def connect_with_bob(port = PORT):
        while True:
            time.sleep(1)
            # Create a socket (SOCK_STREAM means a TCP socket)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to server and send data
                print(port)
                sock.connect((BOBMinion.HOST, port))
                sock.sendall(BOBMinion.data)

                # Receive data from the server and shut down
                received = sock.recv(1024)
            print("Sent:     {}".format(BOBMinion.data))
            print("Received: {}".format(received))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A trusty minion of Bob the server',
                                     epilog='I love banana!! -minion')
    parser.add_argument("-p", "--port", type=int , help="Must be the same port as BOB. Default8")
    args = parser.parse_args()
    print(args.port)
    if args.port == None:
        BOBMinion.connect_with_bob()
    else:
        BOBMinion.connect_with_bob(port = args.port)
