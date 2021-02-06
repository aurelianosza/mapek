import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)
from datetime import datetime


class AdaptationRequest(object):

    counter = 0

    def __init__(self, symptoms):
        AdaptationRequest.counter += 1
        self.id_request = AdaptationRequest.counter
        self.symptoms =  symptoms
        self.requested_at = datetime.now()
  

