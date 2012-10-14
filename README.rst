COG-ABM tutorial
================

Git
---
COG-ABM is using Git for its version control.
See http://git-scm.com/video/what-is-version-control to get some grasp on version control.

  http://upload.wikimedia.org/wikipedia/commons/4/44/Git_data_flow_simplified.svg


Tutorials
~~~~~~~~~

- http://git-scm.com/book
- http://git-scm.com/videos


Important topics
~~~~~~~~~~~~~~~~

git commands:

- init
- clone
- add
- commit (-a, -m)
- push
- pull
- stash
- merege
- rebase
- mv
- rm


Some setup
~~~~~~~~~~

::

    git config --global user.name "Your Name Comes Here"
    git config --global user.email you@yourdomain.example.com

    git config --global color.diff auto
    git config --global color.status auto
    git config --global color.branch auto


Other topics
~~~~~~~~~~~~

- Useful app - gitg
- SSH Keys - https://help.github.com/categories/56/articles
- Github comments


Python
------

- PEP8


Obtaining COG-ABM
-----------------
You can make fork from official version (from Github site) and than clone or just clone the repo locally.

Clone repository

::

    git clone git@github.com:CogSys/cog-abm.git COG-ABM


Making virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~
This step is optional but recommended.

::

    virtualenv --no-site-packages .env
    . .env/bin/activate
    deactivate


Useful packages
~~~~~~~~~~~~~~~

::

   pip install ipython ipdb


Running simulation
------------------

Go to **src/steels** directory and run

::

    python steels_main.py -p simulation_GG.xml -f simulation_results

It should take less than 1 minute to finish.
If you can't remember the command :) just type:

::

    python steels_main.py --help

Many programs in COG-ABM have this option

::

    python analyzer.py -f simulation_results it DSA
    python analyzer.py -f simulation_results it DS
    python analyzer.py -f simulation_results -c it DS
    python analyzer.py -f simulation_results it DS min_DSA max_DSA -c --xlabel="Iteration" --ylabel="DS"

