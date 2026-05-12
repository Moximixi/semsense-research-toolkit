"""
本模块构建系统的错误分析与模型诊断框架。
通过实施置信度分桶和元数据分组聚合，研究者可以精准定位模型在特定子群体或特定特征分布下的性能瓶颈。
此工具极大降低了分析预测盲区的认知成本，为后续特征迭代提供量化依据。
"""

from typing import List, Dict
from collections import defaultdict
from core.schema import PredictionResult

class SimilarityDiagnostics:
    def __init__(self, num_buckets: int = 5):
        self.num_buckets = num_buckets
        
    def analyze_confidence_buckets(self, predictions: List[PredictionResult], ground_truths: Dict[str, int]) -> Dict[str, dict]:
        buckets = defaultdict(list)
        
        for pred in predictions:
            bucket_idx = int(pred.confidence_score * self.num_buckets)
            bucket_idx = min(bucket_idx, self.num_buckets - 1)
            bucket_name = f"bucket_{bucket_idx}"
            
            true_label = ground_truths.get(pred.instance_id)
            is_correct = 1 if true_label == pred.predicted_label else 0
            
            buckets[bucket_name].append(is_correct)
            
        report = {}
        for b_name, results in buckets.items():
            accuracy = sum(results) / len(results) if results else 0.0
            report[b_name] = {
                'volume': len(results),
                'accuracy': accuracy
            }
            
        return report

    def diagnose_errors(self, predictions: List[PredictionResult], ground_truths: Dict[str, int], top_k: int = 10) -> List[PredictionResult]:
        errors = []
        for pred in predictions:
            true_label = ground_truths.get(pred.instance_id)
            if true_label is not None and true_label != pred.predicted_label:
                errors.append(pred)
                
        errors.sort(key=lambda x: x.confidence_score, reverse=True)
        return errors[:top_k]