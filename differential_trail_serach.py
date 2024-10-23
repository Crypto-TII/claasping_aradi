from claasp.ciphers.block_ciphers.aradi_block_cipher_sbox import AradiBlockCipherSBox
from claasp.cipher_modules.models.sat.sat_models.sat_xor_differential_model import SatXorDifferentialModel
cipher = AradiBlockCipherSBox(number_of_rounds=4)
model = SatXorDifferentialModel(cipher)
trail = model.find_lowest_weight_xor_differential_trail()