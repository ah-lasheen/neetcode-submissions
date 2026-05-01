class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack, cars = [], []
        
        for car in range(len(position)):
            time = (target - position[car]) / speed[car]
            cars.append([position[car], speed[car], time])

        cars.sort(key=lambda x: x[0], reverse=True)
        # sorted cars is now a list[list[position, speed, time till target]]
        # sorted by position descending
        stack.append(cars[0])

        for i in range(1, len(cars)):
            # if the current car takes >= time to get to the finish than 
            # the previous, we can ignore this one since it will catch up
            # otherwise, we can push the current car onto the stack
            # as it will be a new fleet
            if cars[i][2] > stack[-1][2]:
                stack.append(cars[i])
        
        return len(stack)