#!/usr/bin/env python3

# Safely run automated Terraform commands and capture stdout
# Additionally, you can set TF logging ENV VARs:
# TF_LOG_PATH = desired log path
# TF_LOG = TRACE, DEBUG, INFO, WARN or ERRO

import subprocess
import shutil

tf_cmd = shutil.which("terraform")
tf_options = ['init', 'plan', 'apply']

def run_command(cmd):
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = pipe.stdout.readline()
        stdout.append(line)
        print line,
        if line == '' and pipe.poll() != None:
            break
    return ''.join(stdout)

# TODO: add terraform command options: init, plan, apply
run_command(tf_cmd)
