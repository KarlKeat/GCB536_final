# Title     : start code
# Objective : Loading 10x data as dgcMatrix
# Created by: Da Kuang
# Created on: 11/15/20
library(Seurat)

WT_PATH<- "data/WT_TRAF6_10X/filtered_gene_bc_matrices/mm10"
KO_PATH<- "data/KO_TRAF6_10X/filtered_gene_bc_matrices/mm10"
wt_data <- Read10X(data.dir = WT_PATH)
ko_data <- Read10X(data.dir = KO_PATH)
dim(wt_data)
dim(ko_data)