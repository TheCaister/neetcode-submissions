# so imagine a line, with a bunch of cars, and their speeds
# max car fleet is n, min car fleet is 1 where they all combine
# brute force would be something like simulate the whole thing one instant at a time.
#   in each time unit, we calculate the next position of each car. one thing to notice here is that we can
#   collapse a car into a fleet as soon as it encounters another car. Aka posA + speedA > posB
#   instantly, this won't be a very efficient algorithm
# would it help to sort the list, perhaps by position? that way, we can potentially scan from left to right when doing position calculations
# we could.... constantly update the position and speed lists. collapse if there are any overlaps. If at any point we cross target, we
# add 1 to our fleet count. repeat until the list is empty
# having speed of 0 is interesting. that means that car will not move at all, so itself and all cars before it will never reach the target

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
# prep and sort tuples of positions and speeds, to make them easier to collapse
# prep stack to hold the next slowest vehicle to bump into
        posSpeed = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(posSpeed)[::-1]:
            timeToTarget = (target - p) / s

            if stack and timeToTarget <= stack[-1]:
                continue
            else:
                stack.append(timeToTarget)
        
        return len(stack)


        