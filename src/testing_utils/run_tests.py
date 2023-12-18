import json
import os

def query(prompt):
    return "TILLS ATT NIELS FIXAR " + prompt

def run_tests(test_file: str, output_name: str, tests_to_run: list = []):
    """
    Automatically tests the LLM using json files as inputs and outputs
    
    =============================
    ARGS:
    test_file (str) : the name of the test file that you want to run (test.json)

    output_name (str) : the name of the output file, .json is not needed here

    tests_to_run (lists of numbers) : A list of indexes of the tests that you want to run if you only want to run some of 
    the tests. Leave empty to run all tests
    =============================
    
    """

    output_file_path = f'test_results/{output_name}.json'
    test_file_path = f'test_inputs/{test_file}'

    output_directory = os.path.dirname(output_file_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(test_file_path, 'r', encoding="utf-8") as input_file:
        test_data = json.load(input_file)

    results = []

    for test in test_data:
        test_index = test["test_index"]
        if not tests_to_run or test_index in tests_to_run:
            test_name = test["test_name"]
            description = test["description"]
            prompt = test["prompt"]
            
            response = query(prompt)
            
            result = {
                "test_name": test_name,
                "description": description,
                "prompt": prompt,
                "response": response
            }
            results.append(result)

    with open(output_file_path, 'w') as output_file:
        json.dump(results, output_file, indent=4)

    print(f"Results saved to {output_file_path}")


