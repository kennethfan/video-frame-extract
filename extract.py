#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import cv2
import sys


def extract_frames(video_path: str, output_path: str):
    """
    从视频文件中提取帧并保存为图片。

    Args:
        video_path (str): 视频文件的路径。
        output_path (str): 保存帧图片的路径。

    Returns:
        None

    Raises:
        SystemExit: 如果无法打开视频文件，则打印错误信息并退出程序。

    """

    # 创建VideoCapture对象
    cap = cv2.VideoCapture(video_path)

    # 检查视频是否打开成功
    if not cap.isOpened():
        raise RuntimeError(f'Error: Could not open video. {video_path}')

    # 帧计数器
    frame_count = 0

    # 逐帧读取视频
    while True:
        # 读取下一帧
        ret, frame = cap.read()

        # 如果正确读取帧，ret为True
        if not ret:
            print("Done extracting frames. End of video.")
            break

        # 保存图片到文件
        cv2.imwrite(f'{output_path}/frame_{frame_count}.png', frame)
        frame_count += 1

    # 释放VideoCapture对象
    cap.release()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: python {sys.argv[0]} <input_file> <output_folder>')
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print(f'{sys.argv[1]} does not exist')
        sys.exit(1)
    if os.path.exists(sys.argv[2]):
        if not os.path.isdir(sys.argv[2]):
            print(f'{sys.argv[2]} already exists and is not a directory')
            sys.exit(1)
        extract_frames(sys.argv[1], sys.argv[2])
        sys.exit(0)
    if not os.makedirs(sys.argv[2]):
        print(f'Could not create folder {sys.argv[2]}')
        sys.exit(1)
    extract_frames(sys.argv[1], sys.argv[2])
