# copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from . import cv

FasterRCNN = cv.models.FasterRCNN
YOLOv3 = cv.models.YOLOv3
MaskRCNN = cv.models.MaskRCNN
transforms = cv.transforms.det_transforms
visualize = cv.models.utils.visualize.visualize_detection
