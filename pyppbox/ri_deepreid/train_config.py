import yaml

from yaml.loader import SafeLoader


class CFGDeepReID(object):

    def __init__(self):
        self.loadCFG("train_config.yaml")

    def set(self, cfg):
        self.classes_txt = cfg['classes_txt']
        self.classifier_pkl = cfg['classifier_pkl']
        self.train_data = cfg['train_data']
        self.model_name = cfg['model_name']
        self.model_path = cfg['model_path']

    def loadCFG(self, cfg_file):        
        with open(cfg_file) as rcf:
            cfg = yaml.load_all(rcf, Loader=SafeLoader)
            self.set(next(cfg))
