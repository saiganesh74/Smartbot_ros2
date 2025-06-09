# 🤖 SmartBot ROS2 Project

SmartBot is a modular, beginner-friendly robot built using ROS2 and Python. This project is designed for college robotics enthusiasts looking to learn real-world robotics software architecture using simulation before connecting actual hardware.

---

## Features

- `teleop_node`: Publishes `/cmd_vel` velocity commands using keyboard inputs or internal logic.
- `base_controller_node`: Simulates robot motion by printing received velocities.
- Modular design for easy integration of:
  - Motor driver logic
  - Obstacle sensors
  - Mapping and navigation
  - RViz/Gazebo simulation

---

## Installation & Setup

### Prerequisites

- Ubuntu 20.04 or 22.04
- ROS2 Humble (or later) installed
- Python 3.10+
- `colcon` build tool

### Setup Steps

```bash
# Clone the repository
git clone https://github.com/yourusername/Smartbot_ros2.git
cd Smartbot_ros2
```
# Install dependencies
rosdep install --from-paths src --ignore-src -r -y

# Build the workspace
colcon build

# Source the workspace (every new terminal session)
` source install/setup.bash `

### Structure
```
Smartbot_ros2/
├── src/
│   ├── teleop_node/
│   │   └── teleop.py
│   └── base_controller_node/
│       └── base_controller.py
├── install/
├── build/
├── log/
├── README.md
├── setup.py
└── package.xml
```
# Contributing
This project is open for contributions, improvements, and collaborations. Feel free to:

- Fork the repo
- Create issues
- Submit PRs

# Author
Sai Ganesh Rejeti <br>
📧 ganeshrejeti1@gmail.com <br>
🌐 <a href = 'https://www.linkedin.com/in/saiganeshrejeti/'>LinkedIn
