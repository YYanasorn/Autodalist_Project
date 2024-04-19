import snap7
from snap7 import util
from datetime import datetime

def snapRunA():
    counterDword = [0]
    counterReal = [16, 52, 88, 124, 196, 232, 268, 304, 376, 340, 160]
    client = snap7.client.Client()
    client.connect('192.168.1.15', 0, 1)
    client.get_connected()

    
    values = ["A", datetime.now().strftime("%Y-%m-%d %H:%M")]

    for countDword in counterDword:
        db_Dword = client.db_read(60, countDword, 4)
        d = util.get_dint(db_Dword, 0)
        d_formatted = "{:.2f}".format(d)
        values.append(d_formatted)


    for countReal in counterReal:
        db_real = client.db_read(88, countReal, 4)
        t = util.get_real(db_real, 0)
        t_formatted = "{:.2f}".format(t)
        values.append(t_formatted)

    client.disconnect()

    parameters = Parameter_test()
    formatted_data = {}

    for idx, (key, value) in enumerate(parameters.items(), start=0):
        formatted_data[value] = values[idx]

    return formatted_data


def snapRunB():
    counterDword = [0]
    counterReal = [16, 52, 88, 124, 196, 232, 268, 304, 376, 340, 160]
    client = snap7.client.Client()
    client.connect('192.168.1.12', 0, 1)
    client.get_connected()

    
    values = ["B", datetime.now().strftime("%Y-%m-%d %H:%M")]

    for countDword in counterDword:
        db_Dword = client.db_read(60, countDword, 4)
        d = util.get_dint(db_Dword, 0)
        d_formatted = "{:.2f}".format(d)
        values.append(d_formatted)


    for countReal in counterReal:
        db_real = client.db_read(88, countReal, 4)
        t = util.get_real(db_real, 0)
        t_formatted = "{:.2f}".format(t)
        values.append(t_formatted)

    client.disconnect()

    parameters = Parameter_test()
    formatted_data = {}

    for idx, (key, value) in enumerate(parameters.items(), start=0):
        formatted_data[value] = values[idx]

    return formatted_data

def Parameter_test():
    parameters = {
        'comp':'parameter0', 'time': 'Parameter1', 'hourMeter': 'Parameter2', 'InletPressure': 'Parameter3', 
        'St1_Pressure': 'Parameter4', 'Discharge': 'Parameter5', 'CompOilPressure': 'Parameter6', 
        'Stage1_1Temp': 'Parameter7', 'Stage1_2Temp': 'Parameter8', 'Stage2_1Temp': 'Parameter9', 
        'Stage2_2Temp': 'Parameter10', 'GasDetec': 'Parameter11', 'CompOilTemp': 'Parameter12', 
        'MotorCur': 'Parameter13' 
    }
    return parameters


if __name__ == "__main__":
    values = snapRunA()
    print(values)
    values = snapRunB()
    print(values)