
# INF-34B-Chat-GPTQ

<!-- description start -->
## Description

This repo contains GPTQ model file, which are made with [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ).


<details>
  <summary>Explanation of GPTQ parameters</summary>

- Bits: The bit size of the quantised model.
- GS: GPTQ group size. Higher numbers use less VRAM, but have lower quantisation accuracy. "None" is the lowest possible value.
- Act Order: True or False. Also known as `desc_act`. True results in better quantisation accuracy. Some GPTQ clients have had issues with models that use Act Order plus Group Size, but this is generally resolved now.
- Damp %: A GPTQ parameter that affects how samples are processed for quantisation. 0.01 is default, but 0.1 results in slightly better accuracy.
</details>

<!-- description end -->


<!-- README_GPTQ.md-use-from-python start -->

We provide the inference examples from Python code. You can then use the following code.

**Install the necessary packages**
Requires: The environment of the Hugging Face transformers is:
- Pytorch 2.3.0+cu121
- Flash Attention 2.5.0
- Transformers 4.42.4

```shell
pip3 install transformers optimum
pip3 uninstall -y auto-gptq
git clone https://github.com/infly-ai/AutoGPTQ
cd AutoGPTQ
git checkout inflm
pip3 install .
# If you are compiling on an A800/H800 GPU, you can add the environment 'export TORCH_CUDA_ARCH_LIST="8.0;9.0"'
```


**Inference with Huggingface's Transformers**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import time

model_path="path/to/model/"
device = "cuda" # the device to load the model onto
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True
)

prompt = "Write a resume for a fresh high school graduate who is seeking their first job. Make sure to include at least 12 placeholder represented by square brackets, such as [address], [name]."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(device)

context_time = 0
start = time.time()
generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=200
)
context_time += time.time() - start

generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print("=> response: ", response)
```

<!-- README_GPTQ.md-use-from-python end -->

<!-- README_GPTQ.md-compatibility start -->
**Inference with AutoGPTQ**

The above files provided are tested to work with Transformers. AutoGPTQ can also be used directly. 
**Note**: If you encounter RuntimeError: probability tensor contains either `inf`, `nan` or element < 0 during inference with transformers, or the generation token contains `<unk>`, we **strongly recommend** that you use the following method to run the code.


```python
import torch
from auto_gptq import AutoGPTQForCausalLM
from transformers import AutoTokenizer

model_path = "/path/to/model/"

device = "cuda:0"
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "left"

model = AutoGPTQForCausalLM.from_quantized(
    model_path,
    inject_fused_attention=False,
    inject_fused_mlp=False,
    device=device,
    trust_remote_code=True,
    use_marlin=True, # marlin kernel slove <unk> for gptq-4bit, for gptq-8bit set 'use_marlin=False'
    use_triton=False, # for gptq-8bit set 'use_triton=True'
)
model.eval()

prompts = [
    "I would like to",
    "北京的冬天很冷，广州的夏天很热。",
    "I have a dream that",
    "To be or not to be, that is the question.",
]

token_dict = tokenizer(prompts, return_tensors="pt", padding="longest").to(device)
with torch.inference_mode():
    output_ids = model.generate(**token_dict, max_new_tokens=200)
output_ids_cut = output_ids[:, token_dict["input_ids"].shape[1] :]

for nb, output_id in enumerate(output_ids_cut):
    print(f"Prompt {nb}: {prompts[nb]}")
    print(f"Generated: {tokenizer.decode(output_id, skip_special_tokens=False)}")
    print('*'*40)
```

<!-- README_GPTQ.md-compatibility end -->
