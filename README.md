

# Overview
This directory contains material prepared by UMass to facilitate training sessions with Unillanos and Alisos staff. The training focuses on use of the Orinoquia Water Futures (OWF), with initial emphasis on users gaining familiarity with modeling framework. The presentation used during the kick off meeting is available [here](https://github.com/BaptisteFrancois/Orinoquia_Water_Futures/tree/Training/Introduction) while the recording of the session is available [here](https://drive.google.com/drive/folders/1COQbinFeURKuuQ9Tpqz0kKhsaPchcDhd?usp=sharing) for a duration of 30 days after the meeting. 


# How to use this repository

- Forked the repository to their own GitHub account. Once forked, you will get be a copy of this repository on you user's GitHub account. The user can make changes to this copy without affecting the original repository. To fork a repository, the user needs to have a GitHub account and be logged in. Once logged in, the user can navigate to the repository they want to fork and click on the `Fork` button in the top right corner of the page. This will create a copy of the repository in their own account.
- You should be able to update the repo by clicking on the `Sync fork` button in the top right corner of the page. This will update your forked repository with any changes made to the original repository. If you are not familiar with this process, please refer to the following link: [GitHub - Sync a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)
- Cloned the repository to their local machine using the command line interface (CLI) or GitHub Desktop application. If you are not familiar with this process, please refer to the following link: [GitHub - Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- With the command line interface (CLI), the user can clone the repository using the following command (note that the URL may need to be updated to match the current version of the repository):
```
    git clone --branch Training --single-branch 'the link to the forked repository on your github account' Training
    cd Training
    git status
```
The link to your Git repository can easily be accessed by clicking on `Code` (big green push button), then by selecting HTTPS and clicking on the `copy url to clipboard` icon. For instance mine is: https://github.com/BaptisteFrancois/Orinoquia_Water_Futures.git


If you need to learn some basics of Git, please refer to the following link: [Introduction to GitHub](https://github.com/skills/introduction-to-github?tab=readme-ov-file)
:::

-  If returning to this instruction after cloning the repo at an earlier time, confirm that the working directory is on the `Training` branch with `git status` and that the branch is up to date with the remote with `git pull`
-  Change directory to UMass_Training_01, where this file is found


# Alternate
Instead of cloning the branch of the repository, the contents of the branch can also be downloaded as a zip file (by clicking on `Download ZIP` available from the options after having clicked on the big green button `Code`). Next, the user will need to manually link their local copy of the repository to their remote repository on Github. This can be done with the following command (note that the URL may need to be updated to match the current version of the repository):
```
git remote add upstream `link to your remote repository`
```


# Setup
The following steps follow along with the exercises presented in the presentation slides:

1. Build the required Python environment:
    -  Open and review the environment specification file named `owf_env.yml`. The file is located in the `env` directory in the root directory of the branch repository. This file contains a list of all the packages and their versions that are required to run the model. The environment is built using the `conda` package manager, which is included with Anaconda or Miniconda installations. If you do not have Anaconda or Miniconda installed, please refer to the following link: [Anaconda installation](https://docs.anaconda.com/anaconda/install/index.html) or [Miniconda installation](https://docs.conda.io/en/latest/miniconda.html).
    -  Run the following command from the command line to build the environment from the YML file (note this may take 5-10 minutes to complete depending on your internet connection):
    ```
    conda env create --file owf_env.yml
    ```

2. Activate the environment:
    -  Run the following command from the command line to activate the environment:
    ```
    conda activate owf_env
    ```
    After running this command, the command line prompt should change to indicate that the `owf_env` environment is active. For example, the prompt may change from `(base)` to `(owf_env)`.

3. Run the following sequence of commands to verify that the environment and model files are properly functioning on your system:

    ```
    conda activate owf_env
    cd scripts
    python WaterTown_Model.py
    ```
    Expected output on the command line is the printed line: "Water Town script run was successful."
