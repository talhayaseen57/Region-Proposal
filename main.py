# import cv2 as cv
import file_handler as handler


def main():
    file_path = "/home/bhatti/Documents/Education/Final Semester/Thesis/Set1Part0/"
    annotated_file_name = "annotations.txt"
    annotated_points = handler.get_annotated_points(
        file_path, annotated_file_name)
    # print(annotated_points.keys())


if __name__ == "__main__":
    main()
