# Testing Hugging Face Models

This a repository for educational purposes, focused on testing models on Hugging Face.

## Requirements

- Python 3.11

You can download the requirements by running the following Makefile command:

```bash
$ make requirements

******************** INSTALLING SOFTWARE REQUIREMENTS **********************************
if [ -x /usr/bin/apt-get ]; then  xargs -a requirements.txt sudo apt-get install -y; fi
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3 is already the newest version (3.10.6-1~22.04.1).
0 to upgrade, 0 to newly install, 0 to remove and 29 not to upgrade.
```

## How to run?

First, you need to connect with Hugging Face API using the following command:

```bash
$ huggingface-cli login

    _|    _|  _|    _|    _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|_|_|_|    _|_|      _|_|_|  _|_|_|_|
    _|    _|  _|    _|  _|        _|          _|    _|_|    _|  _|            _|        _|    _|  _|        _|
    _|_|_|_|  _|    _|  _|  _|_|  _|  _|_|    _|    _|  _|  _|  _|  _|_|      _|_|_|    _|_|_|_|  _|        _|_|_|
    _|    _|  _|    _|  _|    _|  _|    _|    _|    _|    _|_|  _|    _|      _|        _|    _|  _|        _|
    _|    _|    _|_|      _|_|_|    _|_|_|  _|_|_|  _|      _|    _|_|_|      _|        _|    _|    _|_|_|  _|_|_|_|

    A token is already saved on your machine. Run `huggingface-cli whoami` to get more information or `huggingface-cli logout` if you want to log out.
    Setting a new token will erase the existing one.
    To log in, `huggingface_hub` requires a token generated from https://huggingface.co/settings/tokens .
Enter your token (input will not be visible): 
Add token as git credential? (Y/n) Y
Token is valid (permission: read).
The token `huggingface-tests` has been saved to ~/.cache/huggingface/stored_tokens
Cannot authenticate through git-credential as no helper is defined on your machine.
You might have to re-authenticate when pushing to the Hugging Face Hub.
Run the following command in your terminal in case you want to set the 'store' credential helper as default.

git config --global credential.helper store

Read https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage for more details.
Token has not been saved to git credential helper.
Your token has been saved to ~/.cache/huggingface/token
Login successful
```

after this, you may try to run the application by running the following Makefile command:

```bash
$ make

******************** DOWNLOADING (IF NECESSARY) AND RUNNING MODEL **********************************

python ./src/huggingface_tests/main.py
Device set to use cpu
[{'summary_text': 'NAIST tackles problems at the frontiers of science in an environment of interdisciplinary and international cooperation. Students and researchers have access to world-class facilities in a stimulating environment.'}]
```

This is will download the model from Hugging Face and running the Python script. After this, you may remove the model by using the following commands:

```bash
$ huggingface-cli scan-cache
REPO ID                 REPO TYPE SIZE ON DISK NB FILES LAST_ACCESSED  LAST_MODIFIED REFS LOCAL PATH                                                           
----------------------- --------- ------------ -------- -------------- ------------- ---- -------------------------------------------------------------------- 
facebook/bart-large-cnn model             1.6G        6 15 minutes ago 1 hour ago    main ~/.cache/huggingface/hub/models--facebook--bart-large-cnn 

Done in 0.0s. Scanned 1 repo(s) for a total of 1.6G.

$ huggingface-cli delete-cache --models facebook/bart-large-cnn
```
