import json
from claasp.cipher_modules.continuous_diffusion_analysis import ContinuousDiffusionAnalysis
from claasp.ciphers.block_ciphers.aradi_block_cipher import AradiBlockCipher

number_of_rounds = 12
cipher = AradiBlockCipher(number_of_rounds=number_of_rounds)
cda = ContinuousDiffusionAnalysis(cipher)
lambda_values = [0.1, 0.01, 0.02, 0.001, 0.02]
results = []
for lambda_value in lambda_values:
    cda = ContinuousDiffusionAnalysis(cipher)
    test_args = {
        'is_continuous_neutrality_measure': False,
        'is_diffusion_factor': False,
        'continuous_avalanche_factor_number_of_samples': 4000,
        'threshold_for_avalanche_factor': lambda_value
    }
    result = cda.continuous_diffusion_tests(**test_args)
    result['input_parameters']['cipher'] = str(result['input_parameters']['cipher'])

    round_output_results = result['test_results']["plaintext"]["round_output"]
    plaintext_values = round_output_results["continuous_avalanche_factor"][0]["values"]
    round_number_caf_values = [
        {"round_number": idx + 1, "caf_value": val} for idx, val in enumerate(plaintext_values)
    ]

    result.update({
        "round_number_caf_values": round_number_caf_values,
        "number_samples": number_samples,
        "lambda_value": lambda_value,
        "cipher": "_".join(cipher.id.split("_")[:-1])
    })

    results.append(result)

with open("caf_results.txt", "a") as json_file:
    for res in results:
        json.dump(res, json_file)
        json_file.write("\n")