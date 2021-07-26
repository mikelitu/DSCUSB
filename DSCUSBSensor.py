import ctypes

class Sensor():

    def __init__(self, COMPort):

        """
        :param COMPort (int): The port where the DSCUSB is located in your computer

        This function loads the library containing the functions to establish an ASCII connection with the DSCUSB,
        and opens the port to start sending commands
        """

        print("Creating connection with DSCUSB Sensor at COM", COMPort)

        self.dll = ctypes.WinDLL("C:\\Windows\\System32\\MantraASCII2Drv.dll")

        isOpen = self.dll.OPENPORT(
            ctypes.c_int (COMPort),
            ctypes.c_long (115200)
        )

        if isOpen==0:
            print("The connection is established!")
        else:
            self.GetErrors(isOpen)

    def close(self):
        """
        Closes the port and ends the connection
        """

        isClose = self.dll.CLOSEPORT()

        if isClose==0:
            print("Connection finished")
        else:
            self.GetErrors(isClose)

    def readvalue(self):

        """
        :return: The value of the load cell

        This function generates a command to ask for the value in the load cell. In this case, the command will be SYS
        corresponding to the main output. It automatically transforms the value back to a Python floating variable.
        """

        command = ctypes.create_string_buffer(255)
        command.value = b"SYS"

        result = ctypes.c_float(0.0)

        value = self.dll.READCOMMAND(
            ctypes.c_int(1),
            command,
            ctypes.byref(result)
        )

        if value==0:
            return result.value
        else:
            self.GetErrors(value)

    def version(self):
        return self.dll.VERSION()

    def GetErrors(self, value):

        """
        :param value: The values return by the MantraASCII2Drv.dll
        :return: Returns the type of error the program has
        """

        if value == -1:
            raise ValueError("Invalid argument value in function call")
        elif value == -2:
            raise ValueError("Cannot open or close serial port")
        elif value == -100:
            raise ValueError("No response")
        elif value == -200:
            raise ValueError("Invalid station number in response")
        elif value == -300:
            raise ValueError("Invalid checksum")
        elif value == -400:
            raise ValueError("Not acknowledge (NAK)")
        elif value == -500:
            raise ValueError("Invalid reply length")
