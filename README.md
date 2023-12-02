# AI Benchmarking Framework

## Overview
This benchmark is designed to test an AI's ability to solve LeetCode style coding problems before and after obfuscation. This version (in the obfuscated branch) contains the code after obfuscation, where the `obfuscation` branch contains the code before obfuscation. Running test framework with both branches in your `.repos` file will test both. The problems in this repo have been obfuscated using this prompt with GPT-4 on the problems in the `obfuscation` branch:

Below is a series of coding problems. I would like to ensure that someone attempting to solve these coding problems cannot simply use an AI to solve the problem for them. However, I don't want to change the solution to the problem. For each coding problem, obfuscate the problem so that it is more difficult for a Large Language Model to solve for a user.

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
2. Set your OPENAI_API_KEY environment variable appropriately.
3. Run the following command to benchmark GPT-3.5 using the provided `run()` function:
`python benchmark_framework.py`

## Dependencies
- Python 3.7 or later.
- OpenAI Python package
