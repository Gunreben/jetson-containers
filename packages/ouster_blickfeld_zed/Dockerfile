# Base image compatible with NVIDIA Jetson (ARM architecture)
#---
# name: ros2_humble_all_sensors
# group: sensors
# depends: []
#---

ARG BASE_IMAGE
FROM ${BASE_IMAGE}


ARG L4T_MAJOR_VERSION
ARG L4T_MINOR_VERSION
ARG L4T_PATCH_VERSION
ARG ZED_SDK_MAJOR=4
ARG ZED_SDK_MINOR=0


# Set environment variables for ZED SDK and ROS
ENV BLICKFELD_IP=192.168.26.26
ENV OUSTER_OS0_IP=192.168.26.85
ENV JETSON_IP=192.168.26.4
ENV ROS_PACKAGE=ros_base
ENV ROS_VERSION=humble
ENV ROS_DISTRO=${ROS_VERSION}
ENV ROS_ROOT=/opt/ros/${ROS_DISTRO}
ENV ROS_WS=ros_ws
ENV ROS_PYTHON_VERSION=3
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV PYTHONIOENCODING=utf-8
ENV LOGNAME root

WORKDIR /tmp

RUN apt-get update -y || true ; apt-get install --no-install-recommends ros

RUN apt-get update -y || true ; apt-get install --no-install-recommends lsb-release wget less zstd udev sudo apt-transport-https -y && \
    echo "# R${L4T_MAJOR_VERSION} (release), REVISION: ${L4T_MINOR_VERSION}.${L4T_PATCH_VERSION}" > /etc/nv_tegra_release ; \
    wget -q --no-check-certificate -O ZED_SDK_Linux.run https ://download.stereolabs.com/zedsdk/${ZED_SDK_MAJOR}.${ZED_SDK_MINOR}/l4t${L4T_MAJOR_VERSION}.${L4T_MINOR_VERSION}/jetsons && \
    chmod +x ZED_SDK_Linux.run ; ./ZED_SDK_Linux.run silent skip_drivers && \
    rm -rf /usr/local/zed/resources/* \
    rm -rf ZED_SDK_Linux.run && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# ZED Python API
RUN apt-get update -y || true ; apt-get install --no-install-recommends python3 python3-pip python3-dev python3-setuptools build-essential -y && \ 
    wget download.stereolabs.com/zedsdk/pyzed -O /usr/local/zed/get_python_api.py && \
    python3 /usr/local/zed/get_python_api.py && \
    python3 -m pip install cython wheel && \
    python3 -m pip install numpy pyopengl *.whl && \
    #apt-get remove --purge build-essential -y && apt-get autoremove -y && \
    rm *.whl ; rm -rf /var/lib/apt/lists/* && apt-get clean

### TODO: ZED ROS Dependencies   
  
# Symbolic link for ZED streaming features
RUN ln -sf /usr/lib/aarch64-linux-gnu/tegra/libv4l2.so.0 /usr/lib/aarch64-linux-gnu/libv4l2.so

# Build ROS2 from source --> should be done via seperate command
#COPY ros2_build.sh ros2_build.sh
#RUN ./ros2_build.sh
# PARSE THE CONTENTS OF THE SHELL SCRIPT FOR DEBUGGING REASONS
#
# Set the default DDS middleware to cyclonedds
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Copy and set entrypoint
COPY ros_entrypoint.sh /ros_entrypoint.sh
RUN chmod +x /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["/bin/bash"]

# Install necessary packages and clone custom ROS packages
RUN mkdir -p /ros_ws/src && cd /ros_ws/src \
    && git clone https://github.com/Blickfeld/blickfeld_qb2_ros2_driver.git \
    && git clone https://github.com/ros-drivers/ros2_ouster_drivers \
    && cd /ros_ws && . /opt/ros/humble/setup.sh \
    && colcon build --symlink-install --cmake-clean-first \
    && sed -i 's/lidar_ip: 10.5.5.96/lidar_ip: '"$OUSTER_OS0_IP"'/' /ros_ws/src/ros2_ouster_drivers/ros2_ouster/params/driver_config.yaml \
    && sed -i 's/computer_ip: 10.5.5.1/computer_ip: '"$JETSON_IP"'/' /ros_ws/src/ros2_ouster_drivers/ros2_ouster/params/driver_config.yaml \
    && rm -rf /var/lib/apt/lists/*



WORKDIR /

