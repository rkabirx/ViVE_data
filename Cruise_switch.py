# Cruise button to switch ON or OFF the Cruise control
# Send ON/OFF status as binary value to BCM ECU

def CS():
    import tkinter as tk
    import socket

    import time

    TCP_IP = "0.0.0.0"  # IP of RPI1
    TCP_PORT = 6600

    BUFFER_SIZE = 1024

    def CS_OFF():
        MESSAGE = bytearray([0])  # sending 0 to denote TCS OFF
        # Sending to BCM via socket
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending Cruise OFF status")
            data = s.recv(BUFFER_SIZE)
            s.close()
        except:
            socket.error

    CS_OFF()

    def CS_ON():
        MESSAGE = bytearray([1])  # sending 0 to denote TCS OFF
        # Sending to BCM via socket
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending Cruise ON status")
            data = s.recv(BUFFER_SIZE)
            s.close()
        except:
            socket.error

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    ON = tk.Button(frame,
                   text="Cruise ON",
                   fg="green",
                   command=CS_ON)
    ON.pack(side=tk.LEFT)

    OFF = tk.Button(frame,
                    text="Cruise OFF",
                    fg="red",
                    command=CS_OFF)
    OFF.pack(side=tk.RIGHT)

    # root.after(5000, lambda: root.destroy())  # Destroy the widget after 10 seconds
    root.mainloop()


if __name__ == '__main__':
    CS()
