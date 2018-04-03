import torch
from torchvision.transforms import ToTensor
from torch.autograd import Variable
import numpy as np
import torchvision
import importlib
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from model import Net
import os

"""Model 1 : /home/student/Documents/u-net_pytorch/epochs200_layer3_ori_256/"""
"""Model 2 : /home/student/Documents/u-net-pytorch-original/lr001_weightdecay00001/"""
"""Model 3 : /home/student/Documents/u-net_denoising/dataset_small_mask/"""
"""Model 4 : /home/student/Documents/Atom Segmentation APP/AtomSegGUI/atomseg_bupt_new_10/"""
"""Model 5 : /home/student/Documents/Atom Segmentation APP/AtomSegGUI/atomseg_bupt_new_100/"""
"""Model 6 : /home/student/Documents/Atom Segmentation APP/AtomSegGUI/atom_seg_gaussian_mask/"""


def load_model(model_path, data, scale_factor, cuda):

	net = Net(upscale_factor = scale_factor)

	if cuda:
		net = net.cuda()

#	if not cuda:
#		net.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage))
#	else:
#		net.load_state_dict(torch.load(model_path))
	if os.name == 'posix':
		net = torch.load(model_path)
	else:
		from functools import partial
		import pickle
		pickle.load = partial(pickle.load, encoding="latin1")
		pickle.Unpickler = partial(pickle.Unpickler, encoding="latin1")
		net = torch.load(model_path, map_location=lambda storage, loc: storage, pickle_module=pickle)

	transform = ToTensor()
	ori_tensor = transform(data)
	if cuda:
		ori_tensor = Variable(ori_tensor.cuda())
	else:
		ori_tensor = Variable(ori_tensor)
	ori_tensor = torch.unsqueeze(ori_tensor,0)

	output = net(ori_tensor)

	if cuda:
		result = (output.data).cpu().numpy()
	else:
		result = (output.data).numpy()

	result = result[0,0,:,:]
	return result


def PIL2Pixmap(im):
    """Convert PIL image to QImage """
    if im.mode == "RGB":
        pass
    elif im.mode == "L":
        im = im.convert("RGBA")
    data = im.convert("RGBA").tobytes("raw", "RGBA")
    qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def map01(mat):
    return (mat - mat.min())/(mat.max() - mat.min())
