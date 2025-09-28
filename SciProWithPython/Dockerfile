# Use Miniconda as base image
FROM continuumio/miniconda3:latest

# Set working directory
WORKDIR /app

# Copy environment.yml and create conda environment
COPY environment.yml /app/
RUN conda env create -f environment.yml

# Ensure the environment is activated when running any command
SHELL ["conda", "run", "-n", "physics-plots", "/bin/bash", "-c"]

# Copy all project files
COPY . /app

# Expose default VPython/graphics port if needed (for web VPython)
# EXPOSE 8080

# Run the script using the conda environment
CMD ["bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate physics-plots && python GettingFamiliarWithPlots.py"]
