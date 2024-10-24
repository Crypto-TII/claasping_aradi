from claasp.cipher_modules.avalanche_tests import AvalancheTests
from claasp.cipher_modules.report import Report
from claasp.ciphers.block_ciphers.aradi_block_cipher import AradiBlockCipher

cipher = AradiBlockCipher()
test = AvalancheTests(cipher).avalanche_tests(number_of_samples=1000)
report = Report(test)
report.show(test_name="avalanche_entropy_vectors")
