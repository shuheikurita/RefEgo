import numpy as np

def normalize(boxes, h, w):
    if boxes.ndim == 1:
        boxes[[0, 2]] /= w
        boxes[[1, 3]] /= h
    elif boxes.ndim == 2:
        boxes[:, [0, 2]] /= w
        boxes[:, [1, 3]] /= h
    else:
        raise NotImplementedError
    return boxes

def denormalize(boxes, h, w):
    if boxes.ndim == 1:
        boxes[[0, 2]] *= w
        boxes[[1, 3]] *= h
    elif boxes.ndim == 2:
        boxes[:, [0, 2]] *= w
        boxes[:, [1, 3]] *= h
    else:
        raise NotImplementedError
    return boxes

def xyxy2xywh(boxes):
    axis = boxes.ndim - 1
    assert axis < 2
    x1, y1, x2, y2 = np.split(boxes, 4, axis=axis)
    cx = (x2 + x1) / 2
    cy = (y2 + y1) / 2
    w = x2 - x1
    h = y2 - y1
    return np.concatenate([cx, cy, w, h], axis=axis)

def x1y1wh2xyxy(boxes):
    axis = boxes.ndim - 1
    assert axis < 2
    x,y,w,h = np.split(boxes, 4, axis=axis)
    return np.concatenate([x,y,x+w,y+h], axis=axis)

def xywh2xyxy(boxes):
    boxes = boxes.copy()
    axis = boxes.ndim - 1
    assert axis < 2
    cx, cy, w, h = np.split(boxes, 4, axis=axis)
    x1 = cx - w/2
    y1 = cy - h/2
    x2 = cx + w/2
    y2 = cy + h/2
    return np.concatenate([x1, y1, x2, y2], axis=axis)
