"""
本模块定义了整个工具库的核心数据结构。
通过 Python 原生的 dataclass 机制实现数据的强类型约束与结构化封装，确保不同模块之间数据流转的严谨性与一致性。
模块内抽象了单文本实例、句子对实例以及模型预测结果的基类，为后续的特征工程与模型评估奠定底层架构。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class TextInstance:
    text_id: str
    text: str
    label: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SentencePair:
    pair_id: str
    text_a: str
    text_b: str
    label: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class FeatureVector:
    instance_id: str
    features: Dict[str, float] = field(default_factory=dict)
    dense_vector: Optional[List[float]] = None

@dataclass
class PredictionResult:
    instance_id: str
    predicted_label: int
    probability: float
    confidence_score: float
    feature_contributions: Dict[str, float] = field(default_factory=dict)