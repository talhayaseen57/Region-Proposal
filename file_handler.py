import re


def getAnnotatedPoints(path, annotated_file_name):
    """
    getAnnotatedPoints(file path in computer, name of annotated file).\n
    This function returns annotated points.
    """

    # path = "/home/bhatti/Documents/Education/Final Semester/Thesis/Set1Part0/"
    annotation_file_path = path + annotated_file_name

    file = open(annotation_file_path, 'r')

    # varaible to store points of annotations
    points_array = []
    images_name_array = []
    annotated_points = {}

    for line in file:
        content = line.split(':')
        image_name = content[0]
        # image_file = path + image_name
        images_name_array.append(image_name)
        points_array = []

        # when there is no sign in the image
        if content[1] != "\n":
            signs_info_list = content[1].split(';')
            for signs_info in signs_info_list:
                if signs_info == "MISC_SIGNS" or signs_info == "\n" or signs_info == " \n":
                    continue
                else:
                    splited_sign_info = re.split(',\s*', signs_info)
                    points = [(splited_sign_info[1]), splited_sign_info[2],
                              splited_sign_info[3], splited_sign_info[4]]
                    try:
                        points = list(map(float, points))
                        points = list(map(int, points))
                    except ValueError:
                        for i in range(0, 4):
                            points[i] = int(points[i].split('.')[0])

                points_array.append(points)

        annotated_points[image_name] = points_array

    return images_name_array, annotated_points
