#!/usr/bin/env python3

# Run Terraform commands and capture stdout

import subprocess
import shutil

tf_cmd = shutil.which("terraform")

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

run_command(tf_cmd)
