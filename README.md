# JupyLabel Cli

This extension is composed of a Python package named `notebook_labeling`
for the server extension and a NPM package named `notebook_labeling`
for the frontend extension.

## Research 
The corresponding paper can be found under: https://arxiv.org/abs/2403.07562

## Requirements

- JupyterLab >= 4.0.0
- Python 3.10

## Prerequisites

Create a conda environtment and set it up:
```sh
conda create -n {name} python=3.10
conda activate {name}
pip install -r requirements.txt
```

If you want to use your conda kernels in JupyterLab install the following package in your created virutal env:
```sh
conda install -c conda-forge nb_conda_kernels 
```

## Install

To install the extension, cd into the root folder and execute:

```sh
pip install -e .
jupyter server extension enable jupyterlab_examples_server
jlpm run build
```

## Starting the extention
Simply activate your created environment and run:
```sh 
jupyter lab
``` 
After that take a Jupyter Notebook of your choice and click the Label Notebook button. There are also some notebooks where you can test the extension on.

Some example notebooks can be found in the notebooks folder.

## Uninstall

To remove the extension, execute:

```sh
pip uninstall notebook_labeling
```

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```sh
jupyter server extension list
```

If the server extension is installed and enabled, but you are not seeing
the frontend extension, check the frontend extension is installed:

```sh
jupyter labextension list
```

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```sh
# Clone the repo to your local environment
# Change directory to the notebook_labeling directory
# Install package in development mode
pip install -e ".[test]"
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Server extension must be manually installed in develop mode
jupyter server extension enable notebook_labeling
# Rebuild extension Typescript source after making changes
jlpm build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```sh
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```sh
jupyter lab build --minimize=False
```

### Development uninstall

```sh
# Server extension must be manually disabled in develop mode
jupyter server extension disable notebook_labeling
pip uninstall notebook_labeling
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `notebook_labeling` within that folder.