from __future__ import division, print_function, absolute_import

import sys
import cv2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + '/pybin')
os.environ['PATH']  = os.environ['PATH'] + ';' +  dir_path + '/pybin;'

import pyopenpose as op

class MyOpenPose(object):

    def __init__(self, cfg):
        self.params = dict()
        self.params["model_folder"] = cfg.model_folder
        self.params["model_pose"] = cfg.model_pose
        self.params["net_resolution"] = cfg.model_resolution
        self.params["output_resolution"] = cfg.output_resolution
        self.params["hand"] = cfg.hand
        self.params["face"] = False
        self.params["number_people_max"] = cfg.number_people_max
        self.params["disable_blending"] = cfg.disable_blending
        self.params["display"] = 0
        self.opWrapper = op.WrapperPython()
        self.opWrapper.configure(self.params)
        self.opWrapper.start()

    def detectImageFile(self, path):
        self.datum = op.Datum()
        imageToProcess = cv2.imread(path)
        self.datum.cvInputData = imageToProcess
        self.opWrapper.emplaceAndPop(op.VectorDatum([self.datum]))
        return self.datum.cvOutputData, self.datum.poseKeypoints

    def detectFrame(self, frame):
        self.datum = op.Datum()
        self.datum.cvInputData = frame
        self.opWrapper.emplaceAndPop(op.VectorDatum([self.datum]))
        return self.datum.cvOutputData, self.datum.poseKeypoints
        # return self.datum.cvOutputData, self.datum.faceRectangles, self.datum.poseKeypoints

