import docker
import time
import subprocess
from slmApp.exercises import port_allocator, generate_hash

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

# check to see if the container is already running
def container_running(student_name, exercise_name):
    status = {"status": "running",
              "name": exercise_name+student_name,}
    containers = client.containers.list(filters=status,)
    if containers:
        return 1
    else:
        return 0

def run_container(student_name, exercise_name):
    if container_running(student_name, exercise_name):
        print("Container already running")
        return 1
    print("Starting container... ")
    # find open port
    port = port_allocator.open()

    # generate hash and pass it to container


    # start up container
    args = exercise_name+" "+student_name+" "+str(port)+" up"
    command = "cd slmApp/exercises/run_configs/ && ./run.sh "+args
    print("Running: "+ command)
    subprocess.call(command, shell=True)
    time.sleep(5)

    status = container_running(student_name, exercise_name)
    if status:
        # pass back port it is running on so user knows where to navigate
        return port
    else:
        return 1

def stop_container(student_name, exercise_name):
    if not container_running(student_name, exercise_name):
        print("Container not running")
        return 1
    print("stopping container... ")
    status = {"name": exercise_name+student_name,}
    containers = client.containers.list(filters=status,)

    # stop container
    for container in containers:
        container.stop()
    time.sleep(5)

    return container_running(student_name, exercise_name)

# ensure container is erased and remade
def restart_container(student_name, exercise_name):
    stop_container(student_name, exercise_name)
    # remove the stopped container
    status = {"name": exercise_name+student_name,}
    containers = client.containers.list(filters=status,)
    for container in containers:
        container.remove()

    status =  run_container(student_name, exercise_name)
    return status