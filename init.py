"""
NLP Research Toolkit

暴露核心组件与高层接口。统合包级全局导出接口，提升第三方调用的代码规范性与层级感。
"""

from .core.schema import TextInstance, SentencePair, FeatureVector, PredictionResult
from .core.text import TextNormalizer
from .features.sentiment_features import SentimentPriorFeatureExtractor
from .features.pairwise_features import PairwiseCompositeFeatureExtractor
from .models.sentiment_model import SentimentClassifier
from .models.similarity_model import PairwiseSimilarityModel
from .calibration.thresholding import DecisionThresholdOptimizer
from .mining.hard_negative import HardNegativeMiner
from .analysis.diagnostics import SimilarityDiagnostics

__all__ = [
    "TextInstance",
    "SentencePair",
    "FeatureVector",
    "PredictionResult",
    "TextNormalizer",
    "SentimentPriorFeatureExtractor",
    "PairwiseCompositeFeatureExtractor",
    "SentimentClassifier",
    "PairwiseSimilarityModel",
    "DecisionThresholdOptimizer",
    "HardNegativeMiner",
    "SimilarityDiagnostics"
]