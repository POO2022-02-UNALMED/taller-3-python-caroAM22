class TV:
    numTV=0

    def __init__(self,marca,estado):
        self.__marca=marca
        self.__estado=estado
        self.__canal=1
        self.__volumen=1
        self.__precio=500
        self.numTV+=1
        self.__control=None

    def getMarca(self):
        return self.__marca
        
    def setMarca(self,marca):
        self.__marca=marca

    def getControl(self):
        return self.__control
        
    def setControl(self,control):
        self.__control=control

    def getPrecio(self):
        return self.__precio
        
    def setPrecio(self,precio):
        self.__precio=precio

    def getCanal(self):
        return self.__canal
        
    def setCanal(self,canal):
        if (canal<=120 and canal>=1) and self.__estado==True:
            self.__canal=canal
    
    def getVolumen(self):
        return self.__volumen
        
    def setVolumen(self,volumen):
        if (volumen<=7 and volumen>=0) and self.__estado==True:
            self.__volumen=volumen
    
    def getNumTV(cls):
        return cls.__numTV
        
    def setNumTV(cls,numeroTV):
        cls.__numTV=numeroTV

    def getEstado(self):
        return self.__estado

    def turnOn(self):
        self.__estado=True

    def turnOff(self):
        self.__estado=False

    def canalUp(self):
        if self.__canal<120 and self.__estado==True:
            self.__canal=self.__canal+1

    def canalDown(self):
        if self.__canal>1 and self.__estado==True:
            self.__canal=self.__canal-1
    
    def volumenUp(self):
       if self.__volumen<7 and self.__estado==True:
            self.__volumen+=1

    def volumenDown(self):
       if self.__canal>1 and self.__estado==True:
            self.__volumen-=1
