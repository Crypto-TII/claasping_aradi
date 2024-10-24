from claasp.ciphers.block_ciphers.aradi_block_cipher_sbox import AradiBlockCipherSBox
from claasp.cipher_modules.models.sat.sat_models.sat_xor_linear_model import SatXorLinearModel

cipher = AradiBlockCipherSBox(number_of_rounds=4)
model = SatXorLinearModel(cipher)
trail = model.find_lowest_weight_xor_linear_trail()
