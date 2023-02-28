# import cv2 as cv
from file_handler import getAnnotatedPoints
from image_viewer import imageViewer


def main():
    file_path = "/home/bhatti/Documents/Education/Final Semester/Thesis/Set1Part0/"
    annotated_file_name = "annotations.txt"
    image_names, annotated_points = getAnnotatedPoints(
        file_path, annotated_file_name)

    imageViewer(
        file_path+image_names[50], annotated_points[image_names[50]], box_thickness=2)


if __name__ == "__main__":
    main()
