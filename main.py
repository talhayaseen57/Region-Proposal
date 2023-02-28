# import cv2 as cv
import file_handler as handler
import image_viewer as viewer


def main():
    file_path = "/home/bhatti/Documents/Education/Final Semester/Thesis/Set1Part0/"
    annotated_file_name = "annotations.txt"
    image_names, annotated_points = handler.get_annotated_points(
        file_path, annotated_file_name)
    viewer.imageViewer(
        file_path+image_names[1500], annotated_points[image_names[1500]], box_thickness=2, isReduced=True)


if __name__ == "__main__":
    main()
