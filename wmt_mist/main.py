import argparse
import json
import sys
from wmt_mist.datasets.evaluation_translation import EvaluationTranslationDataset
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
        "split",
        help="Dev or test split",
        choices=["dev", "test"]
    )
    parser_load.add_argument(
        "--year",
        help="Which year of the testset to load, default is the current",
        default="2025",
        choices=["2025"],
    )

    # sub-command for evaluating results
    parser_eval = subparsers.add_parser("evaluate", help="Score outputs for a given testset")
    parser_eval.add_argument(
        "task",
        help="Name of the task",
        choices=["translation", "open-ended", "reasoning", "judge"]
    )
    parser_eval.add_argument(
        "split",
        help="Dev or test split",
        choices=["dev", "test"]
    )
    parser_eval.add_argument(
        "--year",
        help="Which year of the testset to load, default is the current",
        default="2025",
        choices=["2025"],
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
        "split",
        help="Dev or test split",
        choices=["dev", "test"]
    )
    parser_mock.add_argument(
        "--year",
        help="Which year of the testset to load, default is the current",
        default="2025",
        choices=["2025"],
    )

    args = parser.parse_args()


    if args.command == "load":
        if args.split == "test":
            print("Testset prompts are not available yet.", file=sys.stderr)
        
        if args.task.lower() == "translation" and args.split.lower() == "dev":
            prompts = TranslationDataset(year=args.year, split="dev").dump_data()
            print(json.dumps(prompts, indent=2, ensure_ascii=False))
        elif args.task.lower() == "open-ended" and args.split.lower() == "dev":
            print("TODO")
        elif args.task.lower() == "reasoning" and args.split.lower() == "dev":
            print("TODO")
        elif args.task.lower() == "judge" and args.split.lower() == "dev":
            # TODO: join with open-ended dataset
            prompts = EvaluationTranslationDataset(year=args.year, split="dev").dump_data()
            print(json.dumps(prompts, indent=2, ensure_ascii=False))

    elif args.command == "evaluate":
        if args.split == "test":
            print("Testset prompts are not available yet.", file=sys.stderr)
        print("Devset prompts are not available yet.", file=sys.stderr)
        # if args.testset.lower() == "mistdev2025":
        #     dataset = TranslationDataset()
        #     dataset.load_data()
        #     prompts = dataset.dump_data()

        #     with open(args.answers, "r", encoding="utf-8") as f:
        #         outputs = json.load(f)

        #     evaluator = TranslationEvaluator()
        #     results = evaluator.score(prompts, outputs)

        #     print(results)
        # else:
        #     print(f"Unknown testset: {args.testset}")

    elif args.command == "mock":
        pass
        # TODO

if __name__ == "__main__":
    main_cli()
