"""
Constraints and assumptions

1 What types of vehicles should we support?
Motorcycle, Car, Bus

2 Does each vehicle type take up a different amount of parking spots?
Yes
Motorcycle spot -> Motorcycle
Compact spot -> Motorcycle, Car
Large spot -> Motorcycle, Car

3 Bus can park if we have 5 consecutive "large" spots
Does the parking lot have multiple levels?
Yes

"""


class ParkingLot(object):

    def __init__(self, num_levels):
        self.num_levels = num_levels
        self.levels = []

    def park_vehicle(self, vehicle):
        for level in levels:
            if level.park_vehicle(vehicle):
                return True
        return False


class Level(object):

    SPOTS_PER_ROW = 10

    def __init__(self, floor, total_spots):
        self.floor = floor
        self.num_spots = total_spots
        self.available_spots = 0
        self.parking_spots = []

    def spot_freed(self):
        self.available_spots += 1

    def park_vehicle(self, vehicle):
        spot = self._find_available_spot(vehicle)
        if spot is None:
            return None
        else:
            spot.park_vehicle(vehicle)
            return spot

    def _find_available_spot(self, vehicle):
        """Find an available spot where vehicle can fit, or return None"""
        # ...

    def _park_starting_at_spot(self, spot, vehicle):
        """Occupy starting at spot.spot_number to vehicle.spot_size."""
        # ...


class ParkingSpot(object):

    def __init__(self, level, row, spot_number, spot_size, vehicle_size):
        self.level = level
        self.row = row
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle_size = vehicle_size
        self.vehicle = None

    def is_available(self):
        return True if self.vehicle is None else False

    def can_fit_vehicle(self, vehicle):
        if self.vehicle is not None:
            return False
        return vehicle.can_fit_in_spot(self)

    def park_vehicle(self, vehicle):  # ...
    def remove_vehicle(self):  # ...