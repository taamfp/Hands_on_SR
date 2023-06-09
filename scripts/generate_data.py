import argparse
import pandas as pd
from benchmark import load, gen_dataset

skipped_problems = ["tully"]

def generate_data(problems):

    parser = argparse.ArgumentParser(description="Choose equation to generate dataset")

    parser.add_argument('--key_equation', required=True)

    args = parser.parse_args()

    for name, problem in problems.items():
        key = problem["key"]
        if key == str(args.key_equation):
            if "data_generator" not in problem and "data" not in problem:
                continue
            if key in skipped_problems:
                continue
            X, y = gen_dataset(data, key)

            print(X, y)

            dataframe = pd.concat([X, pd.DataFrame(y, columns=["target"])], axis=1)
            print(dataframe)
            dataframe.to_csv(f'dataset_{key}.csv')


if __name__ == "__main__":
    data = load()
    problems = data["problems"]
    generate_data(problems)