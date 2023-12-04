# Starting from Jupyter r-notebook image
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
    texlive-science \ 
    pandoc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install python 3 packages
RUN mamba install --quiet --yes \
    'python=3.11' \
    'matplotlib' \
    'numpy' \
    'pandas' \
    'pandas-datareader' \
    'scipy' \
    'seaborn' \
    'yfinance' \
    && mamba clean --all -f -y

# Switch back to the default jupyter user (jovyan), since its non-root
USER $NB_UID

