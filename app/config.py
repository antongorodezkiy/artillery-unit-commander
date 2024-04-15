import configparser
from dotenv import dotenv_values

# we will parse enviromnet file and throw it in the configparser.
# well, it's kind of overhead but it's just for learning, right? :)
env = dotenv_values(".env")
config = configparser.ConfigParser()
config.read_dict({ "env": env })
