import argparse
import json
import sys
from wmt_mist.datasets.base import BaseDataset
from wmt_mist.datasets.judge_translation import JudgeTranslationDataset
from wmt_mist.datasets.translation import TranslationDataset

def main_cli():
    parser = argparse.ArgumentParser(
        description="WMT MIST scoring"
    )
    parser.add_argument(
        "-t", "--task",
        help="Dataset/task name",
        choices=["wmt24metrics", "wmt24++", "mist25dev", "mist25"],
        required=True,
    )
    parser.add_argument(
        "-o", "--output",
        help="Model outputs to evaluate"
    )
    parser.add_argument(
        "-m", "--mock",
        help="Generate mock model outputs"
    )

    args = parser.parse_args()

    if args.output is None:
        print(json.dumps(load_prompts(args.task), indent=2, ensure_ascii=False))
    else:
        print("Evaluation of outputs is not available yet.", file=sys.stderr)


def load_prompts(task):
    if task in {"wmt24", "wmt24++"}:
        return TranslationDataset(task=task).dump_data()
    elif task in {"wmt24metrics"}:
        return JudgeTranslationDataset(task=task).dump_data()
    elif task in {"mist25dev"}:
        return (
            TranslationDataset(task="wmt24++").dump_data()+
            JudgeTranslationDataset(task="wmt24metrics").dump_data()
        )
    else:
        print("Task is not available.", file=sys.stderr)


if __name__ == "__main__":
    main_cli()
