#---
# name: lidars
# group: sensors
# depends: [ros:humble-desktop]
#---

ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG L4T_MAJOR_VERSION
ARG L4T_MINOR_VERSION
ARG L4T_PATCH_VERSION

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    ros-humble-desktop=0.10.0-1* \
#    && rm -r /var/lib/apt/lists/*

# Setzen der Umgebungsvariablen
ENV BLICKFELD_IP=192.168.26.26
ENV OUSTER_OS0_IP=192.168.26.85
ENV JETSON_IP=192.168.26.4

ARG ROS_PACKAGE=ros_base
ARG ROS_VERSION=humble

ENV ROS_DISTRO=${ROS_VERSION}
ENV ROS_ROOT=/opt/ros/${ROS_DISTRO}
ENV ROS_WS=ros_ws
ENV ROS_PYTHON_VERSION=3
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /tmp

###Should all be already done in ros dockerfile
# change the locale from POSIX to UTF-8
RUN apt-get update && \
    apt-get install -y --no-install-recommends locales \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

#RUN locale-gen en_US en_US.UTF-8 && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV PYTHONIOENCODING=utf-8


# set Python3 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Set the default DDS middleware to cyclonedds
# https://github.com/ros2/rclcpp/issues/1335
ENV RMW_IMPLEMENTATION=rmw_fastrtps_cpp

# Installiere notwendige Pakete
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Klonen des Blickfeld-ROS-Pakets
RUN mkdir -p /ros_ws/src \
    && cd /ros_ws/src \
    && git clone https://github.com/Blickfeld/blickfeld_qb2_ros2_driver.git

# Installieren der benötigten Pakete
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-diagnostic-updater \
    libgrpc++-dev \
    protobuf-compiler-grpc \
    libtins-dev \ 
    libprotobuf-dev \
    && . /opt/ros/${ROS_DISTRO}/setup.sh \
    && rm -rf /var/lib/apt/lists/* \
    && colcon build --symlink-install --cmake-clean-first

RUN sed -i 's/"fqdn": "qb2"/"fqdn": "'"$BLICKFELD_IP"'"/' /ros_ws/src/blickfeld_qb2_ros2_driver/scripts/blickfeld_qb2_ros2_driver.py

#Clone Ouster ROS2 packet
RUN cd /ros_ws/src \
    && git clone https://github.com/ros-drivers/ros2_ouster_drivers 
    
# Installieren der benötigten Pakete
RUN . /opt/ros/${ROS_DISTRO}/setup.sh \
    && rm -rf /var/lib/apt/lists/* \
    && colcon build --symlink-install --cmake-clean-first

RUN . /opt/ros/${ROS_DISTRO}/setup.sh \
    && sed -i 's/lidar_ip: 10.5.5.96/lidar_ip: '"$OUSTER_OS0_IP"'/' /ros_ws/src/ros2_ouster_drivers/ros2_ouster/params/driver_config.yaml
RUN . /opt/ros/${ROS_DISTRO}/setup.sh \
    && sed -i 's/computer_ip: 10.5.5.1/computer_ip: '"$JETSON_IP"'/' /ros_ws/src/ros2_ouster_drivers/ros2_ouster/params/driver_config.yaml

# commands will be appended/run by the entrypoint which sources the ROS environment
COPY ros_entrypoint.sh /ros_entrypoint.sh

RUN chmod +x /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["/bin/bash"]


WORKDIR /
