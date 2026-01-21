import os.path as osp
import numpy as np
from matplotlib import pyplot as plt



if __name__ == "__main__":
    this_data = np.load(
        osp.join(osp.dirname(__file__), "recovery_2025-09-11-17-21-02.npz"), allow_pickle=True
    )
    # 'time', 'action', 'actual_acc', 'actual_vel', 'joint_torque', 'foot_contact_force', 'joint_pos', 'joint_vel', 'base_quat', 'soc', 'current', 'vol'
    time = this_data["time"]
    joint_torque = this_data["joint_torque"]
    joint_pos = this_data["joint_pos"]
    joint_vel = this_data["joint_vel"]

    # plot
    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(time, joint_pos)
    plt.title("Joint Position")
    plt.xlabel("Time [s]")
    plt.ylabel("Position [rad]")
    plt.grid()
    plt.subplot(3, 1, 2)
    plt.plot(time, joint_vel)
    plt.title("Joint Velocity")
    plt.xlabel("Time [s]")
    plt.ylabel("Velocity [rad/s]")
    plt.grid()
    plt.subplot(3, 1, 3)
    plt.plot(time, joint_torque)
    plt.title("Joint Torque")
    plt.xlabel("Time [s]")
    plt.ylabel("Torque [Nm]")
    plt.grid()
    plt.tight_layout()
    plt.show()

