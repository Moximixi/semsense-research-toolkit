"""
本模块封装情感分析的顶层预测逻辑。
通过融合稀疏语言学特征与稠密表示，实现情感极性的判定。
设计保留了模型可解释性接口，允许研究者追踪特定特征对最终分类决策的贡献度。
"""

from typing import List
from core.schema import FeatureVector, PredictionResult
import math

class SentimentClassifier:
    def __init__(self, feature_weights: dict, bias: float = 0.0):
        self.feature_weights = feature_weights
        self.bias = bias
        
    def predict(self, feature_vectors: List[FeatureVector]) -> List[PredictionResult]:
        results = []
        for vec in feature_vectors:
            logit = self.bias
            contributions = {}
            
            for feat_name, feat_val in vec.features.items():
                weight = self.feature_weights.get(feat_name, 0.0)
                contribution = feat_val * weight
                logit += contribution
                contributions[feat_name] = contribution
                
            probability = self._sigmoid(logit)
            predicted_label = 1 if probability >= 0.5 else 0
            
            results.append(PredictionResult(
                instance_id=vec.instance_id,
                predicted_label=predicted_label,
                probability=probability,
                confidence_score=abs(probability - 0.5) * 2,
                feature_contributions=contributions
            ))
        return results

    def _sigmoid(self, x: float) -> float:
        return 1 / (1 + math.exp(-x))