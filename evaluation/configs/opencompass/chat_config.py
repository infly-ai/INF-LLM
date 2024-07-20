from mmengine.config import read_base

with read_base():
    # Exam
    from .datasets.ceval.ceval_gen_5f30c7 import ceval_datasets
    from .datasets.agieval.agieval_gen_617738 import agieval_datasets
    from .datasets.mmlu.mmlu_gen_4d595a import mmlu_datasets
    from .datasets.cmmlu.cmmlu_gen_c13365 import cmmlu_datasets
    from .datasets.GaokaoBench.GaokaoBench_gen_5cfe9e import GaokaoBench_datasets
    from .datasets.ARC_c.ARC_c_gen_1e0de5 import ARC_c_datasets
    from .datasets.ARC_e.ARC_e_gen_1e0de5 import ARC_e_datasets

    # Language
    from .datasets.SuperGLUE_WiC.SuperGLUE_WiC_gen_d06864 import WiC_datasets
    from .datasets.FewCLUE_chid.FewCLUE_chid_gen_0a29a2 import chid_datasets
    from .datasets.CLUE_afqmc.CLUE_afqmc_gen_901306 import afqmc_datasets
    from .datasets.SuperGLUE_WSC.SuperGLUE_WSC_gen_fe4bf3 import WSC_datasets
    from .datasets.tydiqa.tydiqa_gen_978d2a import tydiqa_datasets
    # from .datasets.flores.flores_gen_806ede import flores_datasets

    # Knowledge
    from .datasets.SuperGLUE_BoolQ.SuperGLUE_BoolQ_gen_883d50 import BoolQ_datasets
    from .datasets.commonsenseqa.commonsenseqa_gen_c946f2 import commonsenseqa_datasets
    from .datasets.triviaqa.triviaqa_gen_0356ec import triviaqa_datasets
    from .datasets.nq.nq_gen_0356ec import nq_datasets

    # Understanding
    from .datasets.CLUE_C3.CLUE_C3_gen_8c358f import C3_datasets
    from .datasets.race.race_gen_69ee4f import race_datasets
    from .datasets.obqa.obqa_gen_9069e4 import obqa_datasets
    from .datasets.FewCLUE_csl.FewCLUE_csl_gen_28b223 import csl_datasets
    from .datasets.lcsts.lcsts_gen_8ee1fe import lcsts_datasets
    from .datasets.Xsum.Xsum_gen_31397e import Xsum_datasets
    from .datasets.FewCLUE_eprstmt.FewCLUE_eprstmt_gen_740ea0 import eprstmt_datasets
    from .datasets.lambada.lambada_gen_217e11 import lambada_datasets

    # Reasonning
    from .datasets.CLUE_cmnli.CLUE_cmnli_gen_1abf97 import cmnli_datasets
    from .datasets.CLUE_ocnli.CLUE_ocnli_gen_c4cb6c import ocnli_datasets
    from .datasets.SuperGLUE_AX_b.SuperGLUE_AX_b_gen_4dfefa import AX_b_datasets
    from .datasets.SuperGLUE_AX_g.SuperGLUE_AX_g_gen_68aac7 import AX_g_datasets
    from .datasets.SuperGLUE_RTE.SuperGLUE_RTE_gen_68aac7 import RTE_datasets
    from .datasets.SuperGLUE_COPA.SuperGLUE_COPA_gen_91ca53 import COPA_datasets
    from .datasets.SuperGLUE_ReCoRD.SuperGLUE_ReCoRD_gen_a69961 import ReCoRD_datasets
    from .datasets.hellaswag.hellaswag_gen_6faab5 import hellaswag_datasets
    from .datasets.piqa.piqa_gen_1194eb import piqa_datasets
    from .datasets.siqa.siqa_gen_e78df3 import siqa_datasets
    from .datasets.math.math_0shot_gen_393424 import math_datasets
    from .datasets.gsm8k.gsm8k_0shot_gen_a58960 import gsm8k_datasets
    from .datasets.drop.drop_gen_8a9ed9 import drop_datasets
    from .datasets.humaneval.humaneval_gen_a82cae import humaneval_datasets
    from .datasets.mbpp.deprecated_mbpp_gen_1e1056 import mbpp_datasets
    from .datasets.bbh.bbh_gen_5b92b0 import bbh_datasets


datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
