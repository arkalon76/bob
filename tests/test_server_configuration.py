"""
Here we test all functions that has to do with the configuration of the server
"""

from bobserver import BOBServer
from configparser import ConfigParser
import os, shutil

"""
Test that we can load a pre-existing config file
"""
def test_config_exist():
    # Setup the test by removing any existing config file and replace with
    # sample config file
    if os.path.isfile(BOBServer.config_filename) == True:
        os.remove(BOBServer.config_filename)
        shutil.copy('tests/sample-data/sample-init-bobsrv-config.ini', BOBServer.config_filename)
    else:
        shutil.copy('tests/sample-data/sample-init-bobsrv-config.ini', BOBServer.config_filename)
    # Load the file and make sure it loads well
    config = BOBServer.load_config_file()
    assert isinstance(config, ConfigParser)

"""
Let's check that if we try to load the config file without it existing, a basic
one should be created
"""
def test_missing_config():
    #Let's make sure the config file is gone
    if os.path.exists(BOBServer.config_filename) == True:
        os.remove(BOBServer.config_filename)
        # Let's make sure the file is gone
        if os.path.exists(BOBServer.config_filename) == True:
            raise FileExistsError("[Test setup] File exist but should be removed!")

    config = BOBServer.load_config_file()
    assert isinstance(config, ConfigParser)

"""
Ok, so now we will see if we can get some data out of the configuration.
Let's check for the port number and host since that HAVE to be there
"""
def test_basic_info():
    config = BOBServer.load_config_file()
    assert config['Server']['port'] == '7766'
    assert config['Server']['host'] == 'localhost'
