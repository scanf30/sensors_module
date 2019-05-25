
class GpsLibrary:
        
    def __init__(self):
        #PARAMETERS FOR GPS
        self.NORM_LAT = 2036.8
        self.NORM_LON = 10024.2
        self.D_LAT = 10.1
        self.D_LON = 10.1

        self.lat = 0
        self.lon = 0
        self.speed = 0
        self.angle = 0
        self.quality = 0
        self.satellites = 0
        self.errorGgpga = 0
        self.errorGprmc = 0 

    def parseGPGGA(self,data):
        #ggpga, timegpsGPGGA, latGGPGGA, latdirGPGGA, lonGPGGA, londirGPGGA,qualityGPGGA, numberSatellitesGPGGA, hdopGPGGA, heightGPGGA, heightUnitsGPGGA, ageCorrectionGPGGA,correctionStationGPGGA,checksumGPRMC, otherGPRMC = data.split(',')	
        ggpga = data.split(',')
        #print(ggpga)
        try:
            #lat = float(ggpga[2])
            #lon = float(ggpga[4])
            qty = int(ggpga[6])
            sat = int(ggpga[7])
  
            self.quality = qty
            self.satellites = sat
            self.errorGgpga = 0                
        except:
            self.errorGgpga = 1

    def parseGPRMC(self,data):
        #gpmrc, timegpsGPRMC, warningGPRMC, latGPRMC, latdirGPRMC, lonGPRMC, londirGPRMC, speedknotsGPRMC, truecurseGPRMC, dateGPRMC, angleGPRMC, checksumGPRMC, otherGPRMC = data.split(',')	
        gpmrc = data.split(',')	
        #print(data)
        #print(gpmrc)
        try:
            lat = float(gpmrc[3])
            lon = float(gpmrc[5])
            speed = float(gpmrc[7])
            angle = float(gpmrc[8])            

            #Checks if latitude and longitude are in range
            if lat > self.NORM_LAT-self.D_LAT and lat < self.NORM_LAT+self.D_LAT and lon > self.NORM_LON-self.D_LON and lon < self.NORM_LON+self.D_LON:  
                self.lat = lat
                self.lon = lon
                self.speed = speed
                self.angle = angle  
                self.errorGprmc = 0
            else:
                self.errorGprmc = 1
        except:
            self.errorGprmc = 1


