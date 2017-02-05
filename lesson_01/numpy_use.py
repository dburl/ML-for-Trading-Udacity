import numpy as np
import time


def test_run():
    #    print(np.array([(2,3,4),(5,6,7)]))
    #    print(np.zeros((4, 6), dtype=np.int_))
    #   print(np.random.normal(50,10,size=(2,3)))
    a = (np.random.randint(0,10,size=(2,3)))
    print(np.random.randint(0, 10, size=(6)))
    print(a.size)
    print(a.shape)
    print(a.sum())
    print(a.max(axis=1))

def time_check():
    t1= time.time()
    print("Time check")
    t2= time.time()
    print("Time spent:", t2-t1)
    # More complex operation
    nd1 = np.random.random((1000,1000))
    print(nd1.mean())
    t3=time.time()
    print("Time spent:", t3 - t2)