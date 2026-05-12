"""
本模块致力于挖掘句子对之间的深层语义关联与硬冲突特征。
集成了统计学相似度、序列匹配指标以及基于启发式规则的逻辑冲突检测。
为兼顾计算低成本与表示能力，模块支持灵活挂载外部稠密向量模型提取深度语义特征，适用于语义匹配与释义识别任务。
"""

from typing import Optional, Any
from core.schema import SentencePair, FeatureVector

class PairwiseCompositeFeatureExtractor:
    def __init__(self, use_dense_model: bool = False, dense_model: Optional[Any] = None):
        self.use_dense_model = use_dense_model
        self.dense_model = dense_model

    def extract(self, pair: SentencePair) -> FeatureVector:
        tokens_a = pair.text_a.split()
        tokens_b = pair.text_b.split()
        
        features = {
            'jaccard_sim': self._jaccard_similarity(tokens_a, tokens_b),
            'length_ratio': self._length_ratio(tokens_a, tokens_b),
            'lcs_ratio': self._longest_common_subsequence_ratio(tokens_a, tokens_b),
            'digit_conflict': self._check_digit_conflict(tokens_a, tokens_b),
            'wh_word_match': self._check_wh_word_alignment(tokens_a, tokens_b)
        }
        
        dense_vec = None
        if self.use_dense_model and self.dense_model:
            dense_vec = self.dense_model.encode([pair.text_a, pair.text_b]).flatten().tolist()
            
        return FeatureVector(
            instance_id=pair.pair_id,
            features=features,
            dense_vector=dense_vec
        )

    def _jaccard_similarity(self, tokens_a: list, tokens_b: list) -> float:
        set_a, set_b = set(tokens_a), set(tokens_b)
        intersection = len(set_a & set_b)
        union = len(set_a | set_b)
        return intersection / union if union > 0 else 0.0

    def _length_ratio(self, tokens_a: list, tokens_b: list) -> float:
        len_a, len_b = len(tokens_a), len(tokens_b)
        if len_a == 0 or len_b == 0:
            return 0.0
        return min(len_a, len_b) / max(len_a, len_b)

    def _longest_common_subsequence_ratio(self, tokens_a: list, tokens_b: list) -> float:
        m, n = len(tokens_a), len(tokens_b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if tokens_a[i-1] == tokens_b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        lcs_len = dp[m][n]
        return lcs_len / max(m, n) if max(m, n) > 0 else 0.0

    def _check_digit_conflict(self, tokens_a: list, tokens_b: list) -> float:
        digits_a = set(t for t in tokens_a if t.isdigit())
        digits_b = set(t in tokens_b if t.isdigit())
        if not digits_a and not digits_b:
            return 0.0
        return 1.0 if digits_a != digits_b else 0.0

    def _check_wh_word_alignment(self, tokens_a: list, tokens_b: list) -> float:
        wh_words = {"who", "what", "where", "when", "why", "how"}
        wh_a = set(tokens_a) & wh_words
        wh_b = set(tokens_b) & wh_words
        return 1.0 if wh_a == wh_b else 0.0