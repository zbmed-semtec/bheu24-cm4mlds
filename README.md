# bheu24-cm4mlds
BioHackathon Europe 2024 repository to explore Croissant ML metadata extraction from ML platforms such as HuggingFace.

## BioHackathon Proposal

__Abstract__
To advance the use of Machine Learning for the understanding of diseases and conservation of biodiversity is important to promote FAIR AI-ready datasets since data scientists and bioinformaticians spend 80% of their time in data finding and preparation. Metadata descriptors for datasets are pivotal for the creation of Machine Learning Models as they facilitate the definition of strategies for data discovery, feature selection, data cleaning and data pre-processing.

~~Once a dataset is AI-ready, such metadata descriptors change wrt the initial version of the raw data. What can we learn from the metadata of raw vs AI-ready datasets? What transformations from raw to AI-ready could be (semi)automated based on metadata descriptors? In this project, we will manually analyze and curate metadata descriptors before and after AI-readiness. Based on our analysis, we will identify dataset transformations that could be (semi)automated by software pipelines with the aim of alleviating the effort and time invested in data pre-processing for Machine Learning.~~

ML-ready datasets, whether by design or after pre-processing, can be enriched with metadata so they become FAIRer, with all benefits that come from FAIR. [Croissant ML](https://research.google/blog/croissant-a-metadata-format-for-ml-ready-datasets/) is an extension of schema.org to better describe ML-ready datasets, released early 2024 and already adopted by some ML-model platforms such as [Hugging Face](https://huggingface.co/) (see [Croissant ML viewer documentation](https://huggingface.co/docs/dataset-viewer/mlcroissant))and OpenML. However, as it commonly happens with metadata, there are some limitations to the amount of metadata that can be automatically extracted. How much Croissant metadata can be programmatically extracted from ML-ready datasets? How this automation could be improved? In this project, we will explore answers to these two questions. 

The results will be later integrated into a metadata-based reproducibility assessment cycle, part of the NFDI4DataScience project in Germany. To facilitate the work during the BioHackathon, we will focus on [datasets in HuggingFace](https://huggingface.co/datasets) and/or datasets from the [DOME registry](https://registry.dome-ml.org/) as this would indicate already some level of availability for the metadata. ~~The AI-ready metadata descriptors will use the Croissant schema proposed by the ML Commons. This project will also take into account previous work done at the BioHackathon 2022 on metadata for synthetic data.~~

Note: we have modified the intial idea as metadata created by metadata experts is time-consuming and does not necessarily refelct the metadata level that is commonly available in ML-models platforms. We think that a programmatic approach will be of more benefit for the ultimate goal of improving automatically extraction and enrichment metadata for AI/ML-ready datasets.

__Co-leads__
Leyla Jael Castro, Nuria Queralt Rosinach

## BioHackathon Plan

Depending on the participants skills and time (some might be collaborating to another project), the plan bellow will be modified and fine-tuned.

We also have a [document for notes and additional information](https://docs.google.com/document/d/1arwiX3ana9WLk4vPcHeK1ksCDaznxHUB8KTdz_d7fYg).

1. Get familiar with Croissant ML specification, examples and Python library
2. Retrieve Croissant metadata for Hugging Face datasets & OpenML
    -  Hugging Face embeds Croissant JSON-LD directly in the HTML of dataset pages. It also offers ways to download the Croissant JSON-LD file:
        Via a Croissant tag button on the dataset's page (ex: https://huggingface.co/datasets/CohereForAI/aya_collection)
        Via their API (ex: https://huggingface.co/api/datasets/CohereForAI/aya_collection/croissant)
    - OpenML offers a Croissant button on all of their datasets to download the underlying Croissant JSON-LD file. More information can be found [here](https://docs.openml.org/).
    
3. Create a Knowledge Graph from the harvested metadata
4. Analyze how many of the Croissant schema is covered
5. Discuss what sort of corpus would be necessary to increase coverage with ML approaches

## Project execution

### Virtuoso database
There are 2 ways to use the Virtuoso database:
1. Using the docker setup:
To use the docker setup, you need to have docker and docker-compose installed on your machine.
After cloning the repository, run the following commands in the root directory of the repository.
    
    First, build the docker image:
    ```
    docker-compose build
    ```
    
    To start the docker containers, run the following command:
    ```
    docker-compose up -d
    ```

    To just run the example run the following command:
    ```
    docker exec -it app core/main.py
    ```

    To enter the container with the python app that interacts with Virtuoso database, run the following command:
    ```
    docker exec -it app /bin/bash
    ```
2. Using the local setup:
To use the local setup, you need to have Python 3.10, pip and the virtuoso database installed on your machine. 
    
    This setup has been tested on Ubuntu 22.04, and probably only works on Linux systems. For Windows, is recommended to install WSL2 (Windows Subsystem for Linux) and follow the steps for the Linux setup.
    
    After cloning the repository, run the following commands in the root directory of the repository.
    
    Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
    Install the Virtuoso database, you can follow instructions from the official [website](https://vos.openlinksw.com/owiki/wiki/VOS/VOSUbuntuNotes#Installing%20Virtuoso%20with%20Ubuntu%20Packages).

    Give read and write permissions to the folder containing the data files:
    ```
    sudo chmod +rwx ./core/data/
    ```
    
    To run the app, run the following command:
    ```
    python3 core/main.py
    ```

## Participants

- Dhwani Solanki
- Rohitha Ravinder
- Nelson Quiñones
- You?


