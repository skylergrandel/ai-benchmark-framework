import json
import importlib
import glob
import sys
import os

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
    results = []
    
    for problem in benchmark['problems']:
        prompt = problem['prompt']
        solution = llm.predict(prompt)
        test_suite_path = ".".join(["test_suites", benchmark['name'], problem['test_suite'][:-3]])
        
        try:
            test_suite_module = importlib.import_module(test_suite_path)
            points_earned, total_points = test_suite_module.test(solution)
        except Exception as e:
            print("Exception while testing:", e)
            points_earned, total_points = 0, 0  # assuming you award 0 for exceptions
        
        results.append({
            "points_earned": points_earned,
            "total_points": total_points
        })
        
        total_points_earned += points_earned
        total_points_available += total_points
    
    score = total_points_earned / total_points_available * 100 if total_points_available != 0 else 0
    return score, results

def main():
    ai_module = llm
    benchmarks = load_benchmarks('./benchmarks')
    
    output_data = []
    
    for benchmark in benchmarks:
        score, results = run_benchmark(benchmark, ai_module)
        output_data.append({
            "benchmark_name": benchmark['name'],
            "score": score,
            "results": results
        })
        print(f"{benchmark['name']}: {score}%")
        
    with open('output.json', 'w') as f:
        json.dump(output_data, f, indent=4)

if __name__ == "__main__":
    main()
