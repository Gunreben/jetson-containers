#---
# name: zed_ros
# group: sensors
# depends: [ros:humble-desktop, zed]
#---

ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG L4T_MAJOR_VERSION
ARG L4T_MINOR_VERSION
ARG L4T_PATCH_VERSION

# Setzen der Umgebungsvariablen
ENV BLICKFELD_IP=192.168.26.26

ARG ROS_VERSION=humble

ENV ROS_DISTRO=${ROS_VERSION}
ENV ROS_ROOT=/opt/ros/${ROS_DISTRO}
ENV ROS_WS=ros_ws
ENV ROS_PYTHON_VERSION=3
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /tmp

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*


# Klonen des ZED-ROS-Pakets
RUN mkdir -p /ros_ws/src \
    && cd /ros_ws/src \
    && git clone  --recursive https://github.com/stereolabs/zed-ros2-wrapper.git

# Change working directory
WORKDIR /ros_ws/

RUN apt-get update && apt-get install -y \
    python3-rosdep \
    python3-rosinstall-generator \
    python3-vcstool \
    python3-rosinstall \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
    
# Installieren der benötigten Pakete
RUN . ${ROS_ROOT}/install/setup.bash \
    && apt-get update\
    && cd /ros_ws/ \
    && rosdep install --from-paths src --ignore-src -r -y

# CHECK THE SECOND SOURCE COMMAND; FEELS OFF;
RUN . ${ROS_ROOT}/install/setup.bash \
    && . /opt/ros/humble/setup.sh \ 
    && rm -rf /var/lib/apt/lists/* \
    && cd /ros_ws/ \
    && colcon build --symlink-install --cmake-args=-DCMAKE_BUILD_TYPE=Release

# commands will be appended/run by the entrypoint which sources the ROS environment
COPY ros_entrypoint.sh /ros_entrypoint.sh

RUN chmod +x /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["/bin/bash"]


WORKDIR /
