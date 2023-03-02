

def us_sensor() :
    import tkinter as tk
    import socket
    import time
    import numpy as np

    TCP_IP = "0.0.0.0"
    TCP_PORT = 5061

    BUFFER_SIZE = 1024

    def us_OFF():

        MESSAGE = bytearray([0,0,0])
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending No collision signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error

    us_OFF()

    def us_ON() :
        MESSAGE = bytearray([0,0,1])
        try:
            # Sending to park assist ECU
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending collision signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error

    def random_press():
        random_value = np.random.randint(2, size=10)
        for x in random_value:
            MESSAGE = bytearray([0,0,x])
            try :
                # Sending to park assist ECU
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((TCP_IP,TCP_PORT))
                s.send(MESSAGE)
                print("Sending automatic random signal: ",x)
                data = s.recv(BUFFER_SIZE)
                s.close()
                time.sleep(5)
            except :
                socket.error

    while True:
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()

        OFF = tk.Button(frame,
                        text="No collision",
                        fg="red",
                        command=us_OFF)
        OFF.pack(side=tk.LEFT)
        ON = tk.Button(frame,
                       text="Collision",
                       fg="green",
                       command=us_ON)
        ON.pack(side=tk.LEFT)
        random = tk.Button(frame,
                       text="Auto random generate",
                       fg="blue",
                       command=random_press)
        random.pack(side=tk.RIGHT)
        root.mainloop()


if __name__ == '__main__' :
    us_sensor()
