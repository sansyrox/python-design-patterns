class Socket:
    _pinType = "Round"
     
class Adapter:
    _socket = None
    _pinType = "SquareToRound"
     
    def __init__(self, socket):
        self._socket = socket
 
class ElectricKettle:
    _adapter = None
    _pinType = "Square"
 
    def __init__(self, adapter):
        self._adapter = adapter
    def makeTea(self):
        if self._adapter._pinType == (self._pinType + "To" + self._adapter._socket._pinType):
            print("Boiling water....")
            print("Adding ingredients...")
            print("Tea brewing...")
            print("Tea is ready!")
        else:
            print("No power. Can't function.")
 
roundPinSocket  = Socket()
squareToRoundAdapter = Adapter(roundPinSocket)
kettle  = ElectricKettle(squareToRoundAdapter)
kettle.makeTea()
