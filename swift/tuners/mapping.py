# Copyright (c) Alibaba, Inc. and its affiliates.

from .adapter import Adapter, AdapterConfig
from .llamapro import LLaMAPro, LLaMAProConfig
from .longlora.longlora import LongLoRA, LongLoRAConfig
from .lora import LoRA, LoRAConfig
from .neftune import NEFTune, NEFTuneConfig
from .part import Part, PartConfig
from .prompt import Prompt, PromptConfig
from .reft import Reft, ReftConfig
from .restuning import ResTuning, ResTuningConfig
from .scetuning.scetuning import SCETuning, SCETuningConfig
from .side import Side, SideConfig


class SwiftTuners:
    ADAPTER = 'ADAPTER'
    PROMPT = 'PROMPT'
    LORA = 'LORA'
    SIDE = 'SIDE'
    RESTUNING = 'RESTUNING'
    LONGLORA = 'longlora'
    NEFTUNE = 'neftune'
    LLAMAPRO = 'LLAMAPRO'
    SCETUNING = 'SCETuning'
    PART = 'part'
    REFT = 'reft'


SWIFT_MAPPING = {
    SwiftTuners.ADAPTER: (AdapterConfig, Adapter),
    SwiftTuners.PROMPT: (PromptConfig, Prompt),
    SwiftTuners.LORA: (LoRAConfig, LoRA),
    SwiftTuners.SIDE: (SideConfig, Side),
    SwiftTuners.RESTUNING: (ResTuningConfig, ResTuning),
    SwiftTuners.LONGLORA: (LongLoRAConfig, LongLoRA),
    SwiftTuners.NEFTUNE: (NEFTuneConfig, NEFTune),
    SwiftTuners.SCETUNING: (SCETuningConfig, SCETuning),
    SwiftTuners.LLAMAPRO: (LLaMAProConfig, LLaMAPro),
    SwiftTuners.PART: (PartConfig, Part),
    SwiftTuners.REFT: (ReftConfig, Reft),
}
