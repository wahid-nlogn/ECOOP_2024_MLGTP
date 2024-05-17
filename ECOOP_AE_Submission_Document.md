# Artifact Submission Template

Please answer the following questions concisely, either with bullet lists or short paragraphs.

Title of the submitted paper: Learning Gradual Typing Performance
ECOOP submission number for the paper: 45

## Metadata to provide during artifact submission in HotCRP

**No need to provide them again in the submission**

- OS and resource (CPU, memory, disk, GPU) used by the authors to run the artifact
- Estimation of the required hardware resources for evaluation. In case the evaluation takes multiple days or requires huge resources, please provide a scaled-down evaluation.
- Known compatibility issues of the container/VM.
- Which badges do you claim for your artifact? Functional? Reusable? Available?

## Quick-start guide (Kick-the-tires phase)

Please describe how reviewers can check the artifact's integrity and basic functionality.
- Simply running the container using the "run" command will generate a sample result in the command promot. Also it will generate the figures(figure 7,8,9) of our paper 
- Respected reveiwers can also run each of the Python file individually using "python source_file" command.

## Overview: What does the artifact comprise?

Please list for each distinct component of your artifact:

* type of artifact (data, code, proof, etc.)
* format (e.g., CSV, source code, binary, etc.)
* location in the container/VM
- We dividie our artificat into several componenets. 
- In Level-1 folder we included all the benchmarks we are using, its different configurations(discussed in Table-3 of our paper), we have also included the running time in log.txt file into each benchmark directory.
- In Level-2 folder has several subdirectory for example "datasets" has all the cast_cost vector , bit_strings vecotr, run time of each configuration files in .txt format. For example "raytrace_fc_nli_parcast.txt" has the cast_cost vector of 33904 "Raytrace" benchmark configurations,  "raytrace_log.txt.txt" has the running time of 33904 Raytrace benchmark configuration. And "raytrace_bits.txt" has the bit vectors.
- In Leve-3 folder we included all our source code for running different experiments. File_Name reffers to the experiment.
- retic-0.1.0-py3.6.egg folder is the reticulated python we are using for this projects. 

## For authors claiming an available badge

We offer to publish the artifact on [DARTS](https://drops.dagstuhl.de/opus/institut_darts.php), in which case the available badge will be issued automatically.
If you agree to publishing your artifact under a Creative Commons license, please indicate this here.
-Yes I would like to publish under a Creative Commons license 
In case you would like to publish your artifact under different licensing conditions on Zenodo, please state under which license will the artifact be published?

## For authors claiming a functional or reusable badge

For **all** experimental claims made in the paper, please:


Please note: we highly advise authors to provide a push-button evaluation (cf. call for artifacts).
- The data in table 2 can be obtained by running script "TABLE-2_BIT_STRING_Performance.py"
- The data in table 4 can be obtained by running script "TABLE-4_CAST_COST_performance.py"
- The data in table 5 can be obtained by running script "Table-5_Neighbors_preformance.py"
- The data in table 7 can be obtained by running script "Table-7_Transient_cast.py"
- The figure-7 can be obtained by running script "Figure-7_NumberofTyped_VS_Runtime.py"
- The figure-9 can be obtained by running script "Figure-9_NumberofTyped_VS_RunTime_transient.py"
- The data in table 1 can be obtained by running script "Table_1_DeepLearning_using_Embeddings.py"
## For authors claiming a reusable badge

- Many part of our artifact are resuable. 
- For example our datasets can be used by other reseachers for their purposes.
- We used Linear regression in TABLE-2_BIT_STRING_Performance.py, TABLE-4_CAST_COST_performance.py,Table-7_Transient_cast.py, other reseacher might uses other algorithms to measure the performance.
- Table_1_DeepLearning_using_Embeddings.py researcher may use different deeplearning algorithm and technique. 
