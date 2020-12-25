

class Well:
    def __init__(self, wellId):

        self.wellId = wellId
        self.firstPipe = None
        self.secondPipe = None



well1 = Well(1)
well2 = Well(2)
well3 = Well(3)
well4 = Well(4)

well1.firstPipe = well2
well1.secondPipe = well3

well2.firstPipe = well3
well2.secondPipe = well4

well3.secondPipe = well4
