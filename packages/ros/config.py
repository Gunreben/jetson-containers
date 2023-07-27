
from jetson_containers import L4T_VERSION

ROS_DISTROS = ['melodic', 'noetic', 'foxy', 'galactic', 'humble', 'iron']
ROS_PACKAGES = ['ros_base', 'ros_core', 'desktop']

# add permutations of ROS distros/packages as subpackages
template = package.copy()

template['group'] = 'ros'
template['depends'] = ['cmake', 'python', 'opencv']

package = []

for ROS_DISTRO in ROS_DISTROS:
    for ROS_PACKAGE in ROS_PACKAGES:
        pkg = template.copy()
        
        pkg['name'] = f"ros:{ROS_DISTRO}-{ROS_PACKAGE.replace('_', '-')}"
        
        pkg['build_args'] = {
            'ROS_VERSION': ROS_DISTRO,
            'ROS_PACKAGE': ROS_PACKAGE
        }
        
        if ROS_DISTRO == 'melodic':
            pkg['dockerfile'] = 'Dockerfile.ros.melodic'
            pkg['test'] = 'test_ros.sh'
            pkg['requires'] = '<34'   # melodic is for 18.04 only
        elif ROS_DISTRO == 'noetic':
            pkg['dockerfile'] = 'Dockerfile.ros.noetic'
            pkg['test'] = 'test_ros.sh'
        else:
            pkg['dockerfile'] = 'Dockerfile.ros2'
            pkg['test'] = 'test_ros2.sh'
            
        package.append(pkg)
