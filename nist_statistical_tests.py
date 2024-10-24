from claasp.cipher_modules.statistical_tests.nist_statistical_tests import NISTStatisticalTests
from claasp.cipher_modules.report import Report
from claasp.ciphers.block_ciphers.aradi_block_cipher import AradiBlockCipher

cipher = AradiBlockCipher()
test = NISTStatisticalTests(aradi)
index = [0,1]
dataset = ["avalanche", "low_density", "high_density"]
for d in dataset:
    for i in index:
        test_results = test.nist_statistical_tests(d, input_index=i)
        report = Report(test_results)
        report.show()
