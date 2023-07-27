# ros

Various ROS/ROS2 containers for JetPack.  These build ROS from source to run them on the needed versions of Ubuntu.

Supported ROS distros:   `melodic` `noetic` `foxy` `galactic` `humble` `iron`
</br>
Supported ROS packages:  `ros_base` `ros_core` `desktop`

<details open>
<summary><b>CONTAINERS</b></summary>
</br>

| **`ros:melodic-ros-base`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T <34` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros.melodic`](Dockerfile.ros.melodic) |
| &nbsp;&nbsp;&nbsp;Notes | ROS Melodic is for JetPack 4 only |

| **`ros:melodic-ros-core`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T <34` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros.melodic`](Dockerfile.ros.melodic) |
| &nbsp;&nbsp;&nbsp;Notes | ROS Melodic is for JetPack 4 only |

| **`ros:melodic-desktop`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T <34` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros.melodic`](Dockerfile.ros.melodic) |
| &nbsp;&nbsp;&nbsp;Notes | ROS Melodic is for JetPack 4 only |

| **`ros:noetic-ros-base`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros.noetic`](Dockerfile.ros.noetic) |

| **`ros:noetic-ros-core`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros.noetic`](Dockerfile.ros.noetic) |

| **`ros:noetic-desktop`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros.noetic`](Dockerfile.ros.noetic) |

| **`ros:foxy-ros-base`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:foxy-ros-core`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:foxy-desktop`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:galactic-ros-base`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:galactic-ros-core`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:galactic-desktop`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:humble-ros-base`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:humble-ros-core`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:humble-desktop`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:iron-ros-base`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:iron-ros-core`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

| **`ros:iron-desktop`** | |
| :-- | :-- |
| &nbsp;&nbsp;&nbsp;Requires | `L4T >=32.6` |
| &nbsp;&nbsp;&nbsp;Dependencies | [`build-essential`](/packages/build-essential) [`python`](/packages/python) [`cmake`](/packages/cmake/cmake_pip) [`numpy`](/packages/numpy) [`opencv`](/packages/opencv) |
| &nbsp;&nbsp;&nbsp;Dockerfile | [`Dockerfile.ros2`](Dockerfile.ros2) |

</details>

<details open>
<summary><b>CONTAINER IMAGES</b></summary>
</br>

| Tag | Date | Arch | Size |
| :-- | :--: | :--: | :--: |
| [`dustynv/ros:eloquent-ros-base-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(0.8GB)` |
| [`dustynv/ros:eloquent-ros-base-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(0.8GB)` |
| [`dustynv/ros:eloquent-ros-base-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(0.8GB)` |
| [`dustynv/ros:eloquent-ros-base-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(0.8GB)` |
| [`dustynv/ros:foxy-desktop-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(6.5GB)` |
| [`dustynv/ros:foxy-desktop-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(6.4GB)` |
| [`dustynv/ros:foxy-desktop-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(6.0GB)` |
| [`dustynv/ros:foxy-desktop-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(6.0GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(1.6GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(1.6GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(1.6GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(1.7GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r34.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-04-18` | `(6.4GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(6.4GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(6.6GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(6.5GB)` |
| [`dustynv/ros:foxy-pytorch-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(6.1GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(1.1GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(1.1GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(1.1GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(0.9GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r34.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-04-18` | `(5.9GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(5.9GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(5.9GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(5.4GB)` |
| [`dustynv/ros:foxy-ros-base-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.4GB)` |
| [`dustynv/ros:foxy-slam-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(2.3GB)` |
| [`dustynv/ros:foxy-slam-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(2.3GB)` |
| [`dustynv/ros:foxy-slam-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(2.3GB)` |
| [`dustynv/ros:galactic-desktop-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(6.2GB)` |
| [`dustynv/ros:galactic-desktop-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(6.1GB)` |
| [`dustynv/ros:galactic-desktop-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(5.7GB)` |
| [`dustynv/ros:galactic-desktop-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.7GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(1.3GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(1.3GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(1.3GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(1.4GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r34.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-04-18` | `(6.1GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(6.1GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(6.3GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(6.2GB)` |
| [`dustynv/ros:galactic-pytorch-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.8GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(0.8GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(0.8GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(0.8GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(0.6GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r34.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-04-18` | `(5.6GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(5.6GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(5.6GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(5.1GB)` |
| [`dustynv/ros:galactic-ros-base-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.1GB)` |
| [`dustynv/ros:humble-desktop-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(1.0GB)` |
| [`dustynv/ros:humble-desktop-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(6.2GB)` |
| [`dustynv/ros:humble-desktop-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(6.2GB)` |
| [`dustynv/ros:humble-desktop-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(5.7GB)` |
| [`dustynv/ros:humble-desktop-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.7GB)` |
| [`dustynv/ros:humble-pytorch-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(1.4GB)` |
| [`dustynv/ros:humble-pytorch-l4t-r34.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-05-26` | `(6.1GB)` |
| [`dustynv/ros:humble-pytorch-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(6.1GB)` |
| [`dustynv/ros:humble-pytorch-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(6.3GB)` |
| [`dustynv/ros:humble-pytorch-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(6.2GB)` |
| [`dustynv/ros:humble-pytorch-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.8GB)` |
| [`dustynv/ros:humble-ros-base-deepstream-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-10-03` | `(5.5GB)` |
| [`dustynv/ros:humble-ros-base-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(0.6GB)` |
| [`dustynv/ros:humble-ros-base-l4t-r34.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-05-26` | `(5.6GB)` |
| [`dustynv/ros:humble-ros-base-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(5.6GB)` |
| [`dustynv/ros:humble-ros-base-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(5.6GB)` |
| [`dustynv/ros:humble-ros-base-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(5.1GB)` |
| [`dustynv/ros:humble-ros-base-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.2GB)` |
| [`dustynv/ros:iron-desktop-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-26` | `(1.0GB)` |
| [`dustynv/ros:iron-desktop-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-26` | `(6.2GB)` |
| [`dustynv/ros:iron-desktop-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-25` | `(5.8GB)` |
| [`dustynv/ros:iron-desktop-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-25` | `(5.8GB)` |
| [`dustynv/ros:iron-pytorch-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-26` | `(1.4GB)` |
| [`dustynv/ros:iron-pytorch-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-26` | `(6.3GB)` |
| [`dustynv/ros:iron-pytorch-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-25` | `(6.2GB)` |
| [`dustynv/ros:iron-pytorch-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-25` | `(5.8GB)` |
| [`dustynv/ros:iron-ros-base-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-26` | `(0.7GB)` |
| [`dustynv/ros:iron-ros-base-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-26` | `(5.6GB)` |
| [`dustynv/ros:iron-ros-base-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-25` | `(5.2GB)` |
| [`dustynv/ros:iron-ros-base-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-25` | `(5.2GB)` |
| [`dustynv/ros:melodic-ros-base-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(0.5GB)` |
| [`dustynv/ros:melodic-ros-base-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(0.5GB)` |
| [`dustynv/ros:melodic-ros-base-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(0.5GB)` |
| [`dustynv/ros:melodic-ros-base-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(0.5GB)` |
| [`dustynv/ros:noetic-desktop-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(5.5GB)` |
| [`dustynv/ros:noetic-desktop-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.6GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(1.1GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(1.1GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(1.0GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(1.3GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r34.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-04-18` | `(6.1GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(6.0GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(6.3GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(6.1GB)` |
| [`dustynv/ros:noetic-pytorch-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.8GB)` |
| [`dustynv/ros:noetic-ros-base-deepstream-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-10-03` | `(4.3GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r32.4.4`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-08-06` | `(0.5GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r32.5.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2021-09-23` | `(0.5GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r32.6.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-03-02` | `(0.5GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r32.7.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-19` | `(0.6GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r34.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-04-18` | `(5.6GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r34.1.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2022-09-23` | `(5.6GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r35.1.0`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-04-29` | `(5.6GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r35.2.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-03-28` | `(5.1GB)` |
| [`dustynv/ros:noetic-ros-base-l4t-r35.3.1`](https://hub.docker.com/r/dustynv/ros/tags) | `arm64` | `2023-05-02` | `(5.1GB)` |
</details>

<details open>
<summary><b>RUN CONTAINER</b></summary>
</br>

[`run.sh`](/run.sh) adds some default `docker run` args (like `--runtime nvidia`, mounts a [`/data`](/data) cache, and detects devices)
```bash
# automatically pull or build a compatible container image
./run.sh $(./autotag ros)

# or manually specify one of the container images above
./run.sh dustynv/ros:iron-desktop-l4t-r35.1.0

# or if using 'docker run' (specify image and mounts/ect)
sudo docker run --runtime nvidia -it --rm --network=host dustynv/ros:iron-desktop-l4t-r35.1.0
```
To mount your own directories into the container, use the [`-v`](https://docs.docker.com/engine/reference/commandline/run/#volume) or [`--volume`](https://docs.docker.com/engine/reference/commandline/run/#volume) flags:
```bash
./run.sh -v /path/on/host:/path/in/container $(./autotag ros)
```
To start the container running a command, as opposed to the shell:
```bash
./run.sh $(./autotag ros) my_app --abc xyz
```
</details>
<details open>
<summary><b>BUILD CONTAINER</b></summary>
</br>

If you use [`autotag`](/autotag) as shown above, it'll ask to build the container for you if needed.  To manually build it, first do this System Setup, then run:
```bash
./build.sh ros
```
The dependencies from above will be built into the container, and it'll be tested.  See [`./build.sh --help`](/jetson_containers/build.py) for build options.
</details>