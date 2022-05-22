# Week 1 (E): Set up a Python development environment

Your first home task is to install a Python development environment on your computer. Depending on the OS that you are using (macOS, Linux/Unix, Windows, etc.), the are different options to do it. Therefore, I ask you to look up instructions for your system on your own or choose your system in the installation instructions provided below. This task is not marked but if you encounter some problems you can describe them in your submission and get help or feedback from the correctors.

You will need to set up the following components:

* A **Python distribution** including a Python interpreter and the libraries discussed in the exercise class ([numpy](https://numpy.org/install/), [pandas](https://pandas.pydata.org/docs/getting_started/install.html), [matplotlib](https://pypi.org/project/matplotlib/)). You can find instructions how to install Python on all the common systems in this [guide](https://realpython.com/installing-python/#how-to-install-on-debian-linux). Different options to install libraries are explained under the links to these libraries given above. Typically, you would install a Python package installer called **pip** together with your Python distribution. Afterwards, you can install packages in command line as follows:
```pip install package_name```

* A text **editor**, which you will use for reading, writing and editing your Python scripts. One light option is [Sublime Text](https://www.sublimetext.com) but you can look up any other editor. 

* *Instead of a simple text editor, you can also opt for an integrated development environment such as [PyCharm](https://www.jetbrains.com/de-de/pycharm/), [VS Code](https://code.visualstudio.com/), etc. that allows to edit, run, debug Python scripts, inspect the console, features code completion and linting, helps to organize projects, employ version control, etc. without having to leave the application. While these environments allow more functionality, they are also heavier and more difficult to use.

* [**Jupyter Notebook**](https://jupyter.org), which is a web-based interactive development environment for Python.


## Recommended option

**Anaconda** by Continuum Analytics is a Python distribution that, among other things, includes the essential data science Python packages. Numpy, pandas, matplotlib and many other libraries are already included in Anaconda by default and you do not need to install them separately. 

* [Download page](https://www.anaconda.com/distribution/)
* [Install instructions](https://docs.anaconda.com/anaconda/install/)
* [Quick start guide](https://docs.anaconda.com/anaconda/user-guide/getting-started/)
  
After a successful install, further Python packages can be installed using the console command:
```conda install package_name```