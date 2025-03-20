# WMT-MIST multilingual instruction shared task

This packages serves for data loading, evaluation, and validation of the [Multilingual Instruction Shared Task](https://www2.statmt.org/wmt25/multilingual-instruction.html) at WMT.

First, install the package:
```
pip3 install git+https://github.com/wmt-conference/wmt-mist
```

## Loading data

To load the data, use the `load` command and specify the task (`translation`, `reasoning`, `open-ended`, `judge`) and the split (`dev`, `test`):
```bash
wmt-mist load translation dev | jq length
> 7522

wmt-mist load judge dev | jq length
> 88605
```

The output is a JSON array. Taking a look at the first item for the LLM-as-a-judge task contains the source and the system translation that needs to be scored.
```bash
wmt-mist load judge dev | jq '.[0]'
> {
>  "prompt": "Given this source '''Už se nudím: Přítel je neschopný''' in cs and translation '''Мені вже нудно: Хлопець нездатний''' in uk, assign a score to the translation on a scale from 0 to 100. Output only the score and nothing else."
> }
```

## Evaluating outputs

For each item in the array you need to add the `output` field with your LLM output, such as 
```json
{
  "prompt": "Given this source '''Už se nudím: Přítel je neschopný''' in cs and translation '''Мені вже нудно: Хлопець нездатний''' in uk, assign a score to the translation on a scale from 0 to 100. Output only the score and nothing else.",
  "output": "80",
}
```

To automatically evaluate, run the `evaluate` command:
```bash
wmt-mist evaluate translation dev my_outputs.json
```

TODO

## Contributing

- Do not commit large data into this repository.
- Add yourself to the author list in `pyproject.toml`