# python-fire-cli-skeleton

It is a skeleton for easily making original commands.<br>
It uses [Python Fire](https://github.com/google/python-fire).

## Please try how it work

### pip install from github repository.

```sh
$ pip install git+ssh://git@github.com/nkmr-jp/python-fire-cli-skeleton.git
$ sample_command
  Type:        SampleCommand
  String form: <sample_command.SampleCommand object at 0x103f1bb38>
  File:        path/to/nkmr-jp/python-fire-cli-skeleton/sample_command.py
  Docstring:   this is sample
  
  Usage:       sample_command
               sample_command hello
```

`git+ssh` can use private repository too.


### pip install from local repository
```sh
$ git clone git+ssh://git@github.com/nkmr-jp/python-command-skeleton.git
$ cd path/to/nkmr-jp/python-fire-cli-skeleton/
$ pipenv run python setup.py install
$ pip install -e path/to/nkmr-jp/python-fire-cli-skeleton/
$ sample_command hello
Hello world!
```

## How to Use
copy this repository and make your original command.<br>
If you want to know how to make a package in detail [please refer to here](https://packaging.python.org/tutorials/packaging-projects/).
