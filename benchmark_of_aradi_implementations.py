import numpy as np
from claasp.ciphers.block_ciphers.aradi_block_cipher_sbox import AradiBlockCipherSBox
from claasp.ciphers.block_ciphers.aradi_block_cipher import AradiBlockCipher
from timeit import default_timer as timer
import pickle

aradisb = AradiBlockCipherSBox()
aradi = AradiBlockCipher()

for run in range(10):
    times = []
    for pow in range(4, 8):
        X = np.random.randint(256, size=(16, 10 ** pow), dtype=np.uint8)
        K = np.random.randint(256, size=(32, 10 ** pow), dtype=np.uint8)
        t0 = timer()
        C0 = aradi.evaluate_vectorized([X, K])
        t1 = timer() - t0

        t0 = timer()
        C1 = aradisb.evaluate_vectorized([X, K])
        t2 = timer() - t0

        times.append((pow, t1, t2))
        print(times[-1])
    with open(f'bench_aradi_{run}', 'wb') as fp:
        pickle.dump(times, fp)