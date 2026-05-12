"""
本模块专注于分类决策边界的动态校准。
突破静态阈值设定，基于验证集预测概率分布，搜索能够使特定评估指标最大化的最优阈值。
该机制可显著优化模型在类别不平衡或长尾分布场景下的决策表现。
"""

from typing import List, Tuple
import numpy as np

class DecisionThresholdOptimizer:
    def __init__(self, target_metric: str = 'f1'):
        self.target_metric = target_metric
        
    def optimize(self, probabilities: List[float], labels: List[int]) -> Tuple[float, float]:
        probs_array = np.array(probabilities)
        labels_array = np.array(labels)
        
        best_threshold = 0.5
        best_score = 0.0
        
        thresholds = np.linspace(0.1, 0.9, 81)
        
        for thresh in thresholds:
            preds = (probs_array >= thresh).astype(int)
            score = self._compute_metric(labels_array, preds)
            
            if score > best_score:
                best_score = score
                best_threshold = thresh
                
        return best_threshold, best_score

    def _compute_metric(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        tp = np.sum((y_true == 1) & (y_pred == 1))
        fp = np.sum((y_true == 0) & (y_pred == 1))
        fn = np.sum((y_true == 1) & (y_pred == 0))
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        
        if precision + recall == 0:
            return 0.0
            
        return 2 * (precision * recall) / (precision + recall)