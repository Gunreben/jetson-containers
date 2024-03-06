#---
# name: arkvision
# group: sensors
# depends: [ros:humble-desktop]
#---

ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG L4T_MAJOR_VERSION
ARG L4T_MINOR_VERSION
ARG L4T_PATCH_VERSION

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
    cmake \
    build-essential \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Install gstreamer for rtsp support
RUN apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

# Clone the OpenCV Python repo, build, and install
RUN cd /etc/ \
    && git clone --recursive https://github.com/skvark/opencv-python.git \
    && cd opencv-python \
    && export CMAKE_ARGS="-DWITH_GSTREAMER=ON" \
    && pip install --upgrade pip wheel \
    && pip wheel . --verbose \
    && pip install /etc/opencv-python/dist/opencv_python*.whl

#Clone Ouster ROS2 packet
RUN mkdir -p /ros_ws/src && cd /ros_ws/src \
    && git clone https://github.com/Gunreben/arkvision_six_cameras.git
    

RUN apt-get update && apt-get install -y \
    libgrpc++-dev \
    protobuf-compiler-grpc \
    libtins-dev \ 
    libprotobuf-dev \
    && . ${ROS_ROOT}/install/setup.bash \
    && rm -rf /var/lib/apt/lists/* \
    && cd /ros_ws/ \
    && colcon build --symlink-install --cmake-clean-first


# commands will be appended/run by the entrypoint which sources the ROS environment
COPY ros_entrypoint.sh /ros_entrypoint.sh

RUN chmod +x /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["/bin/bash"]


WORKDIR /
