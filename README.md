# endoQAeval
Repository for "Evaluation of GPT-4 for Patient Question Answering about Endometriosis"

**Table of Contents**

1. [Project Overview](#project-overviewverview)
2. [Repository Overview](#repository-overview)
3. [License](#license)


## Project Overview

### Objective
To investigate the information quality, empathy, and actionability of GPT-4 responses to patient questions regarding endometriosis, a stigmatized and understudied condition. We combine physician and patient perspectives.

### Materials and Methods
We prompt GPT-4 with posts from r/Endo and r/endometriosis, and from r/AskDocs. We recruit 3 patients who suffer from endometriosis and an endometriosis specialist to evaluate the information quality, empathy, and actionability of GPT-4 responses to endometriosis and general medical questions. For each endometriosis question, we use three prompting strategies. We then analyze and compare the quality of the responses across the two sets of questions, question types, and different prompting strategies.

### Results
We find great disagreement across our annotators regarding the quality of answers to both general and endometriosis questions, despite the annotation task closely resembling and following annotation guidelines established in previous studies.

### Discussion
More research is needed to determine what criterias and annotation guidelines are most effective to evaluate the quality of answers to medical questions. Furthermore, new annotation strategies are needed in order to incorporate patient perspectives in the evaluation of generated models for clinical purposes.

## Repository Overview

### `Code` folder
contains the code used to replicate the results from [Ayers et al. (2023)](https://doi.org/10.1001/jamainternmed.2023.1838), generate answers using GPT-4, and create analysis-ready CSV files summarizing the annotators' ratings.
- `analysis` contains the code used to conduct analysis of the ratings: calculate inter-annotator agreement, conduct statistical significance testing to assess the difference in ratings between general and endometriosis answers, and create figures.

### `Data` folder
contains the source data used for this project.

### `Figures` folder
contains the figures to be used in publications about this project.

### `Output` folder
The following are the most important folders and files:
- `endo_responses` folder contains all the GPT-4 responses with different prompting strategies to endometriosis questions.
- `general_responses` folder contains all the GPT-4 responses with different prompting strategies to endometriosis questions.
- `all_annotations.csv` contains all the annotated data.

## License
This repository is released under [ODC-BY](https://opendatacommons.org/licenses/by/1.0/) license. 
By downloading this data you acknowledge that you have read and agreed to all the terms in this license.

