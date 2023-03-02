from multiprocessing import Process

import Acc_dec_switch
import Cruise_switch
import WheelSpeed_sensor
import Brake_pedal
import Acc_pedal

def func1() :
    Cruise_switch.CS()

def func2() :
    Brake_pedal.brake_send(6601)

def func3() :
    Acc_dec_switch.speed_change()

def func4() :
    Acc_pedal.acc_pedal(6622)

def func5() :
    WheelSpeed_sensor.send(6622) # In this way, can change port numbers for different use cases




if __name__ == '__main__' :
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p3 = Process(target=func3)
    p3.start()
    # p4 = Process(target=func4)
    # p4.start()
    # p5 = Process(target=func5)
    # p5.start()