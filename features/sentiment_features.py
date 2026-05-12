"""
本模块构建情感分析任务的专门化特征提取流水线。
重点提取具有强语言学先验的特征，涵盖情感词典匹配、否定修饰作用域解析、程度副词权重衰减以及主观性表达标志。
该提取器旨在不依赖庞大深度模型的前提下，高效捕获文本中的细粒度情感线索。
"""

from typing import List, Dict, Set
from core.schema import TextInstance, FeatureVector

class SentimentPriorFeatureExtractor:
    def __init__(self, sentiment_lexicon: Dict[str, float], negation_words: Set[str], intensifiers: Dict[str, float]):
        self.sentiment_lexicon = sentiment_lexicon
        self.negation_words = negation_words
        self.intensifiers = intensifiers
        
    def extract(self, instance: TextInstance) -> FeatureVector:
        tokens = instance.text.split()
        features = {}
        
        features['lexicon_score'] = self._calculate_lexicon_score(tokens)
        features['negation_count'] = self._count_negations(tokens)
        features['intensifier_score'] = self._calculate_intensifier_weight(tokens)
        features['subjectivity_ratio'] = self._estimate_subjectivity(tokens)
        
        return FeatureVector(
            instance_id=instance.text_id,
            features=features
        )

    def _calculate_lexicon_score(self, tokens: List[str]) -> float:
        score = 0.0
        negation_active = False
        
        for token in tokens:
            if token in self.negation_words:
                negation_active = not negation_active
                continue
                
            if token in self.sentiment_lexicon:
                base_score = self.sentiment_lexicon[token]
                if negation_active:
                    base_score *= -1.0
                score += base_score
                
        return score

    def _count_negations(self, tokens: List[str]) -> float:
        return sum(1.0 for token in tokens if token in self.negation_words)

    def _calculate_intensifier_weight(self, tokens: List[str]) -> float:
        weight = 1.0
        for token in tokens:
            if token in self.intensifiers:
                weight *= self.intensifiers[token]
        return weight

    def _estimate_subjectivity(self, tokens: List[str]) -> float:
        if not tokens:
            return 0.0
        subjective_hits = sum(1 for token in tokens if token in self.sentiment_lexicon)
        return subjective_hits / len(tokens)