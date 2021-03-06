class config:

	def __init__(self, configuration):
		
		self.configuration = configuration
		self.config = {
						"common":{},
						"train":{},
						"evaluation":{
								"dataroot":None,
								"test_set":["Set5", "Set14", "BSD100"],
								"models":{},
								
							}
						}
		self.get_config()


	def get_config(self):

		try:
			conf = getattr(self, self.configuration)
			conf()

		except: 
			print("Can not find configuration")
			raise
			
			flags.DEFINE_string("mode", "normal", "operation mode: normal or freq [normal]")

	def EDSR_WGAN(self):

		train_config = self.config["train"]

		train_config["mode"] = "small" # Operation mode: normal or freq [normal]
		train_config["epoch"] = 20000  # Number of epoch [10]
		train_config["batch_size"] = 16 # The size of batch images [128]
		train_config["image_size"] = 48 # The size of image to use [33]
		train_config["label_size"] = 96 # The size of label to produce [21]
		train_config["learning_rate"] = 1e-4/2 #The learning rate of gradient descent algorithm [1e-4]
		train_config["color_dim"] = 3 # Dimension of image color. [1]
		train_config["scale"] = 2 # The size of scale factor for preprocessing input image [3]
		train_config["train_extract_stride"] = 14 #The size of stride to apply input image [14]
		train_config["test_extract_stride"] = train_config["label_size"] #The size of stride to apply input image [14]
		train_config["checkpoint_dir"] = "/home/wei/ML/model/SuperResolution/SR-project-prototype/" #Name of checkpoint directory [checkpoint]
		train_config["log_dir"] = "/home/wei/ML/model/SuperResolution/SR-project-prototype/log/" #Name of checkpoint directory [checkpoint]
		train_config["output_dir"] = "output" # Name of sample directory [output]
		train_config["train_dir"] =  "Train" # Name of train dataset directory
		train_config["test_dir"] = "Test/Set5" # Name of test dataset directory [Test/Set5]
		train_config["h5_dir"] = "/home/wei/ML/dataset/SuperResolution/train" # Name of train dataset .h5 file
		train_config["train_h5_name"] = "train" # Name of train dataset .h5 file
		train_config["test_h5_name"] = "test" # Name of test dataset .h5 file
    
		train_config["ckpt_name"] = "EDSR_WGAN_v7_PatchWGAN" # Name of checkpoints # Gen's resblock=16, depth=28, L1 weighted 50 

		train_config["is_train"] = True # True for training, False for testing [True]
		train_config["model_ticket"] = "EDSR_WGAN" # Name of checkpoints     
		train_config["curr_epoch"] = 16776 # Name of checkpoints        

		def edsr_lsgan(self):
						
			mconfig = {}
			
			mconfig["EDSR_WGAN"] = {

										"scale":[1],
										"subimages":[96,96],
										"padding":[0,0],
										"ckpt_file":"/home/wei/ML/model/SuperResolution/SR-project-prototype/EDSR_WGAN_v7_PatchWGAN/EDSR_WGAN_v7_PatchWGAN-99400",
										"isGray": False,
										"isNormallized":True,
										"upsample": False,
										"sub_mean":False,
										"model_config" :{"d_inputs":None, "d_target":None,"scale":2,"feature_size" : 64,"dropout" : 1.0,"feature_size" : 64, "is_training":False, "reuse":False}
										}
			
			
			return mconfig

		

		eval_config = self.config["evaluation"]
		eval_config["dataroot"] = '/home/wei/ML/dataset/SuperResolution/'
		eval_config["test_set"] = ["Set5_model"]
		eval_config["models"] = [edsr_lsgan(self)]
		eval_config["summary_file"] = "example_summary.txt"        

	def EDSR_WGAN_att_v1(self):

		train_config = self.config["train"]

		train_config["mode"] = "small" # Operation mode: normal or freq [normal]
		train_config["epoch"] = 40000  # Number of epoch [10]
		train_config["batch_size"] = 16 # The size of batch images [128]
		train_config["image_size"] = 48 # The size of image to use [33]
		train_config["label_size"] = 96 # The size of label to produce [21]
		train_config["learning_rate"] = 1e-4 #The learning rate of gradient descent algorithm [1e-4]
		train_config["color_dim"] = 3 # Dimension of image color. [1]
		train_config["scale"] = 4 # The size of scale factor for preprocessing input image [3]
		train_config["train_extract_stride"] = 14 #The size of stride to apply input image [14]
		train_config["test_extract_stride"] = train_config["label_size"] #The size of stride to apply input image [14]
		train_config["checkpoint_dir"] = "/home/wei/ML/model/SuperResolution/SR-project-prototype/" #Name of checkpoint directory [checkpoint]
		train_config["log_dir"] = "/home/wei/ML/model/SuperResolution/SR-project-prototype/log/" #Name of checkpoint directory [checkpoint]
		train_config["output_dir"] = "output" # Name of sample directory [output]
		train_config["train_dir"] =  "Train" # Name of train dataset directory
		train_config["test_dir"] = "Test/Set5" # Name of test dataset directory [Test/Set5]
		train_config["h5_dir"] = "/home/wei/ML/dataset/SuperResolution/train" # Name of train dataset .h5 file
		train_config["train_h5_name"] = "train" # Name of train dataset .h5 file
		train_config["test_h5_name"] = "test" # Name of test dataset .h5 file
      
		train_config["ckpt_name"] = "025_10_full_PatchWGAN-GP_v4_ep0_MSE_lp_64_layer1_3" # Name of checkpoints 0.1 [1,1,1,1] ******************************               
                                   
		train_config["is_train"] = True # True for training, False for testing [True]
		train_config["model_ticket"] = "EDSR_WGAN_att" # Name of checkpoints
		train_config["curr_epoch"] = 0 # Name of checkpoints        
        
		def EDSR_WGAN_att_v1(self):
						
			mconfig = {}
			
			mconfig["EDSR_WGAN_att"] = {

										"scale":[1],
										"subimages":(80, 80, 3), #V1:[96,96]
										"padding":8,
										"ckpt_file":"/home/wei/ML/model/SuperResolution/SR-project-prototype/025_10_full_PatchWGAN-GP_v4_ep0_MSE_lp_28/best_performance/025_10_full_PatchWGAN-GP_v4_ep0_MSE_lp_28_0.0010903702350333333-70400",
#										"ckpt_file":"/home/wei/ML/model/SuperResolution/SR-project-prototype/025_10_full_PatchWGAN-GP_v4_ep0_MSE_lp_28/025_10_full_PatchWGAN-GP_v4_ep0_MSE_lp_28-81950",
#										"ckpt_file":"/mnt/GPU_Server/ML/model/SuperResolution/SR-project-prototype/025_10_full_PatchWGAN-GP_v4_ep0_MSE_lp_28_layer1_3_pre/025_10_full_PatchWGAN-GP_v4_ep0_MSE_lp_28_layer1_3_pre-272525",                                        
#										"ckpt_file":"/home/wei/ML/model/SuperResolution/SR-project-prototype/training_data/EDSR_WGAN_att_v1_x2_95_full/best_performance/EDSR_WGAN_att_v1_x2_95_full_0.009988665580749512-5225",
										"isGray": False,
										"isNormallized":True,
										"upsample": False,
										"sub_mean":False,
										"model_config" :{"d_inputs":None, "d_target":None, "scale":2, "feature_size":64, "reuse":False, "is_training":False, "net":"Gen"}
										}
			
			
			return mconfig

		eval_config = self.config["evaluation"]
		eval_config["dataroot"] = '/data/wei/dataset/SuperResolution/eval_input/'        
		eval_config["models"] = [EDSR_WGAN_att_v1(self)]
		eval_config["summary_file"] = "example_summary.txt"
        
	def EDSR_WGAN_MNIST(self):

		train_config = self.config["train"]

		train_config["mode"] = "small" # Operation mode: normal or freq [normal]
		train_config["epoch"] = 40  # Number of epoch [10]
		train_config["batch_size"] = 64 # The size of batch images [128]
		train_config["image_size"] = 28 # The size of image to use [33]
		train_config["label_size"] = 28 # The size of label to produce [21]
		train_config["learning_rate"] = 1e-4 #The learning rate of gradient descent algorithm [1e-4]
		train_config["color_dim"] = 1 # Dimension of image color. [1]
		train_config["scale"] = 2 # The size of scale factor for preprocessing input image [3]
		train_config["train_extract_stride"] = 14 #The size of stride to apply input image [14]
		train_config["test_extract_stride"] = train_config["label_size"] #The size of stride to apply input image [14]
		train_config["checkpoint_dir"] = "/home/wei/ML/model/SuperResolution/SR-project-prototype/" #Name of checkpoint directory [checkpoint]
		train_config["log_dir"] = "/home/wei/ML/model/SuperResolution/SR-project-prototype/log/" #Name of checkpoint directory [checkpoint]
		train_config["output_dir"] = "output" # Name of sample directory [output]
		train_config["train_dir"] =  "Train" # Name of train dataset directory
		train_config["test_dir"] = "Test/Set5" # Name of test dataset directory [Test/Set5]
		train_config["h5_dir"] = "/home/wei/ML/dataset/SuperResolution/train" # Name of train dataset .h5 file
		train_config["train_h5_name"] = "train" # Name of train dataset .h5 file
		train_config["test_h5_name"] = "test" # Name of test dataset .h5 file
		train_config["ckpt_name"] = "EDSR_WGAN_MNIST_v1" # Name of checkpoints       
		train_config["is_train"] = True # True for training, False for testing [True]
		train_config["model_ticket"] = "EDSR_WGAN_MNIST" # Name of checkpoints
		train_config["curr_epoch"] = 0 # Name of checkpoints        

		def edsr_lsgan(self):
						
			mconfig = {}
			
			mconfig["edsr_lsgan"] = {

										"scale":[1],
										"subimages":[80,80],
										"padding":[8,8],
										#"ckpt_file":"/home/ubuntu/model/model/SR_project/edsr_base_attention_v2_oh/edsr_base_attention_v2_oh-719656",
										"ckpt_file":"/home/wei/ML/model/SR_project/edsr_ls_gan_res4/edsr_ls_gan_res4-103712",
										"isGray": False,
										"isNormallized":True,
										"upsample": False,
										"sub_mean":False,
										"model_config" :{"d_inputs":None, "d_target":None,"scale":2,"feature_size" : 64,"dropout" : 1.0,"feature_size" : 64, "is_training":False, "reuse":False}
										}
			
			
			return mconfig

		

		eval_config = self.config["evaluation"]
		eval_config["dataroot"] = '/home/ubuntu/dataset/SuperResolution/'
		eval_config["test_set"] = ["Set5"]
		eval_config["models"] = [edsr_lsgan(self)]
		eval_config["summary_file"] = "example_summary.txt"        