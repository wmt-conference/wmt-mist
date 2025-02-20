import argparse
import json

from mist.datasets.general_mt_dataset import GeneralMTDataset
from mist.evaluators.mt_evaluator import MTEvaluator


def main():
    parser = argparse.ArgumentParser(
        description="WMT MIST scoring"
    )

    subparsers = parser.add_subparsers(dest="command", help="Sub-command to run")

    # Sub-command: collect
    collect_parser = subparsers.add_parser("collect", help="Collect prompts for a given testset")
    collect_parser.add_argument("--testset", required=True, help="Name of the testset (e.g. wmt)")

    # Sub-command: score
    eval_parser = subparsers.add_parser("score", help="Score outputs for a given testset")
    eval_parser.add_argument("--testset", required=True, help="Name of the testset (e.g. wmt)")
    eval_parser.add_argument("--answers", required=True, help="Path to JSON file with model outputs")

    args = parser.parse_args()

    if args.command == "collect":
        if args.testset.lower() == "mistdev2025":
            testset = GeneralMTDataset()
            testset.load_data()
            prompts = testset.get_prompts()
            print(json.dumps(prompts, indent=2))
        else:
            print(f"Unknown testset: {args.testset}")

    elif args.command == "score":
        if args.testset.lower() == "mistdev2025":
            testset = GeneralMTDataset()
            testset.load_data()
            prompts = testset.get_prompts()

            with open(args.answers, "r", encoding="utf-8") as f:
                outputs = json.load(f)

            evaluator = MTEvaluator()
            results = evaluator.score(prompts, outputs)

            print(results)
        else:
            print(f"Unknown testset: {args.testset}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
