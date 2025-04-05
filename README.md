# Query by Vocal Imitation challenge - Submission

This repository contains the submission package of [Query by Vocal Imitation challenge](https://qvim-aes.github.io/) at the [2025 AES International Conference on Artificial Intelligence and Machine Learning for Audio](https://aes2.org/events-calendar/2025-aes-international-conference-on-artificial-intelligence-and-machine-learning-for-audio/).

Participants should clone this repository, and please ensure that you can successfully run [submission_template.ipynb](submission_template.ipynb) within the repository. Detailed instructions are provided in the template file. 

For your final submission, please submit only the completed template file, and rename the template as {teamname}_{submissionNumber}.ipynb. Please note that we only accept 3 submissions per team. 


## Setup

Your inference code will be run on Ubuntu (24.04) using a conda environment with Python 3.10.
Additional packages must be installed with pip in the notebooks directly (see the two example notebooks).
You may use the functions provided in `helpers.py`; however, do not modify this file.


Prerequisites:
- [conda](https://www.anaconda.com/docs/getting-started/miniconda/install), e.g., [Miniconda3-latest-Linux-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)


1. Clone this repository.

```
git clone https://github.com/qvim-aes/qvim-submission.git
```

2. Create and activate a conda environment with Python 3.10:

```
conda create -n qvim-submission python=3.10 jupyter
python -m jupyterlab
```

## Evaluation Results
Running the example notebooks should give the following results:


| Model Name   | MRR (exact match) | NDCG (category match) |
|--------------|-------------------|-----------------------|
| random       | 0.0444            | ~0.337                |
| 2DFT         | 0.1262            | 0.4793                |
| MN baseline  | 0.2726            | 0.6463                |