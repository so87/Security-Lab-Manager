# docker-compose scale web=2 worker=3
import docker
import subprocess
client = docker.DockerClient(base_url='unix://var/run/docker.sock')
server_criteria = {"name": "standlone-django",}

def update_ram_and_cpu(num_ram, num_cpu):
    print("Updating ram and cpu")
    num_cpu = num_cpu -1 # cpu start at zero
    containers = client.containers.list(filters=server_criteria,)
    for container in containers:
        try:
            container.update(mem_limit=str(num_ram)+"m",memswap_limit=str(num_ram)+"m",cpuset_cpus="0-"+str(num_cpu))
        except:
            return 1
    return 0

def update_instances(num_instances):
    print("Updating instances")
    command = "docker-compose up --scale nginx-django="+str(num_instances)+"web-django="+str(num_instances)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    process.communicate()