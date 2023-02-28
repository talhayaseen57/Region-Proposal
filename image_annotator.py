import cv2 as cv
import os


def annotateImage(file_path, image_name, save_file_path, annotated_points_array):
    image = cv.imread(file_path+image_name)

    if annotated_points_array != []:
        for annotated_points in annotated_points_array:
            cv.rectangle(image, (annotated_points[0], annotated_points[1]),
                         (annotated_points[2], annotated_points[3]), (0, 255, 0), thickness=2)

    cv.imshow(image_name, image)
    key = cv.waitKey(0) & 0xFF

    if key == ord('s'):
        cv.imwrite(os.path.join(save_file_path, image_name), image)
        cv.destroyAllWindows()
