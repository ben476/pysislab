import os
import subprocess

def test_run():
    exit_status = os.system('pysislab --help')
    assert exit_status == 0

def test_list():
    exit_status = os.system('pysislab --list')
    assert exit_status == 0

def test_list_csv():
    exit_status = os.system('pysislab --list --csv')
    assert exit_status == 0