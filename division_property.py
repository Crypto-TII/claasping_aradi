from claasp.ciphers.block_ciphers.aradi_block_cipher import AradiBlockCipher

cipher = AradiBlockCipher(number_of_rounds=2)
from claasp.cipher_modules.division_trail_search import *

model = MilpDivisionTrailModel(cipher)
model.find_degree_of_specific_anf(0)  # to get the degree of 0th bit after 2 rounds
