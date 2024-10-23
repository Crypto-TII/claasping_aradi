"""
Script to run the neural distinguisher AutoND pipeline. The exact execution time will depend
on the number of rounds the neural distinguisher covers, and the number of found
$\epsilon$-close differences.
"""
from claasp.ciphers.block_ciphers.aradi_block_cipher import AradiBlockCipher
from claasp.cipher_modules.neural_network_tests import NeuralNetworkTests

cipher = AradiBlockCipher()
test = NeuralNetworkTests(aradi)
report = test.run_autond_pipeline()
