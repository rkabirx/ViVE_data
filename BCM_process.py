from threading import Thread,Lock

import time
import socket
import numpy as np
lock = Lock()

class dual_thread(Thread):

    def __init__(self,conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):

        BUFFER_SIZE1 = 1024  # Normally 1024, but we want fast response

        print("-----------------------------------------------------------------")
        print('Starting a new connection')

        packet = self.conn.recv(BUFFER_SIZE1)
        received_array = list(packet)
        print("Closing receiver socket")
        print("Received packet: ", received_array)
        # print(len(received_array))
        if len(received_array) == 1:
            np.save('cruise_switch.npy', received_array[0])
        elif len(received_array) == 2:
            np.save('cruise_brake.npy', received_array[1])
        else:
            np.save('cruise_acdc.npy', received_array[2])

        print("Out of receiver for loop")

        self.conn.close()


        bcm1 = np.load('cruise_switch.npy')
        bcm2 = np.load('cruise_brake.npy')
        bcm3 = np.load('cruise_acdc.npy')
        if (bcm1 == 0) & (bcm2 == 0) & (bcm3 == 0):
            bcm_array = [0]
        elif (bcm1 == 0) & (bcm2 == 0) & (bcm3 == 1):
            bcm_array = [1]
        elif (bcm1 == 0) & (bcm2 == 0) & (bcm3 == 2):
            bcm_array = [2]
        elif (bcm1 == 0) & (bcm2 == 1) & (bcm3 == 0):
            bcm_array = [10]
        elif (bcm1 == 0) & (bcm2 == 1) & (bcm3 == 1):
            bcm_array = [11]
        elif (bcm1 == 0) & (bcm2 == 1) & (bcm3 == 2):
            bcm_array = [12]
        elif (bcm1 == 1) & (bcm2 == 0) & (bcm3 == 0):
            bcm_array = [100]
        elif (bcm1 == 1) & (bcm2 == 0) & (bcm3 == 1):
            bcm_array = [101]
        elif (bcm1 == 1) & (bcm2 == 0) & (bcm3 == 2):
            bcm_array = [102]
        elif (bcm1 == 1) & (bcm2 == 1) & (bcm3 == 0):
            bcm_array = [110]
        elif (bcm1 == 1) & (bcm2 == 1) & (bcm3 == 1):
            bcm_array = [111]
        else:
            bcm_array = [112]


        time.sleep(3)

        receiving_completed_flag = 1

        print("bcm array: ", bcm_array)
        # Sender socket
        if receiving_completed_flag == 1:
            TCP_IP = "0.0.0.0"
            TCP_PORT = 5003  # port for 1st payload (is_extended_id)
            BUFFER_SIZE = 1024

            from can import Message

            # Here can_msg is the CAN frame to be sent as 3 payloads
            can_msg = Message(is_extended_id=False, arbitration_id=9, data=bcm_array)

            print(can_msg)  # printing CAN frame

            # converting is_extended_id to sent via socket
            bool_val = can_msg.is_extended_id
            # Converting boolean to integer
            if bool_val:
                bool_val = 1
            else:
                bool_val = 0

            Payload1 = [bool_val]
            Payload2 = [can_msg.arbitration_id]
            Payload3 = list(can_msg.data)
            msg_array = Payload1 + Payload2 + Payload3
            Payload = bytearray(msg_array)
            print("Sending payload array: ", msg_array)

            # Sending the CAN frame to CAN simulator via socket

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            s.send(Payload)
            data1 = s.recv(BUFFER_SIZE)
            s.close()


def bcm():
    TCP_IP = "0.0.0.0"
    TCP_PORT = 6602

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((TCP_IP,TCP_PORT))
    # log.info('Created a socket')
    print(f"Connecting receiver socket with port {TCP_PORT}")
    s.listen(1)
    print("Receiver is waiting for a connection...")

    while True:  # Check if this is right -> This is to make receiver from one socket and sender to other socket in 1 loop

        conn,addr = s.accept()
        conn.setblocking(0)

        thread2 = dual_thread(conn)
        thread2.start()



if __name__ == '__main__':
    bcm()