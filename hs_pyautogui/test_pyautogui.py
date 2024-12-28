import cv2
import numpy as np
import pyautogui

# 定义要查找的绿色范围
lower_green = np.array([8, 180, 52])  # HSV颜色空间中的下界
upper_green = np.array([8, 210, 52])  # HSV颜色空间中的上界

while True:
    # 截取屏幕截图
    screenshot = pyautogui.screenshot()

    # 转换截图为OpenCV图像
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # 将图像从RGB转换为HSV颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 创建掩码，检测绿色区域
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # 寻找绿色区域的轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 如果找到绿色区域，点击第一个找到的区域
    if contours:
        # 获取第一个轮廓的中心点坐标
        M = cv2.moments(contours[0])
        print(M)
        if M["m00"] > 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # 模拟鼠标点击
            pyautogui.click(cx, cy)

    # 显示原始图像和掩码图像（用于调试）
    # cv2.imshow("Original", frame)
    # cv2.imshow("Mask", mask)

    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭所有窗口
cv2.destroyAllWindows()
