# Starting from Jupyter base notebook image
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
    pandoc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Switch back to the default jupyter user (jovyan), since its non-root
USER jovyan

# Installing python libraries using mamba
RUN mamba install matplotlib numpy
