 def update_plots_data(self):
        

        self.xAltitude = self.xAltitude[1:]  # Remove the first y element.
        self.xAltitude.append(self.xAltitude[-1] + 1)

        self.yAltitude = self.yAltitude[1:]  # Remove the first

        self.yAltitude.append(self.instanceAltitude)  # Add a new random value.
        self.instanceAltitude = 1

        self.data_line_altitude.setData(self.xAltitude, self.yAltitude)

        self.xTemprature = self.xTemprature[1:]  # Remove the first y element.
        self.xTemprature.append(self.xTemprature[-1] + 1)

        self.yTemprature = self.yTemprature[1:]  # Remove the first
        self.yTemprature.append(self.instanceTemprature)
        self.instanceTemprature = 0

        self.data_line_temprature.setData(self.xTemprature, self.yTemprature)

        self.xPressure = self.xPressure[1:]  # Remove the first y element.
        self.xPressure.append(self.xPressure[-1] + 1)

        self.yPressure = self.yPressure[1:]  # Remove the first
        self.yPressure.append(self.instancePressure)  # Add a new random value.
        self.instancePressure = 0

        # Update the data.
        self.data_line_pressure.setData(self.xPressure, self.yPressure)

        self.xAirSpeed = self.xAirSpeed[1:]  # Remove the first y element.
        self.xAirSpeed.append(self.xAirSpeed[-1] + 1)

        self.yAirSpeed = self.yAirSpeed[1:]  # Remove the first
        self.yAirSpeed.append(self.instanceAirSpeed)  # Add a new random value.
        self.instanceAirSpeed = 0

        self.data_line_airspeed.setData(self.xAirSpeed, self.yAirSpeed)

        self.xVoltage = self.xVoltage[1:]  # Remove the first y element.
        self.xVoltage.append(self.xVoltage[-1] + 1)

        self.yVoltage = self.yVoltage[1:]  # Remove the first
        self.yVoltage.append(self.instanceVoltage)  # Add a new random value.
        self.instanceVoltage = 0

        self.data_line_voltage.setData(self.xVoltage, self.yVoltage)

        self.xParticleCount = self.xParticleCount[1:]
        self.xParticleCount.append(self.xParticleCount[-1] + 1)

        self.yParticleCount = self.yParticleCount[1:]  # Remove the first
        self.yParticleCount.append(self.instanceParticleCount)
        self.instanceParticleCount = 0

        # Update the data.
        self.data_line_particlecount.setData(
        self.xParticleCount, self.yParticleCount)
        