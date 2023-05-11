#config.py


#base model  

model_path = 'decapoda-research/llama-7b-hf'
model_architecture = 'llama' # use one of 'llama','other'


#lORA  
use_lora = True
lora_r= 8
lora_alpha= 16
lora_dropout= 0.00
lora_target_modules =  None
lora_bias = 'none'

#data_args

data_path = 'tatsu-lab/alpaca'
concat_config ={0:{'column':True,'text':'text'}}
data_source_type = 'hub_link'

# Trainer 
num_train_epochs = 1

per_device_train_batch_size = 4

gradient_accumulation_steps = 16
fp16 = False # dont change
device_map = 'auto'
learning_rate=2e-4
warmup_steps =100
logging_steps = 10
group_by_length = True

# wandb for tracking
use_wandb =True
wandb_login_key= '57b2ac6a1c49c9c7314b7f41141074c35321b4b1' # place in your wandb login key
wandb_project= "llamaAlpaca-Finetuning-Test"
wandb_run_name = ""
wandb_watch = ""  # options: false | gradients | all
wandb_log_model = ""  # options: false | true
resume_from_checkpoint = None,  # Will resume from the latest adapter

#hugging face hub

use_hugging_face= True # set this to true if you want to push your model to hugging facce hub after training
hf_login_key = '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'
hf_model_path = 'Zangs3011/llama_alpaca-lora'


# Memory Optimization
load_in_8bit = True
gradient_checkpointing=False
