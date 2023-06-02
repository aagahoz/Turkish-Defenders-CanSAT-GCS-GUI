class TelemetryData:
    def __init__(self):
        self.team_id = None
        self.mission_time = None
        self.packet_count = None
        self.mode = None
        self.state = None
        self.altitude = None
        self.hs_deployed = None
        self.pc_deployed = None
        self.mast_raised = None
        self.temp = None
        self.pressure = None
        self.volt = None
        self.gps_time = None
        self.gps_altitude = None
        self.gps_latitude = None
        self.gps_longitude = None
        self.gps_sats = None
        self.tilt_x = None
        self.tilt_y = None
        self.cmd_echo = None
        self.accelX = None
        self.accelY = None
        self.accelZ = None
    
    # give set get functions

    def set_team_id(self, team_id):
        self.team_id = team_id

    def get_team_id(self):
        return str(self.team_id)
    
    def set_mission_time(self, mission_time):
        self.mission_time = mission_time

    def get_mission_time(self):
        return str(self.mission_time)
    
    def set_packet_count(self, packet_count):
        self.packet_count = packet_count

    def get_packet_count(self):
        return str(self.packet_count)
    
    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return str(self.mode)
    
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return str(self.state)
    
    def set_altitude(self, altitude):
        self.altitude = altitude

    def get_altitude(self):
        return str(self.altitude)
    
    def set_hs_deployed(self, hs_deployed):
        self.hs_deployed = hs_deployed

    def get_hs_deployed(self):
        return str(self.hs_deployed)
    
    def set_pc_deployed(self, pc_deployed):
        self.pc_deployed = pc_deployed

    def get_pc_deployed(self):
        return str(self.pc_deployed)
    
    def set_mast_raised(self, mast_raised):
        self.mast_raised = mast_raised

    def get_mast_raised(self):
        return str(self.mast_raised)
    
    def set_temp(self, temp):
        self.temp = temp

    def get_temp(self):
        return str(self.temp)
    
    def set_pressure(self, pressure):
        self.pressure = pressure

    def get_pressure(self):
        return str(self.pressure)
    
    def set_volt(self, volt):
        self.volt = volt

    def get_volt(self):
        return str(self.volt)
    
    def set_gps_time(self, gps_time):
        self.gps_time = gps_time

    def get_gps_time(self):
        return str(self.gps_time)
    
    def set_gps_altitude(self, gps_altitude):
        self.gps_altitude = gps_altitude

    def get_gps_altitude(self):
        return str(self.gps_altitude)
    
    def set_gps_latitude(self, gps_latitude):
        self.gps_latitude = gps_latitude

    def get_gps_latitude(self):
        return str(self.gps_latitude)
    
    def set_gps_longitude(self, gps_longitude):
        self.gps_longitude = gps_longitude

    def get_gps_longitude(self):
        return str(self.gps_longitude)
    
    def set_gps_sats(self, gps_sats):
        self.gps_sats = gps_sats

    def get_gps_sats(self):
        return str(self.gps_sats)
    
    def set_tilt_x(self, tilt_x):
        self.tilt_x = tilt_x

    def get_tilt_x(self):
        return str(self.tilt_x)
    
    def set_tilt_y(self, tilt_y):
        self.tilt_y = tilt_y

    def get_tilt_y(self):
        return str(self.tilt_y)
    
    def set_cmd_echo(self, cmd_echo):
        self.cmd_echo = cmd_echo

    def get_cmd_echo(self):
        return str(self.cmd_echo)
    
    def set_accelX(self, accelX):
        self.accelX = accelX

    def get_accelX(self):
        return str(self.accelX)
    
    def set_accelY(self, accelY):
        self.accelY = accelY

    def get_accelY(self):
        return str(self.accelY)
    
    def set_accelZ(self, accelZ):
        self.accelZ = accelZ
    

    def __str__(self):
        return "team_id: " + str(self.team_id) + "\n" + "mission_time: " + str(self.mission_time) + "\n" + "packet_count: " + str(self.packet_count) + "\n" + "mode: " + str(self.mode) + "\n" + "state: " + str(self.state) + "\n" + "altitude: " + str(self.altitude) + "\n" + "hs_deployed: " + str(self.hs_deployed) + "\n" + "pc_deployed: " + str(self.pc_deployed) + "\n" + "mast_raised: " + str(self.mast_raised) + "\n" + "temp: " + str(self.temp) + "\n" + "pressure: " + str(self.pressure) + "\n" + "volt: " + str(self.volt) + "\n" + "gps_time: " + str(self.gps_time) + "\n" + "gps_altitude: " + str(self.gps_altitude) + "\n" + "gps_latitude: " + str(self.gps_latitude) + "\n" + "gps_longitude: " + str(self.gps_longitude) + "\n" + "gps_sats: " + str(self.gps_sats) + "\n" + "tilt_x: " + str(self.tilt_x) + "\n" + "tilt_y: " + str(self.tilt_y) + "\n" + "cmd_echo: " + str(self.cmd_echo) + "\n" + "accelX: " + str(self.accelX) + "\n" + "accelY: " + str(self.accelY) + "\n" + "accelZ: " + str(self.accelZ) + "\n"

    def set_all_values_to_zero(self):
        self.mission_time = 0
        self.packet_count = 0
        self.mode = 0
        self.state = 0
        self.altitude = 0
        self.hs_deployed = 0
        self.pc_deployed = 0
        self.mast_raised = 0
        self.temp = 0
        self.pressure = 0
        self.volt = 0
        self.gps_time = 0
        self.gps_altitude = 0
        self.gps_latitude = 0
        self.gps_longitude = 0
        self.gps_sats = 0
        self.tilt_x = 0
        self.tilt_y = 0
        self.cmd_echo = 0
        self.accelX = 0
        self.accelY = 0
        self.accelZ = 0

    def returnAsList(self):
        tempList = list()
        tempList.append(str(self.team_id))
        tempList.append(str(self.mission_time))
        tempList.append(str(self.packet_count))
        tempList.append(str(self.mode))
        tempList.append(str(self.state))
        tempList.append(str(self.altitude))
        tempList.append(str(self.hs_deployed))
        tempList.append(str(self.pc_deployed))
        tempList.append(str(self.mast_raised))
        tempList.append(str(self.temp))
        tempList.append(str(self.pressure))
        tempList.append(str(self.volt))
        tempList.append(str(self.gps_time))
        tempList.append(str(self.gps_altitude))
        tempList.append(str(self.gps_latitude))
        tempList.append(str(self.gps_longitude))
        tempList.append(str(self.gps_sats))
        tempList.append(str(self.tilt_x))
        tempList.append(str(self.tilt_y))
        tempList.append(str(self.cmd_echo))
        tempList.append(str(self.accelX))
        tempList.append(str(self.accelY))
        tempList.append(str(self.accelZ))

        return tempList
        

    def getDataAsList(self):
        dataS = list()
        dataS.append(str(self.team_id))
        dataS.append(str(self.mission_time))
        dataS.append(str(self.packet_count))
        dataS.append(str(self.mode))
        dataS.append(str(self.state))
        dataS.append(str(self.altitude))
        dataS.append(str(self.hs_deployed))
        dataS.append(str(self.pc_deployed))
        dataS.append(str(self.mast_raised))
        dataS.append(str(self.temp))
        dataS.append(str(self.pressure))
        dataS.append(str(self.volt))
        dataS.append(str(self.gps_time))
        dataS.append(str(self.gps_altitude))
        dataS.append(str(self.gps_latitude))
        dataS.append(str(self.gps_longitude))
        dataS.append(str(self.gps_sats))
        dataS.append(str(self.tilt_x))
        dataS.append(str(self.tilt_y))
        dataS.append(str(self.cmd_echo))
        dataS.append(str(self.accelX))
        dataS.append(str(self.accelY))
        dataS.append(str(self.accelZ))
    
        return dataS
    
    def getDataCommaSeparated(self):
        dataS = str()
        dataS += str(self.team_id)
        dataS += ","
        dataS += str(self.mission_time)
        dataS += ","
        dataS += str(self.packet_count)
        dataS += ","
        dataS += str(self.mode)
        dataS += ","
        dataS += str(self.state)
        dataS += ","
        dataS += str(self.altitude)
        dataS += ","
        dataS += str(self.hs_deployed)
        dataS += ","
        dataS += str(self.pc_deployed)
        dataS += ","
        dataS += str(self.mast_raised)
        dataS += ","
        dataS += str(self.temp)
        dataS += ","
        dataS += str(self.pressure)
        dataS += ","
        dataS += str(self.volt)
        dataS += ","
        dataS += str(self.gps_time)
        dataS += ","
        dataS += str(self.gps_altitude)
        dataS += ","
        dataS += str(self.gps_latitude)
        dataS += ","
        dataS += str(self.gps_longitude)
        dataS += ","
        dataS += str(self.gps_sats)
        dataS += ","
        dataS += str(self.tilt_x)
        dataS += ","
        dataS += str(self.tilt_y)
        dataS += ","
        dataS += str(self.cmd_echo)
        dataS += ","
        dataS += str(self.accelX)
        dataS += ","
        dataS += str(self.accelY)
        dataS += ","
        dataS += str(self.accelZ)

        return dataS



        # this my function parameter : Data = 1007,12:34:56.23,21,S,HS_RELEASE,108.20,P,C,M,32.10,2.50,15:06:33,105.50,170.69,42.57,3,5.32,15.21,ST,10231
        # give function that takes this data and parse by comma and set according to proporties
        # return object of class TelemetryData

    def parseData(self, data):
        
        # split data by comma
        data = data.split(',')

        return data
    
    # get comma seperated data and set class proporties

    def setDatabyCommaSepratedDataList(self, data):
        # split data by comma

        self.set_team_id(data[0])
        self.set_mission_time(data[1])
        self.set_packet_count(data[2])
        # self.set_mode(data[3])
        self.set_mode("F")
        # self.set_state(data[4])
        self.set_state("LAUNCH_WAIT")
        tempYukseklik = float(data[5])
        tempYukseklik = tempYukseklik - 221
        tempYukseklik = round(tempYukseklik, 2)
        self.set_altitude(str(tempYukseklik))

        
        # self.set_altitude(data[5])
        # self.set_hs_deployed(data[6])
        self.set_hs_deployed("N")
        # self.set_pc_deployed(data[7])
        self.set_pc_deployed("N")
        # self.set_mast_raised(data[8])
        self.set_mast_raised("N")
        self.set_temp(data[9])
        self.set_pressure(data[10])
        self.set_volt(data[11])
        self.set_gps_time(data[12])
        self.set_gps_altitude(data[13])
       


        self.set_gps_latitude(data[14])
        self.set_gps_longitude(data[15])
        self.set_gps_sats(data[16])
        self.set_tilt_x(data[17])
        self.set_tilt_y(data[18])
        self.set_cmd_echo(data[19])
        self.set_accelX(data[20])
        self.set_accelY(data[21])
        self.set_accelZ(data[22])
        