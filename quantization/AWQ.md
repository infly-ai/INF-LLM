# INF-34B-Chat-AWQ

<!-- description start -->
## Description

This repo contains AWQ model file, which are made with [AutoAWQ](https://github.com/casper-hansen/AutoAWQ).

<!-- description end -->

<!-- README_AWQ.md-use-from-python start -->

We provide the inference examples from Python code. You can then use the following code.

**Install the necessary packages**

Requires: The environment of the Hugging Face transformers is:
- Pytorch 2.3.0+cu121
- Flash Attention 2.5.0
- Transformers 4.42.4

```shell
pip3 install transformers optimum
pip3 uninstall -y autoawq
git clone https://github.com/infly-ai/AutoAWQ
cd AutoAWQ
git checkout inflm
pip3 install .
# If you are compiling on an A800/H800 GPU, you can add the environment 'export TORCH_CUDA_ARCH_LIST="8.0;9.0"'
```

**Inference with Huggingface's Transformers**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import time

model_path = "/path/to/model/"
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
print("=> response: \n", response)
```

<!-- README_AWQ.md-use-from-python end -->

<!-- README_AWQ.md-compatibility start -->
**Inference with AutoAWQ**

The above files provided are tested to work with Transformers. AutoAWQ can also be used directly.
We **recommend** that you use the following method to run the code.

```python
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer, TextStreamer

model_path = "/path/to/model/"
device = "cuda" # the device to load the model onto

model = AutoAWQForCausalLM.from_quantized(model_path, fuse_layers=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

prompt = "Write a resume for a fresh high school graduate who is seeking their first job. Make sure to include at least 12 placeholder represented by square brackets, such as [address], [name]."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer(
    text,
    return_tensors='pt'
).input_ids.cuda()

generation_output = model.generate(
    model_inputs, 
    streamer=streamer,
    max_new_tokens=200
)

print("Generated output:", generation_output)
print("Generated text: \n", tokenizer.decode(generation_output[0], skip_special_tokens=True))
```

<!-- README_AWQ.md-compatibility end -->
