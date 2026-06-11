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
    The OpenFE ecosystem is an open-source framework for calculating alchemical free energies.


    Binding free energies are one metric used to predict which ligand might bind best to a target protein and are often used in **computational drug discovery campaigns**.

    This notebook demonstrates how you can use either the **CLI or Python API** to execute physics-based simulations and calculate relative binding free energies (RBFE) for a series of ligands and a given protein.


    - ``.sdf`` format: [chemical data file format](https://en.wikipedia.org/wiki/Chemical_table_file#SDF) used to describe small molecules.
    - ``.pdb`` format: [protein data bank](https://www.wwpdb.org/) standardized file format for describing proteins:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    OpenFE free energy calculations can be thought of as 3 distinct steps, each of which corresponds to a CLI command.


    1. **Plan**: `openfe plan-rbfe-networl` construct a graph relating the ligands
    2. **Run**: execute a physics-based simulation
    3. **Gather**: compute meaningful metrics from the simulation data

    **1. **: ``openfe plan-rbfe-network``

    **2. run**: ``openfe quickrun``

    **3. gather**: ``openfe gather``

    All you need is your target protein in `.pdb` format, and your candidate ligands in `.sdf` format.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Running a relative binding free energy campaign from a candidate ligand
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    target protein: BACE-1
    """)
    return


@app.cell
def _(mo):
    import py3Dmol
    v = py3Dmol.view('7DCZ',height=400,width="100%",style='cartoon')
    mo.iframe(v.write_html(fullpage=True),height=420)
    return


app._unparsable_cell(
    r"""
    Ωimport gufe, konnektor
    from rdkit import Chem
    from gufe import SmallMoleculeComponent
    """,
    name="_"
)


@app.cell
def _(gufe):
    lomap_network = gufe.LigandNetwork.from_json("inputs/lomap_network.json")
    return (lomap_network,)


@app.cell
def _(lomap_network):
    from konnektor.visualization import draw_ligand_network

    draw_ligand_network(lomap_network)
    return


@app.cell
def _(Chem, SmallMoleculeComponent):
    ligands_sdf = Chem.SDMolSupplier('inputs/ligands.sdf', removeHs=False)
    from rdkit.Chem import AllChem

    ligand_mols = [SmallMoleculeComponent(sdf) for sdf in ligands_sdf]

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
