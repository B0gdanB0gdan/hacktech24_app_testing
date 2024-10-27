from segment_anything import sam_model_registry


class ModelSingleton:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelSingleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Only initialize once
        if not ModelSingleton._initialized:
            print("Initializing model...")  # Debug message
            self.model = self._load_model()
            ModelSingleton._initialized = True
    
    def _load_model(self):
        path_to_model = r'C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\segmentation\SoM\sam_vit_h_4b8939.pth'
        model_sam = sam_model_registry["vit_h"](checkpoint=path_to_model).eval().cuda()
        return model_sam
    
    def get_model(self):
        return self.model
