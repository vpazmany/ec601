# ec601
Mission Statement: 

As a small coffee shop, we need to determine what coffee consumers are enjoying in the area to determine which products must be on our menu.

User Stories: 

I, the coffee shop, want immediate feedback based on handle and hashtag inputs to gage audience sentiment feedback about specific drinks to determine what to put on my own menu.

I, the coffee shop, want a percentage of the positive vs. negative sentiment in the text of the hashtag/handle searched to assess the reviews and fully understand the public’s sentiment.

I, the coffee shop, need to quickly filter and search tweets from specific popular coffee shops in the area.

Install virtualenv globally.

MACOSWINDOWSLINUX
Use pip2 install --upgrade virtualenv or pip3 install --upgrade virtualenv.
After you install virtualenv, you can create a virtual environment in your project. virtualenv creates a virtual copy of the entire Python installation in the env folder.

MACOSWINDOWSLINUX
Use the --python flag to tell virtualenv which Python version to use:

cd your-project
virtualenv --python python3 env
After the copy is created, set your shell to use the virtualenv paths for Python by activating the virtual environment as follows.

MACOSWINDOWSLINUX
source env/bin/activate
Now you can install packages without affecting other projects or your global Python installation:

pip install google-cloud-storage
If you want to stop using the virtual environment and go back to your global Python, you can deactivate it:

deactivate

virtual install/run : https://cloud.google.com/python/setup

############################################################
Authentication environemnt:
https://cloud.google.com/natural-language/docs/reference/libraries#installing_the_client_library

export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
For example:

export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"

execute "python sentiapi.py" to test program.
