# Example python environment using conda

Example of a simple python project using conda

### Dependencies

Requires `conda` to be installed

### Installation

First create and activate your conda environment using the provided `environment.yml`:

```bash
conda env create --prefix ./env --file environment.yml
conda activate ./env
```

### Usage

Run the script like so:

```bash
python ./draw_molecule.py
```
