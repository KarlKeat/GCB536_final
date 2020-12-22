import pandas as pd
import os


def format_scpopcorn_data(file_path, type):
    genes = pd.read_csv(
        os.path.join(file_path, 'genes.tsv'),
        sep='\t',
        names=["gene_id", "gene"],
        header=None
    )

    gene_map = dict(zip(
        genes.index+1,
        genes.gene
    ))

    barcodes = pd.read_csv(
        os.path.join(file_path, 'barcodes.tsv'),
        sep='\t',
        names=["cell_id"],
        header=None
    )

    cell_map = dict(zip(
        barcodes.index+1,
        barcodes.cell_id
    ))

    matrix = pd.read_csv(
        os.path.join(file_path, 'matrix.mtx'),
        sep=' ',
        skiprows=[0, 1],
        header=None,
        names=["gene_index", "cell_index", "count"]
    )

    matrix["gene"] = matrix["gene_index"].map(gene_map) 
    matrix["cell"] = matrix["cell_index"].map(cell_map)

    matrix = (
        matrix
        .pivot_table(index='gene', columns='cell', values='count', aggfunc='first')
        .fillna(0)
    )

    matrix.index.names = [None]
    matrix.to_csv(f"{type}.tsv", sep='\t')


if __name__ == "__main__":
    WT_PATH = "data/WT_TRAF6_10X/filtered_gene_bc_matrices/mm10/"
    KO_PATH = "data/KO_TRAF6_10X/filtered_gene_bc_matrices/mm10/"

    format_scpopcorn_data(WT_PATH, "wt")
    format_scpopcorn_data(KO_PATH, "ko")
