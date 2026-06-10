import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Estimating Ligand Potency with OpenFE
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Introduction to Alchemical Free Energies
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First, we'll demonstrate runing a basic RBFE campaign from the command line (with no Python at all!).

    The 3 stages described above each correspond to a CLI command:

    **1. setup**: ``openfe plan-rbfe-network``

    **2. run**: ``openfe quickrun``

    **3. gather**: ``openfe gather``

    All you need is your target protein in `.pdb` format, and your candidate ligands in `.sdf` format.
    """)
    return


@app.cell
def _():
    import subprocess

    subprocess.run("openfe")
    # subprocess.run(["openfe plan-rbfe-network -M inputs/tyk2_ligands_charged.sdf -p inputs/tyk2_protein.pdb -o tyk2_campaign"])
    return


@app.cell
def _():


    return


if __name__ == "__main__":
    app.run()
