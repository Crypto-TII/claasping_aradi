import numpy as np
from claasp.ciphers.block_ciphers.aradi_block_cipher_sbox import AradiBlockCipherSBox
from claasp.cipher_modules.models.utils import set_fixed_variables, integer_to_bit_list
cipher = AradiBlockCipherSBox(number_of_rounds=7)
model = cipher.get_model('cp', 'xor_differential')
search_function = model.find_one_xor_differential_trail
last_component_id = cipher.get_all_components()[-1].id
id_list = []
inputs_dictionary = cipher.inputs_size_to_dict()
plain_bits = inputs_dictionary['plaintext']
key_bits = inputs_dictionary['key']
for input_word_position in range(32):
    zero_bits_in_input = [i for i in range(128) if (i%32) != input_word_position]
    non_zero_bits_in_input = [32*i + input_word_position for i in range(4)]
    for output_word_position in range(32):
        zero_bits_in_output = [i for i in range(128) if (i%32) != output_word_position]
        non_zero_bits_in_output = [32*i + output_word_position for i in range(4)]
        fixed_values = []
        fixed_values.append(set_fixed_variables('key', 'equal', list(range(key_bits)),
                                integer_to_bit_list(0, key_bits, 'big')))
        fixed_values.append(set_fixed_variables('plaintext', 'equal', zero_bits_in_input,
                                integer_to_bit_list(0, plain_bits-4,'big')))
        fixed_values.append(set_fixed_variables(last_component_id, 'equal', zero_bits_in_output,
                                integer_to_bit_list(0, plain_bits-4,'big')))
        fixed_values.append(set_fixed_variables('plaintext', 'not_equal', non_zero_bits_in_input,
                                integer_to_bit_list(0, plain_bits-4,'big')))
        fixed_values.append(set_fixed_variables(last_component_id, 'not_equal', non_zero_bits_in_output,
                                integer_to_bit_list(0, plain_bits-4,'big')))
        solution = search_function(fixed_values, solver_name='Chuffed')
        if solution['status'] == "UNSATISFIABLE":
            id_list.append((input_word_position, output_word_position))
