# crypto_mean_variance
[![](https://img.shields.io/badge/go_to-course_homepage-blue)](https://github.com/ipozdeev/it-skills-for-research)
[![](https://img.shields.io/badge/go_to-data_grabbing_notebook-yellow)](src/data/data_grabbing.ipynb)
[![](https://img.shields.io/badge/go_to-main_notebook-green)](notebooks/MAIN.ipynb)

---

We're researching if the way crypto currienciemean variance efficient frontier
UPDATE THIS

# To do
**Data grabbing**
* <span style="color:red"> **Update datagrabbing part of README**</span>.
* add some kind of "estimated time" to make_dataset.py ? 
* Change naming convention in data grabbing? (e.g. with *f* string in naming, and adding {count(tickers)} at end)
 * This would make it easier when performing robustness checks, but also make it so that a reproducing user might need to look at the name of files when importing csv files in the MAIN notebook.
* Maybe replace config.py with a JSON file --> data grabbing script will be a bit messier though

**Docker**
* Check if compiling of beamer works

**Jupyter notebook**
* Look at ways to make it interactive and nice to use. 
 * Maybe ipy widgets? for interactivity. 

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
3. Run [make_dataset.py](src/data/make_dataset.py) to grab data.
4. Run cells in [main notebook](/notebooks/MAIN.ipynb).

## Pull GitHub repository
Pull the GitHub repository to desired directory:
```bash
Do we need this ?
```

## Build docker image
Build the docker image with the provided Dockerfile:
```bash
docker build -t my-jupyter-image .
```
where *my-jupyter-image* is an example tag for the image. The dot (.) directs to the Dockerfile in the current directory so make sure you're in the correct folder when running this command. 

### Run Docker container
Run the following code to mount the working directory inside the container to our project folder. Make sure you're in the correct folder when running this. 

```bash
docker run -p 8888:8888 -v $(pwd):/workspace -e JUPYTER_ENABLE_LAB=yes -w /workspace -e JUPYTER_TOKEN='' my-jupyter-image
```

OR

```bash
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes my-jupyter-image
```

## Data grabbing
The code in the [main notebook](notebooks/MAIN.ipynb) requires two input CSV files. 
* One with the benchmark portfolio returns 
* One with the returns for the **additional assets only**. 

The structure of the CSVs needs to be:
<center>

| Date       | industry_1 | industry_2 | ... | industry_n |
|------------|------------|------------|-----|------------|
| 2020-01-01 | 0.02       | 0.01       | ... | 0.03       |
| ...        | ...        | ...        | ... | ...        |
| 2023-04-04 | -0.2       | -0.15      |     | -0.05      |

</center>

The data we have used can be downloaded by running the code in the [data grabbing notebook](src/data/data_grabbing.ipynb). The notebook also provides easy adjustment for:
* Date range
* Choice of industry portfolios (ken french)
* Alteration of choice/amount of crypto currencies from yahoo finance

## LaTeX compiler
* Add syntax needed to compile
* Check with sanders if we're using bibtex or biber (only )


```bash
xelatex file.tex
bibtex file.aux
xelatex file.tex
xelatx file.tex
```







Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
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


