# import cv2 as cv
from file_handler import getAnnotatedPoints
from image_viewer import imageViewer
from image_annotator import annotateImage


def main():
    file_path = "/home/bhatti/Documents/Education/Final Semester/Thesis/Set1Part0/"
    annotated_file_name = "annotations.txt"
    image_names, annotated_points = getAnnotatedPoints(
        file_path, annotated_file_name)

    # imageViewer(
    #     file_path+image_names[50], annotated_points[image_names[50]], box_thickness=2)

    # save_file_path = "/home/bhatti/Documents/Education/Final Semester/Thesis/Annotated Images"
    # for image in image_names:
    #     annotateImage(file_path, image, save_file_path,
    #                   annotated_points[image])


if __name__ == "__main__":
    main()
