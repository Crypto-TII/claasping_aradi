from claasp.ciphers.block_ciphers.aradi_block_cipher_sbox import AradiBlockCipherSBox

cipher = AradiBlockCipherSBox(number_of_rounds=4)
id_list = cipher.impossible_differential_search("cp", solver='Chuffed')
