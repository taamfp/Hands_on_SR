import pandas as pd
from benchmark import load, gen_dataset

skipped_problems = ["tully"]

def generate_data(problems):

    for name, problem in problems.items():
        key = problem["key"]
        if key == "rydberg":
            if "data_generator" not in problem and "data" not in problem:
                continue
            if key in skipped_problems:
                continue
            X, y = gen_dataset(data, key)

            dataframe = pd.concat([X, pd.DataFrame(y, columns=["target"])], axis=1)
            print(dataframe)
            dataframe.to_csv(f'dataset_{key}.csv')


if __name__ == "__main__":
    data = load()
    problems = data["problems"]
    generate_data(problems)