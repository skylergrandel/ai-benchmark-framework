import json
import importlib
import glob
import sys
import os  # Import the os module to join paths

from llm_test_helpers import get_llm, get_args
args = get_args(sys.argv)
llm = get_llm(args.model)

def load_benchmarks(directory):
    benchmark_files = glob.glob(f"{directory}/*.json")
    benchmarks = [json.load(open(file)) for file in benchmark_files]
    return benchmarks

def run_benchmark(benchmark, ai_module):
    total_points_earned = 0
    total_points_available = 0
    
    for problem in benchmark['problems']:
        prompt = problem['prompt']
        solution = llm.predict(prompt)
        
        #print(solution)

        # Construct the path to the test suite module
        test_suite_path = ".".join(["test_suites", benchmark['name'], problem['test_suite'][:-3]])
        
        try:
            test_suite_module = importlib.import_module(test_suite_path)
            total_points = 1
            points_earned = test_suite_module.test(solution)
        except Exception as e:
            print("Exception while testing: ", e)
            points_earned, total_points = 0,0

        print(points_earned, "/", total_points)
        
        total_points_earned += points_earned
        total_points_available += total_points
    
    print(total_points_earned, "/", total_points_available)
    score = total_points_earned / total_points_available * 100
    return score

def main():
    #ai_module = importlib.import_module(ai_filename[:-3])
    ai_module = llm
    benchmarks = load_benchmarks('./benchmarks')
    
    for benchmark in benchmarks:
        score = run_benchmark(benchmark, ai_module)
        print(f"{benchmark['name']}: {score}%")

    output_data = {"output": score}
    
    with open('output.json', 'w') as f:
        json.dump(output_data, f, indent=4)


if __name__ == "__main__":
    main()
    #main(sys.argv[1])
