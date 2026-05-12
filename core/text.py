"""
本模块专注于自然语言文本的底层清洗与标准化操作。
针对中英文混合文本的复杂性，提供统一的字符级别过滤、全半角转换以及多语言边界对齐功能。
设计重点在于以极低的计算成本实现文本的规范化，保障后续特征提取模块的输入质量与处理效率。
"""

import re
import unicodedata

class TextNormalizer:
    def __init__(self, lowercase: bool = True, remove_urls: bool = True):
        self.lowercase = lowercase
        self.remove_urls = remove_urls
        self._url_pattern = re.compile(r'https?://\S+|www\.\S+')
        self._cjk_pattern = re.compile(r'([\u4e00-\u9fa5])')
        
    def normalize(self, text: str) -> str:
        if not text:
            return ""
        
        text = unicodedata.normalize('NFKC', text)
        
        if self.remove_urls:
            text = self._url_pattern.sub('<URL>', text)
            
        if self.lowercase:
            text = text.lower()
            
        text = self._insert_cjk_spaces(text)
        text = self._clean_whitespace(text)
        
        return text

    def _insert_cjk_spaces(self, text: str) -> str:
        text = self._cjk_pattern.sub(r' \1 ', text)
        return text

    def _clean_whitespace(self, text: str) -> str:
        return ' '.join(text.split())