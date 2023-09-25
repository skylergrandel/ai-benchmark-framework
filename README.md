# AI Benchmarking Framework

## Overview
This framework is designed to benchmark generative AI models on a variety of tasks. It facilitates easy integration of new benchmarks and subject AIs for a standardized evaluation.

## Structure
The repository is structured as follows:
- `benchmarks/`: A directory containing modular benchmark JSON files.
- `test_suites/`: A directory containing the test suites for each benchmark, with the tests for each problem housed in individual Python files.
- `benchmark_framework.py`: The script for running the benchmarks.
- `run_func.py`: Contains the `run()` function for GPT-3.5 to test it on our benchmarks.

## How It Works
1. **Benchmark Definition**:
   - Benchmarks are defined in JSON files placed in the `benchmarks` directory. Each benchmark file contains a collection of problems, with each problem defining a prompt for the AI model and a corresponding test suite for evaluating the generated solution.
   - The test suites are Python files placed in the `test_suites` directory, organized in subdirectories named after the corresponding benchmark.

2. **Subject AI Integration**:
   - The subject AI is integrated via a `run()` function that takes the problem prompt as input and returns the generated solution. For example, `run_func.py` contains the `run()` function for GPT-3.5.

3. **Benchmarking Process**:
   - The `benchmark_framework.py` script loads all benchmarks, queries the subject AI with each problem, evaluates the generated solutions using the provided test suites, and computes a score for each benchmark based on the evaluation results.

## How to Run The Script
1. Ensure you have all the necessary dependencies installed (see [Dependencies](#dependencies) section).
2. Replace the `api_key` in `run_func.py` with your actual OpenAI API key.
3. Run the following command to benchmark GPT-3.5 using the provided `run()` function:
`python benchmark_framework.py run_func.py`

## Adding Your Own Benchmarks

1. **Create Benchmark JSON**:
   - Create a new JSON file following the existing format in the `benchmarks` directory.
   - Each benchmark file should contain a benchmark name and a list of problems, with each problem defining a prompt for the AI model and a corresponding test suite for evaluating the generated solution.
   - See the example benchmark JSON for the expected format.

2. **Create Test Suites**:
   - For each problem in your benchmark, create a Python file containing the test suite.
   - Place your test suite files in a new subdirectory under the `test_suites` directory. The name of the subdirectory should match the "name" field defined in your benchmark's JSON file.
   - Your test suites should calculate a quantitative result, returning the points earned and the points possible.
   - For more qualitative results, you could make a call to the GPT-4 API for inspection and you could output intermediate results separately if that is necessary for your benchmark.

## Testing a New AI with This Framework
1. **Create AI Runner File**:
   - Create a new Python file defining a run() function. This function should take the problem prompt as input and return the generated solution.
   - You can look at run_func.py as an example of how to structure this file for GPT-3.5.

2 **Run The Benchmarking Script**:
   - Execute the benchmark_framework.py script, passing the path to your AI runner file as a command-line argument.

## Dependencies
- Python 3.7 or later.
- OpenAI Python package
