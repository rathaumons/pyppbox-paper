import yaml
from yaml.loader import SafeLoader

class CFGFacenet(object):

    def __init__(self):
        self.loadCFG("train_config.yaml")

    def set(self, cfg):
        self.gpu_mem = cfg['gpu_mem']
        self.model_det = cfg['model_det']
        self.model_file = cfg['model_file']
        self.classifier_file = cfg['classifier_file']
        self.data_path = cfg['data_path']
        self.batch_size = cfg['batch_size']
        self.min_confidence = cfg['min_confidence']

    def loadCFG(self, cfg_file):
        with open(cfg_file) as rcf:
            cfg = yaml.load_all(rcf, Loader=SafeLoader)
            self.set(next(cfg))
