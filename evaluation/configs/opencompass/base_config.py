from mmengine.config import read_base

with read_base():
    # Exam
    from .datasets.ceval.ceval_ppl_578f8d import ceval_datasets
    from .datasets.agieval.agieval_mixed_0fa998 import agieval_datasets
    from .datasets.mmlu.mmlu_ppl_ac766d import mmlu_datasets
    from .datasets.cmmlu.cmmlu_ppl_041cbf import cmmlu_datasets
    from .datasets.GaokaoBench.GaokaoBench_mixed_9af5ee import GaokaoBench_datasets
    from .datasets.ARC_c.ARC_c_ppl_2ef631 import ARC_c_datasets
    from .datasets.ARC_e.ARC_e_ppl_2ef631 import ARC_e_datasets

    # Knowledge
    from .datasets.SuperGLUE_BoolQ.SuperGLUE_BoolQ_gen_883d50 import BoolQ_datasets
    from .datasets.commonsenseqa.commonsenseqa_ppl_5545e2 import commonsenseqa_datasets
    from .datasets.triviaqa.triviaqa_gen_0356ec import triviaqa_datasets
    from .datasets.nq.nq_gen_3dcea1 import nq_datasets
    
    # Understanding
    from .datasets.CLUE_C3.CLUE_C3_gen_8c358f import C3_datasets
    from .datasets.race.race_ppl_5831a0 import race_datasets
    from .datasets.obqa.obqa_ppl_6aac9e import obqa_datasets
    from .datasets.FewCLUE_csl.FewCLUE_csl_ppl_841b62 import csl_datasets
    from .datasets.lcsts.lcsts_gen_8ee1fe import lcsts_datasets
    from .datasets.Xsum.Xsum_gen_31397e import Xsum_datasets
    from .datasets.FewCLUE_eprstmt.FewCLUE_eprstmt_gen_740ea0 import eprstmt_datasets
    from .datasets.lambada.lambada_gen_8b48a5 import lambada_datasets
    
    # Reasonning
    from .datasets.CLUE_cmnli.CLUE_cmnli_gen_51e956 import cmnli_datasets
    from .datasets.CLUE_ocnli.CLUE_ocnli_gen_51e956 import ocnli_datasets
    from .datasets.SuperGLUE_AX_b.SuperGLUE_AX_b_ppl_6db806 import AX_b_datasets
    from .datasets.SuperGLUE_AX_g.SuperGLUE_AX_g_gen_68aac7 import AX_g_datasets
    from .datasets.SuperGLUE_RTE.SuperGLUE_RTE_gen_68aac7 import RTE_datasets
    from .datasets.SuperGLUE_COPA.SuperGLUE_COPA_gen_91ca53 import COPA_datasets
    from .datasets.SuperGLUE_ReCoRD.SuperGLUE_ReCoRD_gen_30dea0 import ReCoRD_datasets
    from .datasets.hellaswag.hellaswag_ppl_a6e128 import hellaswag_datasets
    from .datasets.piqa.piqa_ppl_0cfff2 import piqa_datasets
    from .datasets.siqa.siqa_ppl_e8d8c5 import siqa_datasets
    from .datasets.math.math_gen_265cce import math_datasets
    from .datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    from .datasets.drop.drop_gen_8a9ed9 import drop_datasets
    from .datasets.humaneval.humaneval_gen_a82cae import humaneval_datasets
    from .datasets.mbpp.deprecated_mbpp_gen_1e1056 import mbpp_datasets
    from .datasets.bbh.bbh_gen_5b92b0 import bbh_datasets


datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
