import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ================= 数据预处理 =================
def process_policy_data(file_path):
    """处理单个策略数据，返回各关节平均扭矩和标准差"""
    df = pd.read_csv(file_path)
    avg_torques = [df[f"torque_{i}"].abs().mean() for i in range(12)]
    std_torques = [df[f"torque_{i}"].abs().std() for i in range(12)]
    return avg_torques, std_torques

# 读取四个策略的数据

policy2_mean, policy2_std = process_policy_data("torque_data.csv")

# ================= 绘图 =================
plt.figure(figsize=(14, 7), dpi=120)
x = np.arange(12)  # 12个关节的位置

# 为了防止不同策略的误差条重叠，这里给 x 轴稍作偏移
offset = 0.4
offset2 = 0.2

# 策略1：只画误差条和中间的水平线表示平均值
# plt.errorbar(x - offset, policy1_mean, yerr=policy1_std, fmt='none',
#              ecolor='green', capsize=5, label='KYON wheel-active')
# plt.plot(x - offset, policy1_mean, '_', markersize=15, color='green')
# # 在每个数据点上显示均值
# # for i, mean in enumerate(policy1_mean):
# #     plt.text(x[i] - offset, mean, f'{mean:.2f}', ha='center', va='bottom', fontsize=10, color='green')

# 策略2：同上
plt.errorbar(x + offset, policy2_mean, yerr=policy2_std, fmt='none',
             ecolor='red', capsize=5, label='KYON wheel-fixed')
plt.plot(x + offset, policy2_mean, '_', markersize=15, color='red')
# for i, mean in enumerate(policy2_mean):
#     plt.text(x[i] + offset, mean, f'{mean:.2f}', ha='center', va='bottom', fontsize=10, color='red')

# # 策略3：同上
# plt.errorbar(x - offset2, policy3_mean, yerr=policy3_std, fmt='none',
#              ecolor='blue', capsize=5, label='Unitree wheel-active')
# plt.plot(x - offset2, policy3_mean, '_', markersize=15, color='blue')
# # for i, mean in enumerate(policy3_mean):
# #     plt.text(x[i] - offset2, mean, f'{mean:.2f}', ha='center', va='bottom', fontsize=10, color='blue')

# # 策略4：同上
# plt.errorbar(x + offset2, policy4_mean, yerr=policy4_std, fmt='none',
#              ecolor='black', capsize=5, label='Unitree wheel-fixed')
# plt.plot(x + offset2, policy4_mean, '_', markersize=15, color='black')
# # for i, mean in enumerate(policy4_mean):
# #     plt.text(x[i] + offset2, mean, f'{mean:.2f}', ha='center', va='bottom', fontsize=10, color='black')

# 设置 x 轴刻度和标签
joint_labels = ['LF_HAA', 'LH_HAA', 'RF_HAA', 'RH_HAA', 
                'LF_HFE', 'LH_HFE', 'RF_HFE', 'RH_HFE', 
                'LF_KFE', 'LH_KFE', 'RF_KFE', 'RH_KFE']
plt.xticks(x, joint_labels, rotation=45, fontsize=18, ha='right')

plt.ylabel("Average Torque (N·m)", fontsize=25, labelpad=10)
plt.xlabel("Joints", fontsize=25, labelpad=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(frameon=True, shadow=True, loc='upper right', fontsize=18)
plt.xticks(fontsize=20)  # 增加横坐标刻度标签字体大小
plt.yticks(fontsize=20)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
# plt.savefig('torque_max.pdf', bbox_inches='tight',dpi=600)
plt.show()
