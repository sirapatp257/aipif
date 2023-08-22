import io
import time
import random
import tomesd
import torch
from diffusers import DiffusionPipeline, utils
from Context import Context
from media.MediaManager import MediaManager
from pictures.PictureMaker import PictureMaker

class FastLocalSdPictureMaker(PictureMaker):       
    
    def make_picture(self, prompt_dict: dict):
        save_img = True        
        prompt, neg_prompt = self.create_prompt(prompt_dict)
        
        pipeline = DiffusionPipeline.from_pretrained("Lykon/DreamShaper", torch_dtype=torch.float16)
        pipeline = pipeline.to("cuda")
        image = pipeline(prompt=prompt,negative_prompt=neg_prompt).images[0]
        
        with io.BytesIO() as output:
            image.save(output, format="PNG")
            image_bytes = output.getvalue()
        
        if save_img:
            file_name = time.strftime("%Y%m%d_%H%M%S") + ''.join([str(random.randint(1, 9)) for _ in range(5)]) + ".png"
            image.save(file_name)        
        
        url = MediaManager.bytes_to_png_url(image_bytes)

        return url

    def create_prompt(self,prompt_dict: dict):
        prompt_types = ["positive","negative","style"]
        prompt_data = dict()
        for prompt_type in prompt_types:
            text_key = f"{prompt_type}_prompt_text"
            if text_key in prompt_dict:
                prompt_data[text_key] = prompt_dict[text_key]

        pos_text = prompt_data.get("positive_prompt_text")
        neg_text = prompt_data.get("negative_prompt_text")
        style_text = prompt_data.get("style_prompt_text")

        if pos_text == None:
            raise Exception("PictureMaker: No Positive Prompt")
        
        prompt = pos_text if style_text == None else pos_text + " in the style of " + style_text
        neg_prompt = neg_text

        return (prompt,neg_prompt)
    

