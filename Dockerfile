# Starting from Jupyter base notebook image
FROM jupyter/base-notebook

#Switch to the root user to install packages
USER root

# Switch back to the default jupyter user (jovyan), since its non-root
USER jovyan

# Installing python libraries using mamba (tried adding -y since it was getting stuck)
RUN mamba install matplotlib numpy pandas scipy scipy.optimize matplotlib.pyplot yfinance -y
