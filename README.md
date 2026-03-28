# KG-EDAS: A Meta-Metric Framework for Evaluating Knowledge Graph Completion Models

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

##  Associated Research Paper

**Title**: KG-EDAS: A Meta-Metric Framework for Evaluating Knowledge Graph Completion Models  
**Authors**: Haji Gul¹, Abdul Ghani Naim¹, Ajaz Ahmad Bhat¹*  
**Affiliation**: School of Digital Science, Universiti Brunei Darussalam  

**Paper Link**: [IEEE Big Data 2025](https://www.computer.org/csdl/proceedings-article/bigdata/2025/11402521/2eDtzuJkX9S)   
**ORCIDs**:  
- Haji Gul: [0000-0002-2227-6564](https://orcid.org/0000-0002-2227-6564)  
- Abdul Ghani Naim: [0000-0002-7778-4961](https://orcid.org/0000-0002-7778-4961)  
- Ajaz Ahmad Bhat: [0000-0002-6992-8224](https://orcid.org/0000-0002-6992-8224)

**Abstract**:  
KGs are often incomplete, missing entities and relations, an issue addressed by Knowledge Graph Completion (KGC) methods that predict missing elements. Mean Reciprocal Rank (MRR), Mean Rank (MR), and Hit@k (e.g., MRR) are commonly used to assess the performance of KGC models. A major challenge in evaluating KGC models however, lies in comparing their performance across multiple datasets and metrics. A model may outperform others on one dataset but underperform on another, making it difficult to determine overall superiority. Moreover, even within a single dataset, different metrics such as MRR and Hit@1 can yield conflicting rankings, where one model excels in MRR while another performs better in Hit@1, further complicating model selection for downstream tasks.  To address this fragmentation, we propose \textbf{KG-EDAS}, Inspired by Inspired by Multi-Criteria Decision-Making (MCDM), \textit{E}valuation based on \textit{D}istance from \textit{A}verage \textit{S}olution (EDAS), a robust meta-metric that synthesizes model performance across multiple datasets and diverse evaluation criteria into a single normalized score ($M_i \in [0,1]$). Experiments on five standard datasets show that KG-EDAS produces stable, interpretable rankings highly correlated with MRR ($\rho=0.93$) while resolving conflicts across metrics. In addition, it integrates multi-metric, multi-dataset performance into a unified ranking, offering a consistent, robust, and generalizable framework that resolves conflicting rankings and supports informed model selection in real-world KGC applications. We argue that KG-EDAS offers a principled foundation for standardized evaluation in KGC—enabling fair comparisons and supporting automated model selection.

### Keywords:   
Knowledge Graph Embedding, Link Prediction, Evaluation Metrics, Multi-criteria Decision Making, Model Ranking, Performance Aggregation


## Structure


#
KG-EDAS/  
├── dataloader.py  
├── edas.py  
├── utils.py  
├── main.py  
├── tail_prediction_results.csv          # Example input (tail prediction)  
├── README.md  
├── paper/  
│   ├── IEEE_BigData__KG_EDAS_.pdf       # Full paper  
│── Figure1.png                     
└── outputs/                             # Generated results (gitignored)  

---


## Figure 1 from the Paper  
**Figure 1**: Comparison of prediction metrics across datasets. The left image shows the relation prediction $(h, ?, t)$ comparison of **mean MRR** and **EDAS $M$** values across datasets: FB15k-237, FB15k, WN18, WN18RR, and YAGO3-10.  The second image shows the comparison of **mean Hit@1** and **EDAS $M$-values**.

![KG-EDAS Figure 1](FB237_MRR_Hit1_vs_EDAS.png)

![KG-EDAS Figure 1](Combined_MRR_Hit1_vs_EDAS.png)



## Citation

@INPROCEEDINGS{11402521,
  author    = {Gul, Haji and Naim, Abdul Ghani and Bhat, Ajaz Ahmad},
  booktitle = {2025 IEEE International Conference on Big Data (BigData)},
  title     = {{KG-EDAS: A Meta-Metric Framework for Evaluating Knowledge Graph Completion Models}},
  year      = {2025},
  pages     = {2823-2832},
  doi       = {10.1109/BigData66926.2025.11402521},
  url       = { [IEEE Big Data 2025](https://www.computer.org/csdl/proceedings-article/bigdata/2025/11402521/2eDtzuJkX9S)},
  publisher = {IEEE Computer Society},
  address   = {Los Alamitos, CA, USA},
  month     = {Dec}
}




