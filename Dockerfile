# Starting from Jupyter base notebook image
FROM jupyter/r-notebook

#Switch to the root user to install packages
USER root

#Install LaTeX packages for compilation (and updating)  (check if we need this later) 
# texlive-xetex is a lighter LaTeX package that should suffice for our needs
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra \
    pandoc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install python 3 packages
RUN mamba install --quiet --yes \
    'python=3.11' \
    'matplotlib' \
    'numpy' \
    'pandas' \
    'scipy' \
    'seaborn' \
    'yfinance' \
    && mamba clean --all -f -y

# Install R packages
RUN mamba install --quiet --yes \
    'r-base' \
    'r-fportfolio' \
    'r-fbasics' \
    'r-fassets' \
    'r-lubridate' \
    'r-quantmod' \
    'r-readr' \
    'r-tidyr' \
    'r-xml' \
    # remove package installation caches etc, -f to avoid prompts, -y to answer yes to prompts. 
    && mamba clean --all -f -y 

# Switch back to the default jupyter user (jovyan), since its non-root
USER $NB_UID

