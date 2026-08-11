# OpenFE Demo: OMSF Stack Tour 2026-06-24

You can find the demo notebook in `src/openfe_demo.ipynb`.

See the [openfe git repo](https://github.com/OpenFreeEnergy/openfe) and [documentation](https://docs.openfree.energy/en/latest/) to learn more!

## Running the demo locally

### using `pixi` 

In this directory, run:

```bash
pixi run demo
```


### using `micromamba`
To run the notebook locally, you'll need to install **openfe**:

You can instead use `micromamba` (recommended), `mamba` or `conda`:

```bash

micromamba create -f env.yaml
micromamba activate openfe-demo

```

then open the demo with `jupyter notebook src/openfe_demo.ipynb`.

