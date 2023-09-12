import argparse

from camila.runner import Runner
from camila.settings import Settings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, nargs="+")
    parser.add_argument("--load-data", type=str, nargs="*", default=[])
    parser.add_argument("--settings", type=str)

    args = parser.parse_args()

    runner = Runner(Settings.from_json(args.settings))

    for data_path in args.load_data:
        runner.load(data_path)

    print(runner.run_query(" ".join(args.query)))
