import time
import serial
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM4',
    baudrate=115200,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()


while 1 :
        #input = str(1)
        command = input()
        ser.write(command.encode())
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            print(">>" + ser.readline().decode("gb18030"))
            # out += ser.read(1)

        # if out != '':
            # print(">>" + out)