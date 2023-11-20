from setuptools import find_packages, setup

package_name = 'video_2_ros2_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pep',
    maintainer_email='jrueda@ikerlan.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'video = video_2_ros2_topic.video:main',
            'webcam = video_2_ros2_topic.webcam:main',
        ],
    },
)
