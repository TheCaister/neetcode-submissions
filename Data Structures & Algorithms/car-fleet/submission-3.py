# let's calculate the amount of time it would take all cars to get to the target?
# i think we'd like to process these cars in a sorted order
# if we plot out the trajectory for these cars, if they intersect, the car with the 
# steeper slope will be collapsed into the other one
# so I guess is there a quick way to tell if there's gonna be a collision?
# well the best way would be the time it takes to get to the target. say we have x and y. if y < x, then y needs to be collapsed into x
# and on instinct so far, I think it's best to sort/process starting with largest position first, so that for subsequent cars, we can do the collapsing processing
# if we start the other way around, it could be a bit tougher to figure out if the current car will be collapsed into a car in front
# with the sorting coming into place, it will be n log n, and we'll need n space to hold this stack for processing. at the end we just return the length of the stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        cur_largest_time = 0

        cars_sorted = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars_sorted.append((position[i], time))
        
        cars_sorted = sorted(cars_sorted)[::-1]
        
        for pos, time in cars_sorted:
            # if not stack or (stack and stack[-1] < time):
                # stack.append(time)
            if time > cur_largest_time:
                cur_largest_time = time
                fleet += 1


        return fleet