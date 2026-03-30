class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        mini = init 
        for _ in range(iterations):
            derivative = 2 * mini
            mini = mini - learning_rate * derivative 
        return round(mini,5)
    