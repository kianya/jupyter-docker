# Pick your favorite docker-stacks image
FROM jupyter/scipy-notebook:latest

USER root
ENTRYPOINT ["/bin/sh"]
# Add permanent apt-get installs and other root commands here
# e.g., RUN apt-get install npm nodejs

RUN apt-get update && apt-get install -y  postgresql-client curl nano

USER jovyan
# Add permanent pip/conda installs, data files, other user libs here
# e.g., RUN pip install jupyter_dashboards

# running notebook with password ''

RUN yes | jupyter notebook --generate-config
RUN echo "c.NotebookApp.password = 'sha1:e96e48af7c0d:4df487a2149398c594b6f6aadec1443f4cc5663c'">>/home/jovyan/.jupyter/jupyter_notebook_config.py

ENTRYPOINT ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]