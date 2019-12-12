FROM gitpod/workspace-full

USER gitpod

RUN sudo apt install pip3 -y \
    sudo pip3 install pil -y \
    sudo add-apt-repository ppa:openscad/releases -y \
    sudo apt-get update -y \
    sudo apt-get upgrade -y \
    sudo apt-get install openscad -y

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN sudo apt-get -q update && \
#     sudo apt-get install -yq bastet && \
#     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
