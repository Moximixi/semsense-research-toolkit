"""
本模块处理句子对级别的语义匹配与相似度计算任务。
模型接收复合特征输入，利用多层感知或特征加权机制输出相似度得分。
该架构专门针对文本蕴含与释义识别任务进行了接口适配，支持后期阈值校准机制的无缝接入。
"""

from typing import List, Any
from core.schema import FeatureVector, PredictionResult

class PairwiseSimilarityModel:
    def __init__(self, classifier_backend: Any):
        self.backend = classifier_backend
        
    def predict_similarity(self, feature_vectors: List[FeatureVector]) -> List[PredictionResult]:
        results = []
        
        for vec in feature_vectors:
            feature_array = self._flatten_features(vec)
            prob = self.backend.predict_proba([feature_array])[0][1]
            
            results.append(PredictionResult(
                instance_id=vec.instance_id,
                predicted_label=1 if prob >= 0.5 else 0,
                probability=prob,
                confidence_score=prob,
                feature_contributions={} 
            ))
            
        return results

    def _flatten_features(self, vec: FeatureVector) -> List[float]:
        flat = list(vec.features.values())
        if vec.dense_vector:
            flat.extend(vec.dense_vector)
        return flat