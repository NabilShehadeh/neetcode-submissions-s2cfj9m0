import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # we stabilize first
        shifted = z - np.max(z)
        # we put together an exponential calculation here where the values are between 0 and 1
        exps = np.exp(shifted)

        #normalization and return the value
        return np.round(exps / np.sum(exps), 4)
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        pass
