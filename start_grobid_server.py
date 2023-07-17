# this piece of code initializes the grobid server

import os
import subprocess
import socket


grobid_directory = "./grobid-0.7.3"
port = 8070  # the default grobid port

# change to grobid directory
os.chdir(grobid_directory)


# check if the port is already in use
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def kill_application_using_port(port):
    cmd = f"lsof -t -i:{port} | xargs kill"
    subprocess.run(cmd, shell=True)


# Check if the port is in use
if is_port_in_use(port):
    # Kill the application using the port
    kill_application_using_port(port)
    print(f"Application using port {port} has been killed.")
else:
    print(f"No application found using port {port}.")


# run initialize the grobid server
p = subprocess.Popen(["./gradlew", "run"])

# we never want to kill this server
