import numpy
#
# def Iou(arr_1, arr_2):
#     # 求两个框的面积
#     arr_1 = (arr_1[2] - arr_1[0]) * (arr_1[3] - arr_1[1])
#     arr_2 = (arr_2[2] - arr_2[0]) * (arr_2[3] - arr_2[1])
#
#     # 求交集的面积
#     x_1 = numpy.maximum(arr_1[0], arr_2[0])
#     y_1 = numpy.maximum(arr_1[1], arr_2[1])
#     x_2 = numpy.maximum(arr_1[2], arr_2[2])
#     y_2 = numpy.maximum(arr_1[3], arr_2[3])
#
#     w = numpy.maximum(0, x_2 - x_1)
#     h = numpy.maximum(0, y_2 - y_1)
#     inv = w * h
#
#     iou = inv / (arr_1 + arr_2 - inv)
#     return iou


def IouPro(box, boxes):
    # 求框的面积
    arr = (box[2] - box[0]) * (box[3] - box[1])
    # print(arr)
    arres = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
    # print(boxes[:, 2] - boxes[:, 0])
    # print(boxes[:, 3] - boxes[:, 1])
    # print(arres)

    x_1 = numpy.maximum(box[0], boxes[:, 0])
    y_1 = numpy.maximum(box[1], boxes[:, 1])
    x_2 = numpy.minimum(box[2], boxes[:, 2])
    y_2 = numpy.minimum(box[3], boxes[:, 3])

    w = numpy.maximum(0, x_2 - x_1)
    h = numpy.maximum(0, y_2 - y_1)

    # print(w)
    # print(h)
    inv = w * h
    iou = inv / (arr + arres - inv)
    return iou


# boex.shape（n , 5）
def Nms(boxes, thresh=0.3):
    new_index = numpy.argsort(-boxes[:, 0])
    # print(new_index)
    new_boxes = boxes[new_index]
    # print(new_boxes)
    # 最终输出所有的框
    boxes_result = []
    #
    while len(new_boxes) >= 1:
        box = new_boxes[0]
        # print(box)
        boxes_result.append(box)
        new_boxes = new_boxes[1:]
        # print(new_boxes)
        # 置信度最大的框和其他的框分别求iou
        iou = IouPro(box[1:], new_boxes[:, 1:])
        # print(iou)
        # 去除和第一个box的iou小于阈值的框
        box_index = numpy.where(iou < thresh)
        print(box_index)
        new_boxes = new_boxes[box_index]

        # exit()
    # if len(new_boxes) > 0:
    #     boxes_result.append(new_boxes[0])
    return boxes_result


if __name__ == '__main__':
    # box = numpy.array([0, 0, 4, 4])
    # boxes = numpy.array([[6, 6, 7, 7], [1, 1, 5, 5]])
    # iou = IouPro(box, boxes)
    # print(iou)

    boxes = numpy.array([[0.2, 1, 2, 4, 4],[0.9, 8, 8, 9, 9], [0.7, 1, 1, 4, 4]])
    boxes = Nms(boxes)
    print(boxes)
