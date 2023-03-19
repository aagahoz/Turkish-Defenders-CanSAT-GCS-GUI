class TelemetryData:
    def __init__(self):
        self.team_id = None
        self.mission_time = None
        self.packet_count = None
        self.altitude = None
        self.pressure = None
        self.temp = None
        self.volt = None
        self.gps_time = None
        self.gps_latitude = None
        self.gps_longitude = None
        self.gps_altitude = None
        self.gps_sats = None
        self.air_speed = None
        self.particle_count = None
        self.pitch = None
        self.roll = None
        self.yaw = None
    
    def set_team_id(self, team_id):
        self.team_id = team_id
        
    def set_mission_time(self, mission_time):
        self.mission_time = mission_time
        
    def set_packet_count(self, packet_count):
        self.packet_count = packet_count
        
    def set_altitude(self, altitude):
        self.altitude = altitude
        
    def set_pressure(self, pressure):
        self.pressure = pressure
        
    def set_temp(self, temp):
        self.temp = temp
        
    def set_volt(self, volt):
        self.volt = volt
        
    def set_gps_time(self, gps_time):
        self.gps_time = gps_time
        
    def set_gps_latitude(self, gps_latitude):
        self.gps_latitude = gps_latitude
        
    def set_gps_longitude(self, gps_longitude):
        self.gps_longitude = gps_longitude
        
    def set_gps_altitude(self, gps_altitude):
        self.gps_altitude = gps_altitude
        
    def set_gps_sats(self, gps_sats):
        self.gps_sats = gps_sats
        
    def set_air_speed(self, air_speed):
        self.air_speed = air_speed
        
    def set_particle_count(self, particle_count):
        self.particle_count = particle_count
        
    def set_pitch(self, pitch):
        self.pitch = pitch
        
    def set_roll(self, roll):
        self.roll = roll
        
    def set_yaw(self, yaw):
        self.yaw = yaw

    def __str__(self):
        return f"Team ID: {self.team_id}\nMission Time: {self.mission_time}\nPacket Count: {self.packet_count}\nAltitude: {self.altitude}\nPressure: {self.pressure}\nTemp: {self.temp}\nVolt: {self.volt}\nGPS Time: {self.gps_time}\nGPS Latitude: {self.gps_latitude}\nGPS Longitude: {self.gps_longitude}\nGPS Altitude: {self.gps_altitude}\nGPS SATs: {self.gps_sats}\nAir Speed: {self.air_speed}\nParticle Count: {self.particle_count}\nPitch: {self.pitch}\nRoll: {self.roll}\nYaw: {self.yaw}"

    def set_all_values_to_zero(self):
        self.team_id = 0
        self.mission_time = 0
        self.packet_count = 0
        self.altitude = 0
        self.pressure = 0
        self.temp = 0
        self.volt = 0
        self.gps_time = 0
        self.gps_latitude = 0
        self.gps_longitude = 0
        self.gps_altitude = 0
        self.gps_sats = 0
        self.air_speed = 0
        self.particle_count = 0
        self.pitch = 0
        self.roll = 0
        self.yaw = 0