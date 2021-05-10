# Say-What

[![CodeFactor](https://www.codefactor.io/repository/github/appdevelopmentandsuch/say-what/badge)](https://www.codefactor.io/repository/github/appdevelopmentandsuch/say-what)

Rapidly create JSON Serializable classes for Unity using sample JSON

![say-what-demo](https://user-images.githubusercontent.com/22528729/88982483-00460800-d28e-11ea-9ad6-e218c1ada6e5.gif)

# Quick Start

1. Clone the repo

2. Create a json file with the title of your JSON response, i.e. `VerifyToken.json`

3. In a terminal, run `python3 createjsonclass.py -f <path-to-file>/VerifyToken.json`

## Required Args

- `-f / --File`: Provide path to the file you wish to convert

## Optional Args

- `-p / --Path`: Provide output path of the file. Default: "./"

# Dependencies

- Python 3.8.2

NOTE: This code is untest on other version of python
