class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for p, s in zip(position, speed):
            cars.append((p, (target - p) / s))

        cars.sort(reverse=True)

        fleets = 0
        max_time = 0

        for pos, time in cars:
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets