# Starting from Jupyter base notebook image
FROM jupyter/base-notebook

#Switch to the root user to install packages
USER root

#Install LaTeX packages for compilation (check if we need this later)
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-generic-recommended

# Switch back to the default jupyter user (jovyan), since its non-root
USER jovyan
