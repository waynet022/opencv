import cv2 as cv
import argparse

def parser():
    parser = argparse.ArgumentParser(description='OpenCV Reader')
    parser.add_argument("--image", type=str, help='Path to the image')
    parser.add_argument("--video", type=str, help='Path to the video')
    parser.add_argument("--scale", type=float, default=1.00, help='Scale size of output')

    return parser.parse_args()

    