def get_annotated_points(path, annotated_file_name):
    """
    get_annotated_points(file path in computer, name of annotated file).\n
    This function returns annotated points.
    """

    # path = "/home/bhatti/Documents/Education/Final Semester/Thesis/Set1Part0/"
    annotation_file_path = path + annotated_file_name

    file = open(annotation_file_path, 'r')

    # varaible to store points of annotations
    points_array = []
    annotated_points = {}

    for line in file:
        content = line.split(':')
        image_name = content[0]
        # image_file = path + image_name
        points_array.clear()

        # when there is no sign in the image
        if content[1] == "\n":
            continue
        else:
            signs_info_list = content[1].split(';')
            for signs_info in signs_info_list:
                if signs_info == "MISC_SIGNS" or signs_info == "\n":
                    continue
                else:
                    splited_sign_info = signs_info.split(', ')
                    points = [splited_sign_info[1], splited_sign_info[2],
                              splited_sign_info[3], splited_sign_info[4]]

                points_array.append(points)

        annotated_points[image_name] = points_array

    return annotated_points
