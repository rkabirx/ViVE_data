# Button to increase or decrease speed for Cruise control
# Send Acc/dec status as binary value to ECM ECU

def speed_change():
    import tkinter as tk
    import socket
    import time

    TCP_IP = "0.0.0.0"  # IP of RPI1
    TCP_PORT = 6602

    BUFFER_SIZE = 1024

    def maintain():
        MESSAGE = bytearray([0,0,1])  # sending 0 to denote TCS OFF

        # Sending to TCS via socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        s.send(MESSAGE)
        print("Sending signal to maintain current speed")
        data = s.recv(BUFFER_SIZE)
        s.close()
        # root.after(2000,lambda: root.destroy())

    maintain()

    def acc():
        MESSAGE = bytearray([0,0,2])  # sending 0 to denote TCS OFF

        # Sending to TCS via socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        s.send(MESSAGE)
        print("Sending signal to increase speed")
        data = s.recv(BUFFER_SIZE)
        s.close()
        root.after(2000,lambda: root.destroy())


    def dec():
        MESSAGE = bytearray([0,0,0])

        # Sending to TCS via socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        s.send(MESSAGE)
        print("Sending signal to decrease speed")
        data = s.recv(BUFFER_SIZE)
        s.close()
        root.after(2000,lambda: root.destroy())


    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    OFF = tk.Button(frame,
                    text="(-)speed",
                    fg="red",
                    command=dec)
    OFF.pack(side=tk.RIGHT)
    ON = tk.Button(frame,
                   text="(+)speed",
                   fg="green",
                   command=acc)
    ON.pack(side=tk.RIGHT)
    # M = tk.Button(frame,
    #               text="maintain",
    #               fg="blue",
    #               command=maintain)
    # M.pack(side=tk.RIGHT)
    # Quit = tk.Button(frame,
    #                  text="Quit",
    #                  command=quit)
    # Quit.pack(side=tk.RIGHT)
    # root.after(5000,lambda: root.destroy())  # Destroy the widget after 10 seconds
    root.mainloop()


if __name__ == '__main__':
    speed_change()
