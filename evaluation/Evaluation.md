
## Evaluation Details
LLM evaluation is subject to lots of factors such as prompt,  postprocess scripts and inference framework etc.

For the purpose of reproduction of evaluation results, we refer to open-source evaluation scripts
to report evaluation results.

### General Benchmark

- MMLU
- CMMLU
- GSM8k
- MATH
- BBH
- other tests in OpenCompass

For these tests, we use OpenCompass `0.2.5` (https://github.com/open-compass/opencompass/tree/0.2.5). The detailed settings are listed below:
* Base `configs/opencompass/base_config.py`
* Chat `configs/opencompass/chat_config.py`

Please install OpenCompass and place the relevant configuration files in `<opencompass_dir>/configs/`. Once this is done, you can launch an evaluation task as follows:

```bash
cd <opencompass_dir>
python run.py configs/<config_file> -w outputs/<output_dir>
```

### Coding

- Humaneval
- MBPP

For code benchmark, we are experiencing timeout and postprocess issues with Open-Compass.
So we refer to https://github.com/deepseek-ai/deepseek-coder/tree/main/Evaluation

We made several modifications to get our results in our report:

1. Add "\n":

    Base models are usually format-sensitive. For INF-34B, both '''\n and ]\n are a single token. The deepseek-coder's prompts end with ''' and ] during evaluation of HumanEval and MBPP respectively. This results in degradation of performance as the base model rarely
    sees these tokens in code corpus. Qwen1.5 is also subject to this case.

    This known deficiency is somewhat similar to the famous "trailing whitespace" introduced by current LLM tokenizers. We refer to an amazing video of Andrej Karpathy  https://www.youtube.com/watch?v=zduSFxRajkE to illustrate in detail.

    Thus we add '\n' for all the tests.

2. When evaluating HumanEval, We put "\nA:" as stop_word for Yi1.5.


3. (Optional) If experiencing OOM , empty cache before barrier.
    ```
    # add this！
    torch.cuda.empty_cache()
    accelerator.wait_for_everyone()
    ```

After these modifications:

```
cd HumanEval
MODEL_NAME_OR_PATH="MODEL"
DATASET_ROOT="data/"
LANGUAGE="python"
python -m accelerate.commands.launch --config_file test_config.yaml eval_pal.py --logdir ${MODEL_NAME_OR_PATH} --language ${LANGUAGE} --dataroot ${DATASET_ROOT}

cd MBPP
MODEL_NAME_OR_PATH="MODEL"
DATASET_ROOT="data/"
LANGUAGE="python"
python -m accelerate.commands.launch --config_file test_config.yaml eval_pal.py --logdir ${MODEL_NAME_OR_PATH} --dataroot ${DATASET_ROOT}

```

Thanks to the robust post-processing of deepseek-coder's evaluation scripts,
our reproduced results of these open-access models are higher than their own reports.

|       | Qwen1.5-32B-reproduced | Qwen1.5-32B-reported | Yi1.5-34B-reproduced |Yi1.5-34B-reported |
| ----------- | ----------- |----------- | ----------- |----------- |
| HumanEval | 44.51      | 37.2      |47.56       |46.3       |
| MBPP |  51.00       | 49.4      |65.6  |65.5      |


### Domain

For domain benchmarks, we use internal evaluation scripts. We put an example of prompt here.

*USMLE*:

We download the USMLE exam here: https://www.usmle.org/prepare-your-exam/


- prompt: 5-shot for base model

```
# 5-shot examples then the tested question with the format below:
**Question:**: A 58-year-old man with chronic obstructive pulmonary disease comes to the clinic with his wife for a follow-up examination. He has smoked one pack of cigarettes daily for 35 years. He has tried to quit smoking twice but was unsuccessful both times. At today’s visit, when the physician asks the patient about smoking cessation, he says he is not ready to do so. The patient’s wife states her husband’s smoking makes her cough and gives her chest tightness. Which of the following is the most appropriate physician statement?
A. Are there any reasons why you might want to quit smoking?
B. Are you aware that your lung condition is chronic at this point?
C. I'm sure you don't want your wife to suffer as a result of your smoking.
D. The majority of your health issues would improve if you quit smoking.
E. Why haven't you been able to stay off cigarettes?
**Answer:**
```

- prompt: 0-shot for chat model

```
The following are multiple choice questions (with answers) about medical knowledge, please answer the question step by step, then pick the correct option in \"The answer is [option]\" format.
Question:A 58-year-old man with chronic obstructive pulmonary disease comes to the clinic with his wife for a follow-up examination. He has smoked one pack of cigarettes daily for 35 years. He has tried to quit smoking twice but was unsuccessful both times. At today’s visit, when the physician asks the patient about smoking cessation, he says he is not ready to do so. The patient’s wife states her husband’s smoking makes her cough and gives her chest tightness. Which of the following is the most appropriate physician statement?
A. Are there any reasons why you might want to quit smoking?
B. Are you aware that your lung condition is chronic at this point?
C. I'm sure you don't want your wife to suffer as a result of your smoking.
D. The majority of your health issues would improve if you quit smoking.
E. Why haven't you been able to stay off cigarettes?

```





