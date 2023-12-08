# Starting from Jupyter base image, maybe switch to scipy but will bloat our image a bit. 
FROM jupyter/base-notebook

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

# Install python 3 packages --> could add specific version numbers, 
RUN mamba install --quiet --yes \
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

