# WMT-MIST multilingual instruction shared task

This packages serves for data loading, evaluation, and validation of the [Multilingual Instruction Shared Task](https://www2.statmt.org/wmt25/multilingual-instruction.html) at WMT.

First, install the package:
```
pip3 install git+https://github.com/wmt-conference/wmt-mist
```

## Loading data

To load the data, use the `load` command and specify the task (`translation`, `reasoning`, `open-ended`, `judge`) and the split (`dev`, `test`):
```bash
wmt-mist load translation wmt24 | jq length
> 10301

wmt-mist load judge-translation wmt24 | jq length
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

To automatically evaluate, run the `evaluate` command:
```bash
wmt-mist evaluate translation wmt24 my_outputs.json
```

TODO

## Contributing

- Do not commit large data into this repository.
- Add yourself to the author list in `pyproject.toml`