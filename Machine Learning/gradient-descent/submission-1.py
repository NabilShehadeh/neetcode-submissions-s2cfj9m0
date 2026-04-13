class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        mini = init
        # Derivative:         f'(x) = 2x
        for _ in range(iterations):
            derivative = 2 * mini
            mini = mini - learning_rate * derivative
        return round(mini, 5)
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        pass
