"""
本模块提供高效的困难负样本挖掘机制。
核心思想利用低成本特征的表面匹配分数与高成本模型的语义差异进行对抗检索，快速定位导致模型混淆的边界样本。
这对于提升对比学习模型鲁棒性与加速收敛具有关键作用。
"""

from typing import List, Tuple, Any

class HardNegativeMiner:
    def __init__(self, lexical_scorer: Any, semantic_scorer: Any, margin: float = 0.3):
        self.lexical_scorer = lexical_scorer
        self.semantic_scorer = semantic_scorer
        self.margin = margin
        
    def mine_batch(self, anchor: str, candidates: List[str]) -> List[Tuple[str, float]]:
        hard_negatives = []
        
        for candidate in candidates:
            lexical_overlap = self.lexical_scorer.score(anchor, candidate)
            
            if lexical_overlap > 0.6:
                semantic_sim = self.semantic_scorer.score(anchor, candidate)
                
                if semantic_sim < (lexical_overlap - self.margin):
                    penalty_score = lexical_overlap - semantic_sim
                    hard_negatives.append((candidate, penalty_score))
                    
        hard_negatives.sort(key=lambda x: x[1], reverse=True)
        return hard_negatives