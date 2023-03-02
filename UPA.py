
import threading
from threading import Thread,Lock
from tkinter import *
import socket
import numpy as np

class listener_thread(Thread):

    def __init__(self,conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):
        global myarray

        BUFFER_SIZE1 = 1024  # Normally 1024, but we want fast response

        print("-----------------------------------------------------------------")
        print('Starting a new connection')

        packet = self.conn.recv(BUFFER_SIZE1)
        received_array = list(packet)
        print("Closing receiver socket")
        print("Received packet: ", received_array)
        # print(len(received_array))

        self.conn.close()
        print("Out of receiver for loop")


def upa_recv():
    TCP_IP = "0.0.0.0"
    TCP_PORT = 5061

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((TCP_IP,TCP_PORT))
    # log.info('Created a socket')
    print(f"Connecting receiver socket with port {TCP_PORT}")
    s.listen(1)
    print("Receiver is waiting for a connection...")

    while True:  # Check if this is right -> This is to make receiver from one socket and sender to other socket in 1 loop

        conn,addr = s.accept()
        conn.setblocking(0)

        thread2 = listener_thread(conn)
        thread2.start()




class upa_thread(Thread):

    def __init__(self,conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):
        global myarray

        BUFFER_SIZE1 = 1024  # Normally 1024, but we want fast response

        print("-----------------------------------------------------------------")
        print('Starting a new connection')

        packet = self.conn.recv(BUFFER_SIZE1)
        datalist = list(packet)
        print("Closing receiver socket")
        print("Received packet: ", datalist)

        self.conn.close()
        print("Out of receiver for loop")

        from can import Message  # importing CAN frame using python-can library
        # can_msg is the assembled CAN frame with received payloads
        can_msg = Message(is_extended_id=bool(datalist[0]),arbitration_id=datalist[1],data=datalist[2 :])
        print("Assembled CAN frame: ",can_msg)

        torque_reduction = datalist[2]

        print("Collision alert" % datalist[2])

        def print_output() :
            # if you want the button to disappear:
            # button.destroy() or button.pack_forget()
            label = Label(root,text=("Collision alert" % datalist[2]))
            label.config(width=32,font=("Courier",16))
            # this creates x as a new label to the GUI
            label.pack()

        root = Tk()
        root.after(3000,lambda : root.destroy())
        button = Button(root,command=print_output)
        button.pack()

        print_output()
        root.mainloop()



def upa():
    TCP_IP = "0.0.0.0"
    TCP_PORT = 5099

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((TCP_IP,TCP_PORT))
    # log.info('Created a socket')
    print(f"Connecting receiver socket with port {TCP_PORT}")
    s.listen(1)
    print("Receiver is waiting for a connection...")

    while True:  # Check if this is right -> This is to make receiver from one socket and sender to other socket in 1 loop

        conn,addr = s.accept()
        conn.setblocking(0)

        thread = upa_thread(conn)
        thread.start()


if __name__ == '__main__':
    threading.Thread(target=upa_recv).start()
    threading.Thread(target=upa).start()


























