# crypto_mean_variance
[![](https://img.shields.io/badge/go_to-course_homepage-blue)](https://github.com/ipozdeev/it-skills-for-research)
[![](https://img.shields.io/badge/go_to-data_grabbing_notebook-yellow)](src/data/GDLC_data.ipynb)
[![](https://img.shields.io/badge/go_to-main_notebook-green)](notebooks/MAIN.ipynb)

==============================

**TABLE OF CONTENTS** \
[Short step-by-step guide](#build-docker-image)




We're researching if the way crypto currienciemean variance efficient frontier
UPDATE THIS

# Notes - Thomas
### Build docker image

**Build docker image**
```bash
docker build -t my-jupyter-image .
```
where *my-jupyter-image* is the tag we choose for this image and . will use the dockerfile in the current directory. (make sure you're in the correct wd folder when running this command.)


**run this to start jupyter notebook session:**
```bash
docker run -p 8888:8888 -v $(pwd):/workspace -e JUPYTER_ENABLE_LAB=yes -w /workspace -e JUPYTER_TOKEN='' my-jupyter-image
```

OR

```bash
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes my-jupyter-image
```

# To do
**Data grabbing**
* Look up how to mkdir data/processed and data/raw. (since they are in the .gitignore)
* change the data grabbing to .py files instead of ipynb.
* make script to run both the data grabbing scripts?
* ken french data grabbing is suboptimal and takes approx 20 sec. --> check if time!
 * Data grabbing can get faster with paralell tasks --> concurrent.futures (feels a bit unneccessary for us)
* Double check ken french return conversion to log return!


**Readme**
* instructions for all steps for reproduction
* link to headers/files when they are mentioned

**Docker**
* Remove r & r-libraries from dockerimage

**Jupyter notebook**
* Look at ways to make it interactive and nice to use. 
 * Maybe ipy widgets? for interactivity. 

# Data
The code in the main notebook requires two input CSV files. One with the benchmark portfolio returns and one with the returns for the **additional assets only**. 
The structure of the CSVs needs to be.

| Date       | industry_1 | industry_2 | ... | industry_n |
|------------|------------|------------|-----|------------|
| 2020-01-01 | 0.02       | 0.01       | ... | 0.03       |
| ...        | ...        | ...        | ... | ...        |
| 2023-04-04 | -0.2       | -0.15      |     | -0.05      |

The data we have used can be downloaded by running the code in the [data grabbing notebook](src/data/GDLC_data.ipynb). The notebook also provides easy adjustment for:
* Data range
* Choice of industry portfolios (ken french)
* Alteration of additional assets from yahoo finance




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


