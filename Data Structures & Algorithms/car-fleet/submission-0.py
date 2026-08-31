class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for index, s in enumerate(speed):
            position[index] = (position[index], s)

        position.sort()

        if len(position) == 1:
            return 1

        time_taken_by_slowest_car = -1
        car_fleet = 0

        for p, s in position[::-1]:
            if (target - p) / s > time_taken_by_slowest_car:
                time_taken_by_slowest_car = (target - p) / s
                car_fleet += 1

        return car_fleet