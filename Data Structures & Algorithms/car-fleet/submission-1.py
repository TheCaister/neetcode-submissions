# brute force... i don't even know
# let's say each car takes a certain amount of time to cross the finish line
# seems like most cars will be bound by the slowest one?
# if you have car A, with a million cars behind it, it doesn't matter if car A
# takes the most amount of unit time, non of the previous cars will surpass it
# for each car, take a look at all the cars behind it. if the speed is the same or lower,
# they'll never touch and will be separate fleets. If speed is higher, that previous
# car will be consolidated into the current car
# but, there's a chance that a previous subsection would consolidate further
# before the current car. Aka, on instinctual level it'd make sense to collapse
# cars from start to target, rather than from end to start because we might consolidate
# too quickly
# and, just checking speed wouldn't always work, you could have a super slow
# car at the end that takes only 1 unit time to cross, so a much faster car
# further back could still be a separate fleet. it'd make more sense to 
# use time to target instead

# i think it makes sense to sort by position, and make sure to have the right speeds as well
# let's build up a list, and consolidate as we go
# [1, 3], [4, 2]
# at each step, let's check if it can be consolidated w/ the previous one
# time to destination = (target - pos) / speed
# if prev_time <= cur_time, then consolidate, using the latest car, the previous
# car is not in consideration anymore 
# keep popping as necessary
# at the end, just return the length of the list

# o (n log n) to sort, o (n) space to hold sorted values and stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        sorted_cars = sorted(zip(position, speed))
        

        for cur_pos, cur_speed in sorted_cars:
            cur_time_to_goal = (target - cur_pos) / cur_speed

            while stack and ((target - stack[-1][0]) / stack[-1][1]) <= cur_time_to_goal:
                stack.pop()
            
            stack.append([cur_pos, cur_speed])

        return len(stack)
        