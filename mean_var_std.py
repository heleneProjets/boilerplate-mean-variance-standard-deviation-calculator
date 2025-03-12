import numpy as np


def calculate(list):
    if (len(list) < 9): 
        raise ValueError("List must contain nine numbers.")

    # list into np.array
    array = np.array(list)
    matrix = np.array(list).reshape(3,3)

    # Dico creation 
    calculations = {
        'mean': [
            np.mean(matrix, axis=0, dtype=float).tolist(), 
            np.mean(matrix, axis=1, dtype=float).tolist(), 
            np.mean(array, dtype=float)
        ],
        'variance': [
            np.var(matrix, axis=0, dtype=float).tolist(), 
            np.var(matrix, axis=1, dtype=float).tolist(), 
            np.var(array)
        ],
        'standard deviation': [
            np.std(matrix, axis=0, dtype=float).tolist(), 
            np.std(matrix, axis=1, dtype=float).tolist(), 
            np.std(array).tolist()
        ],
        'max': [
            np.max(matrix, axis=0).tolist(), 
            np.max(matrix, axis=1).tolist(), 
            np.max(array)
        ],
        'min': [
            np.min(matrix, axis=0).tolist(), 
            np.min(matrix, axis=1).tolist(), 
            np.min(array)
        ],
        'sum': [
            np.sum(matrix, axis=0).tolist(), 
            np.sum(matrix, axis=1).tolist(), 
            np.sum(array)
        ]
    }

    return calculations