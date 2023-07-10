from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self):
        pass


class HDMICable(Cable):

    def connect(self, device1, device2):
        return f"Connect {device1} to {device2}"


class RCACable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2}"


class EthernetCable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2}"


class PowerCable(Cable):
    def connect(self, device):
        return f"Device Connected to Power Outlet"

class DVDPlayer():
    pass


class GameConsole():
    pass

class Router():
    pass


class Television():
    pass


hdmi = HDMICable()
tv = Television()
gc = GameConsole()

print(hdmi.connect(tv, gc))



