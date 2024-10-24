from claasp.ciphers.block_ciphers.aradi_block_cipher_sbox import AradiBlockCipherSBox
from claasp.cipher_modules.algebraic_tests import AlgebraicTests

aradi = AradiBlockCipherSBox(number_of_rounds=2)
test = AlgebraicTests(aradi)
result=test.algebraic_tests(timeout_in_seconds=10)
