import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # first we're going to stabilize numerically
        # to avoid overflows with larger numbers 
        shifted = z - np.max(z)
        #exponents
        exps = np.exp(shifted)
        # normalization and the return of the value between 0 and 1
        return np.round(exps / np.sum(exps), 4)





        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        pass
