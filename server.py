#!/usr/bin/env python
# coding: utf-8

import socket
import cv2
import numpy as np
import sys
import argparse
import threading
import time
import logging

class Broker():



    def __init__(self):
        logging.info('Initializing Broker')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_address = ('127.0.0.1', 5000)
        self.sock.bind(self.server_address)
        self.clients_list = []
        self.sock.setblocking(0)

    def talkToClient(self):

        frame_idx = 0
        buffer_array = []
        t0 = time.time()
        broadcast_frame_idx = 0;

        while True:

            data, address = self.sock.recvfrom(65507)
            if data == b'000000000000000000000000000000000000000000000000000':
                print('requested from army')
                self.sock.sendto(buffer_array[len(buffer_array) - 1], address)
                broadcast_frame_idx += 1
            elif len(data) > 10000:
                print('requested from camera')
                self.sock.sendto("from server saying hello to camera".encode('utf-8'), address)
                buffer_array.append(data)
                cv2.waitKey(1)
            else:
                self.sock.sendto("kaduna".encode('utf-8'), address)

            logging.info("Sending 'ok' to %s", address)


    def listen_clients(self):



            logging.info('Received data from client: %s', address)
            t = threading.Thread(target=self.talkToClient, args=(address,))
            t.start()
            return data, address



if __name__ == '__main__':
    # Make sure all log messages show up
    logging.getLogger().setLevel(logging.DEBUG)

    b = Broker()
    b.talkToClient()

# parser = argparse.ArgumentParser()
# parser.add_argument('--port', type=int, help='The port on which the server is listening', required=True)
# parser.add_argument('--jpeg_quality', type=int, help='The JPEG quality for compressing the reply', default=50)
# parser.add_argument('--encoder', type=str, choices=['cv2','turbo'], help='Which library to use to encode/decode in JPEG the images', default='cv2')



# args = parser.parse_args()

# cv2.namedWindow("Image")

# t0 = time.time()
# frame_idx = 0
#
# keep_running = True

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# downstream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# host = ''
# port = args.port
#
# # Bind the socket to the port
# server_address = (host, port)
# downstream_server_address = (host, 6000)

# print('starting up on %s port %s\n' % server_address)
#
# sock.bind(server_address)
# # downstream_socket.bind(downstream_server_address)

# buffer_array = []

# while True:
#     data, address = sock.recvfrom(65507)

    # if data:
    #     try:
    #         data = data.decode('utf-8')
    #         if data == "get":
    #             print("Requested from stf")
    #             if len(buffer_array) > 0:
    #                 sock.sendto(buffer_array[len(buffer_array) - 1], address)
    #             else:
    #                 sock.sendto(bytes(4), address)
    #         continue
    #     except:
    #         hello = "as"
    #         sock.sendto(bytes(4), address)
    # if data == b'get':
    #     # try:
    #     print(data)
    #     data1 = data.decode('utf-8')
    #     print('requested from stf')
    #     sock.sendto("from server saying hello".encode('utf-8'), address1)
    #     # except:
    #     # sock.sendto('lula'.encode('utf-8'), address1)
    #
    # if len(data) > 15000:
    #     buffer_array.append(data)
    #     array = np.frombuffer(data, dtype=np.dtype('uint8'))
    #     img = cv2.imdecode(array, 1)
    #     cv2.imshow("Image", img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         print("Asking the server to quit")
    #         sock.sendto("quit".encode('utf-8'), server_address)
    #         print("Quitting")
    #         break
    #     frame_idx += 1
    #
    #     if frame_idx == 30:
    #         t1 = time.time()
    #         sys.stdout.write('\r Framerate : {:.2f} frames/s.     '.format(30 / (t1 - t0)))
    #         sys.stdout.flush()
    #         t0 = t1
    #         frame_idx = 0
    #
    # elif data == "quit":
    #     keep_running = False
#
#
# print("Quitting..")
# sock.close()
