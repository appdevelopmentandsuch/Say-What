# Say-What

[![CodeFactor](https://www.codefactor.io/repository/github/appdevelopmentandsuch/say-what/badge)](https://www.codefactor.io/repository/github/appdevelopmentandsuch/say-what)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/appdevelopmentandsuch/Say-What/graphs/commit-activity)
[![GitHub license](https://img.shields.io/github/license/appdevelopmentandsuch/Say-What.svg)](https://github.com/appdevelopmentandsuch/Say-What/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/appdevelopmentandsuch/Say-What.svg)](https://GitHub.com/appdevelopmentandsuch/Say-What/releases/)
[![GitHub tag](https://img.shields.io/github/tag/appdevelopmentandsuch/Say-What.svg)](https://GitHub.com/appdevelopmentandsuch/Say-What/tags/)
[![Github all releases](https://img.shields.io/github/downloads/appdevelopmentandsuch/Say-What/total.svg)](https://GitHub.com/appdevelopmentandsuch/Say-What/releases/)
[![GitHub stars](https://img.shields.io/github/stars/appdevelopmentandsuch/Say-What.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/appdevelopmentandsuch/Say-What/stargazers/)
[![GitHub issues](https://img.shields.io/github/issues/appdevelopmentandsuch/Say-What.svg)](https://GitHub.com/appdevelopmentandsuch/Say-What/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/appdevelopmentandsuch/Say-What.svg)](https://GitHub.com/appdevelopmentandsuch/Say-What/issues?q=is%3Aissue+is%3Aclosed)

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
