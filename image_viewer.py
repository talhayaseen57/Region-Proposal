import cv2 as cv
import numpy as np


def rescaleImage(image, scale=0.50):
    """
    This function helps to resize image with some ratio.
    """
    width = int(image.shape[1] * scale)
    length = int(image.shape[0] * scale)

    dimensions = (width, length)

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)


def imageViewer(image_path, annotated_points_array, box_color=(0, 255, 0), box_thickness=1, isReduced=False):
    image = cv.imread(image_path)

    if annotated_points_array != []:
        for annotated_points in annotated_points_array:
            cv.rectangle(image, (annotated_points[0], annotated_points[1]),
                         (annotated_points[2], annotated_points[3]), box_color, thickness=box_thickness)

    if isReduced:
        reduced_cv_image = rescaleImage(image)
        cv.imshow("Reduced " + image_path.split('/')[-1], reduced_cv_image)
    else:
        cv.imshow("Original " + image_path.split('/')[-1], image)

    cv.waitKey(0)
