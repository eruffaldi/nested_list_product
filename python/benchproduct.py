#http://stackoverflow.com/questions/4709510/itertools-product-speed-up
import numpy as np
import time
import itertools

def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = n / arrays[0].size
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m,1:])
        for j in xrange(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out

def test_numpy(arrays):
    for res in cartesian(arrays):
        pass


def test_itertools(arrays):
    return np.array(list(itertools.product(*arrays)),dtype=np.int32).transpose()


def main():
    arrays = [np.fromiter(range(100), dtype=int), np.fromiter(range(100, 200), dtype=int)]
    start = time.clock()
    for _ in range(100):
        test_numpy(arrays)
    print(time.clock() - start)
    start = time.clock()
    for _ in range(100):
        test_itertools(arrays)
    print(time.clock() - start)

if __name__ == '__main__':
    main()