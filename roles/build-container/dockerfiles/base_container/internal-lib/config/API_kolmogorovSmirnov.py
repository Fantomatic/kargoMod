'''
Created on May 2015
Update on May 2017

Use this code to install config


@author: capgemini.cloudinfrastructurefrance.ac4dc
@copyright: capgemini 2015,2016,2017
'''
import yaml
from config.YAML_config import settings

path=settings["etc"]["path"]
with open(path+"kolmogorovSmirnov.yaml", "r") as f:
    kstsettings = yaml.load(f)
