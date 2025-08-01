# utils.py

import cv2
import numpy as np
import os

# Load model only once
def load_colorization_model():
    proto_file = "models/colorization_deploy_v2.prototxt"
    model_file = "models/colorization_release_v2.caffemodel"
    pts_file = "models/pts_in_hull.npy"

    # SAFETY NOTE: These files must be manually downloaded by the user.
    # Do not commit licensed model files to GitHub.
    
    net = cv2.dnn.readNetFromCaffe(proto_file, model_file)
    pts = np.load(pts_file)

    # Populate cluster centers as 1x1 convolution kernel
    class8_ab = net.getLayerId("class8_ab")
    conv8_313_rh = net.getLayerId("conv8_313_rh")

    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8_ab).blobs = [pts.astype(np.float32)]
    net.getLayer(conv8_313_rh).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    return net

def colorize_image(image_path, output_path, net):
    bw_image = cv2.imread(image_path)
    normalized = bw_image.astype("float32") / 255.0
    lab = cv2.cvtColor(normalized, cv2.COLOR_BGR2LAB)

    l_channel = lab[:, :, 0]
    resized = cv2.resize(l_channel, (224, 224))
    resized -= 50  # Important shift

    net.setInput(cv2.dnn.blobFromImage(resized))
    ab_decoded = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab_decoded = cv2.resize(ab_decoded, (bw_image.shape[1], bw_image.shape[0]))

    lab_out = np.zeros(bw_image.shape, dtype="float32")
    lab_out[:, :, 0] = l_channel
    lab_out[:, :, 1:] = ab_decoded

    colorized = cv2.cvtColor(lab_out, cv2.COLOR_LAB2BGR)
    colorized = (np.clip(colorized, 0, 1) * 255).astype("uint8")
    cv2.imwrite(output_path, colorized)
    return output_path
