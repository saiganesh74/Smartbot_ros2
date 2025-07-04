from setuptools import find_packages, setup

package_name = 'smartbot_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/smartbot_launch']),
    ('share/smartbot_launch', ['package.xml']),
    ('share/smartbot_launch/launch', ['launch/smartbot_launch.py']),
],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='saiganesh',
    maintainer_email='ganeshrejeti1@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
