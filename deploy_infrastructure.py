#!/usr/bin/env python3

# Safely run automated Terraform commands and capture stdout,stderr
# Additionally, set TF logging ENV VARs:
# TF_LOG_PATH = desired log path
# TF_LOG = TRACE, DEBUG, INFO, WARN or ERRO

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

# TF init
tf_init = tf_cmd + "init -input=false"
run_command(tf_init)

# TF plan
tf_plan = tf_cmd + "plan -out=tfplan -input=false"
run_command(tf_plan)

# TF apply
tf_apply = tf_cmd + "apply -input=false tfplan"
run_command(tf_apply)
