# Do cryptocurrencies extend the mean-variance frontier of an equity investor?
[![](https://img.shields.io/badge/go_to-main_notebook-green)](notebooks/MAIN.ipynb)
[![](https://img.shields.io/badge/go_to-course_homepage-blue)](https://github.com/ipozdeev/it-skills-for-research)

---
*In this project we investigate if cryptocurrencies extend the mean-variance frontier of an equity investor. By using an industry portfolio dataset consisting of 12 different industries collected from Kenneth French data library combined with the 3 largest cryptocurrencies based on market capitalization, we extract the mean-variance frontier. We show that adding cryptocurrencies to the mean-variance frontier has a significant impact.*

# To do:
<span style="color:crimson"> **UPDATE FILES STRUCTURE TREE AT END OF README**</span>

# TABLE OF CONTENTS
[Short step-by-step guide](#short-step-by-step) \
[Pull GitHub repository](#pull-github-repository) \
[Build Docker image](#build-docker-image) \
[Run Docker container](#run-docker-container) \
[Grab data](#data-grabbing) \
[Compile LaTeX report](#latex-compiler) 


# Short step by step
This is a brief walkthrough on the steps needed to reproduce our results. It will be followed by more conprehensive instructions for each of the steps. 
1. Pull github repository
2. Open project in docker container
3. Run [make_dataset.py](src/data/make_dataset.py) to grab data (you need to be in */src/data* when running the script).
4. Run cells in [main notebook](/notebooks/MAIN.ipynb).
5. Use LaTeX compiler (xelatex) to make PDF of Report & Beamer

## Pull GitHub repository
Pull the GitHub repository to desired directory:
```bash
git clone https://github.com/fairwayfinder/crypto-mean-variance-frontier.git
```

## Build docker image
Build the docker image with the provided Dockerfile (approximately 8 min):
```bash
docker build -t my-jupyter-image .
```
where *my-jupyter-image* is an example tag for the image. The dot (.) directs to the Dockerfile in the current directory so make sure you're in the correct folder when running this command. 

### Run Docker container
Run the following code to mount the working directory inside the container to our project folder. Make sure you're in the correct folder when running this. 

```bash
docker run -p 8888:8888 -v $(pwd):/workspace -e JUPYTER_ENABLE_LAB=yes -w /workspace -e JUPYTER_TOKEN='' my-jupyter-image
```

## Data grabbing
### Reproducing data
To reproduce the data in our report, you can run [make_dataset.py](/src/data/make_dataset.py). Please make sure that you're in the */src/data* directory when you run the script. 

### Modifying data
It's possible to make adjustments in [config.py](src/data/config.py) for:
* Date range.
* Choice of industry portfolios (ken french).
* Choice of crypto curencies. 

### To use own data:
The code in the [main notebook](notebooks/MAIN.ipynb) requires a CSV *industry_crypto_returns.csv* located in [data/processed](data/processed/) with the following structure:

<center>

| Date       | industry_1 | industry_2 | ... | industry_n | crypto_1 | ... | crypto_n |
|------------|------------|------------|-----|------------|----------|-----|----------|
| 2020-01-01 | 0.02       | 0.01       | ... | 0.3        | 0.05     | ... | 0.04     |
| ...        | ...        | ...        | ... | ...        | ...      | ... | ...      |
| 2023-04-04 | -0.11      | -0.15      | ... | -0.05      | -0.3     | ... | -0.22    |

</center>

Additionally: A list of the crypto column names (`TICKERS_CRYPTO`) need to be defined in [main notebook](notebooks/MAIN.ipynb).


## LaTeX compiler
To compile the latex report into PDF, please use the following lines of code:

```bash
xelatex Report.tex
bibtex Report.aux
xelatex Report.tex
xelatx Report.tex
```
The same sequence of code can then be run on *Beamer.tex* to compile the beamer. 

The [cleanup.sh](Reports/cleanup.sh) script in [Reports/](Reports/) can be used to clean up the auxiliary files created by the compiler. The following code can be run while in the [Reports/](Reports/) to give the script permission to execute and then run the script:

```bash
chmod +x cleanup.sh
./cleanup.sh 
```

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    │   
    │   
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │   
    │ 
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │
    │
    ├── Reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── Figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


