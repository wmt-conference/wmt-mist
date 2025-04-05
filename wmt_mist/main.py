import argparse
import json
import sys
from wmt_mist.datasets.judge_translation import JudgeTranslationDataset
from .datasets.translation import TranslationDataset
from .evaluators.translation import TranslationEvaluator

def main_cli():
    parser = argparse.ArgumentParser(
        description="WMT MIST scoring"
    )
    subparsers = parser.add_subparsers(dest="command", help="Sub-command to run")

    # sub-command for loading data
    parser_load = subparsers.add_parser("load", help="Load prompts for a given testset")
    parser_load.add_argument(
        "task",
        help="Name of the task",
        choices=["translation", "open-ended", "reasoning", "judge"]
    )
    parser_load.add_argument(
        "dataset",
        help="Dataset name",
        choices=["wmt24pp", "wmt24++"]
    )

    # sub-command for evaluating results
    parser_eval = subparsers.add_parser("evaluate", help="Score outputs for a given testset")
    parser_eval.add_argument(
        "task",
        help="Name of the task",
        choices=["translation", "open-ended", "reasoning", "judge"]
    )
    parser_eval.add_argument(
        "dataset",
        help="Dataset name",
        choices=["wmt24pp", "wmt24++"]
    )
    parser_eval.add_argument("answers", help="Path to JSON file with model outputs")

    # sub-command for mock outputs
    parser_mock = subparsers.add_parser("mock", help="Score outputs for a given testset")
    parser_mock.add_argument(
        "task",
        help="Name of the task",
        choices=["translation", "open-ended", "reasoning", "judge"]
    )
    parser_mock.add_argument(
        "dataset",
        help="Dataset name",
        choices=["wmt24pp", "wmt24++"]
    )

    args = parser.parse_args()


    if args.command == "load":        
        if args.task.lower() == "translation":
            prompts = TranslationDataset(dataset=args.dataset).dump_data()
            print(json.dumps(prompts, indent=2, ensure_ascii=False))
        elif args.task.lower() == "open-ended":
            print("TODO")
        elif args.task.lower() == "reasoning":
            print("TODO")
        elif args.task.lower() == "judge":
            if args.dataset in {"wmt24pp", "wmt24++"}:
                prompts = JudgeTranslationDataset(dataset=args.dataset).dump_data()
            else:
                raise ValueError(f"Unsupported dataset for the judge task {args.dataset}")
            print(json.dumps(prompts, indent=2, ensure_ascii=False))

    elif args.command == "evaluate":
        print("Evaluation is not available yet.", file=sys.stderr)

    elif args.command == "mock":
        print("Mock outputs are not available yet.", file=sys.stderr)

if __name__ == "__main__":
    main_cli()
