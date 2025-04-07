# WMT-MIST multilingual instruction shared task

This packages serves for data loading, evaluation, and validation of the [Multilingual Instruction Shared Task](https://www2.statmt.org/wmt25/multilingual-instruction.html) at WMT.

First, install the package:
```
pip3 install git+https://github.com/wmt-conference/wmt-mist
```

## Loading data

To load the data, specify the particular task with `-t` or `--task`:
```bash
wmt-mist -t wmt24++ | jq length
> 54890

wmt-mist -t wmt24metrics | jq length
> 87857

wmt-mist -t mist25dev | jq length
> 87857
```

The output is a JSON array. Taking a look at the first item for the LLM-as-a-judge task contains the source and the system translation that needs to be scored.
```bash
wmt-mist load judge-translation wmt24 | jq '.[0]'
> "Consider this source '''Siso's depictions of land, water center new gallery exhibition''' in English and this translation '''Las representaciones de tierra y agua de Siso protagonizan nueva exposición en galería''' in Spanish; Castilian. Assess the translation quality from 0% to 100%."
```

## Evaluating outputs

For each item in the array you need to add the `output` field with your LLM output, such as 
```json
{
  "prompt": "Given this source '''Už se nudím: Přítel je neschopný''' in cs and translation '''Мені вже нудно: Хлопець нездатний''' in uk, assign a score to the translation on a scale from 0 to 100. Output only the score and nothing else.",
  "output": "80",
}
```

To automatically evaluate, add the `--output` parameter:
```bash
wmt-mist -t mist25dev -o my_outputs.json
```

TODO

## Task overview

Can be specified with the `--task` argument:

- `mist25dev` devset for multilingual instruction shared task
- `wmt24metrics` translation evaluation
- `wmt24`, `wmt24++` translation

## Contributing

- Do not commit large data into this repository.
- Add yourself to the author list in `pyproject.toml`