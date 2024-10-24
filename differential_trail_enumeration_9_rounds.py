from claasp.cipher_modules.models.utils import set_fixed_variables, integer_to_bit_list
from claasp.ciphers.block_ciphers.aradi_block_cipher_sbox import AradiBlockCipherSBox

cipher = AradiBlockCipherSBox(number_of_rounds=9)
from claasp.cipher_modules.models.sat.sat_models.sat_xor_differential_model import SatXorDifferentialModel
key = set_fixed_variables(component_id='key', constraint_type='equal', bit_positions=range(256), bit_values= [0]*256)
pt = set_fixed_variables(component_id='plaintext', constraint_type='equal', bit_positions= range(128), bit_values=integer_to_bit_list(0x00000000400010020000000000000000, 128, 'big'))
ct = set_fixed_variables(component_id='intermediate_output_7_61', constraint_type='equal', bit_positions= range(128), bit_values=integer_to_bit_list(0x10800080000000000000000000000000, 128, 'big'))
sat = SatXorDifferentialModel(cipher)
trail = sat.find_all_xor_differential_trails_with_weight_at_most(137, 137, fixed_values=[pt, ct,  key])
