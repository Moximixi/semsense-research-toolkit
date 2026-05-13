# semsense-research-toolkit

**多维文本语义与情感分析研究套件 / Multidimensional Text Semantics and Sentiment Analysis Research Toolkit**

------

## 🇨🇳 中文说明 / Chinese Version

### 1. 项目简介

本项目是一个专为自然语言处理学术研究与算法实验打造的高阶工具库。项目核心聚焦于情感分析与句子级语义匹配两大基础任务。有别于常规的工程化展示代码，本项目旨在体现深度的自然语言处理研究思想与特征建模能力。代码全程采用 Python 原生的强类型约束与结构化封装，不仅保障了实验数据的严谨流转，同时极大地降低了外部开发者阅读与二次开发的认知成本。

### 2. 核心功能与架构特性

工具包基于高度模块化的架构设计，主要提供以下核心能力：

- **低成本文本标准化：** 高效处理中英文混合文本，从底层解决全半角转换与多语言边界对齐问题，重点突出处理过程的计算效率与低成本优势。
- **先验语言学特征工程：** 无需依赖庞大深度模型，即可精准提取情感先验、否定作用域、程度副词衰减及主观表达等细粒度特征，兼顾解释性与运行效率。
- **复合语义对齐特征：** 融合 Jaccard 与最长公共子序列等浅层统计学指标，并结合数字冲突与疑问词不一致等深层逻辑冲突检测机制。同时支持外部稠密语义向量的灵活挂载。
- **动态阈值校准：** 突破静态决策边界，基于验证集自动搜索最优阈值，显著提升长尾分布或类别不平衡场景下的模型宏观评价表现。
- **对抗性挖掘与诊断：** 内置困难负样本挖掘模块以对抗性地提升模型鲁棒性。同时提供基于置信度分桶的精细化错误诊断框架，为后续特征迭代与误差分析提供量化依据。

### 3. 项目文件结构

项目根目录初始化文件实现了全局接口导出，统合各模块核心组件，规范了第三方调用逻辑。内部模块结构如下：

Plaintext

```
semsense-research-toolkit/
├── analysis/
│   ├── diagnostics.py         # 错误分析与置信度分桶诊断框架
│   └── hard_negative.py       # 困难负样本对抗挖掘机制
├── calibration/
│   ├── thresholding.py        # 动态决策边界搜索与优化
│   └── metrics.py             # 核心评估指标计算与校准支持
├── core/
│   ├── schema.py              # 核心数据结构与强类型约束定义
│   └── text.py                # 底层文本清洗与多语言对齐工具
├── features/
│   ├── sentiment_features.py  # 先验情感语言学特征抽取器
│   └── pairwise_features.py   # 句子对统计相似度与冲突特征抽取器
├── models/
│   ├── sentiment_model.py     # 情感极性分类预测与特征贡献度分析
│   └── similarity_model.py    # 语义相似度匹配与后端模型适配
└── __init__.py                # 项目根目录全局接口导出文件
```

------

## 🇬🇧 英文说明 / English Version

### 1. Project Overview

This project is an advanced toolkit designed specifically for academic research and algorithmic experiments in Natural Language Processing. **Initiated and maintained by researchers from the College of Cyber Security at Jinan University**, the project focuses primarily on two fundamental tasks: Sentiment Analysis and Semantic Matching. Unlike conventional engineering demonstration codes, this project aims to reflect deep research methodologies and feature modeling capabilities. The codebase strictly utilizes Python's strong type hinting and structured encapsulation, ensuring rigorous data flow during experiments while significantly reducing the cognitive cost for external developers.

### 2. Core Features and Architecture

The toolkit is built on a highly modular architecture, offering the following core capabilities:

- **Low-Cost Text Normalization:** Efficiently processes mixed Chinese and English texts, resolving full-width to half-width conversions and multilingual boundary alignment at the foundational level. The design emphasizes computational efficiency and low operational cost.
- **Prior Linguistic Feature Engineering:** Accurately extracts fine-grained features including sentiment priors, negation scopes, intensifier decay, and subjective expressions without relying on massive deep learning models. This ensures both high interpretability and efficiency.
- **Composite Semantic Alignment Features:** Integrates shallow statistical metrics such as Jaccard index and longest common subsequence, combined with deep logical conflict detection mechanisms like digit mismatches and interrogative word inconsistencies. It also supports the flexible mounting of external dense semantic vectors.
- **Dynamic Threshold Calibration:** Breaks through static decision boundaries by automatically searching for optimal thresholds based on validation sets, significantly improving the macro evaluation performance of models under long-tail distributions.
- **Adversarial Mining and Diagnostics:** Features a built-in hard negative mining module to adversarially enhance model robustness. It also provides a refined error diagnostic framework based on confidence bucketing, offering quantitative evidence for feature iteration and error analysis.

### 3. Project Structure

The root initialization file implements global interface exports, unifying core components across modules and standardizing third-party invocation logic. The internal structure is as follows:

Plaintext

```
semsense-research-toolkit/
├── analysis/
│   ├── diagnostics.py         # Error analysis and confidence bucketing diagnostic framework
│   └── hard_negative.py       # Hard negative adversarial mining mechanism
├── calibration/
│   ├── thresholding.py        # Dynamic decision boundary search and optimization
│   └── metrics.py             # Core evaluation metric calculation and calibration support
├── core/
│   ├── schema.py              # Core data structures and strong type constraint definitions
│   └── text.py                # Fundamental text cleaning and multilingual alignment tools
├── features/
│   ├── sentiment_features.py  # Prior sentiment linguistic feature extractor
│   └── pairwise_features.py   # Sentence-pair statistical similarity and conflict feature extractor
├── models/
│   ├── sentiment_model.py     # Sentiment polarity classification prediction and feature contribution analysis
│   └── similarity_model.py    # Semantic similarity matching and backend model adaptation
└── __init__.py                # Root directory global interface export file
```

------

## 项目声明
本项目的作者及单位：
```
项目名称：Multidimensional Text Semantics and Sentiment Analysis Research Toolkit
项目作者：Wenxiao Liu, Zhiquan Liu
作者单位：暨南大学网络空间安全学院
```

## 开源许可 / Open Source License

本项目采用 [MIT License](https://www.google.com/search?q=https://opensource.org/licenses/MIT) 开源协议。

This project is licensed under the [MIT License](https://www.google.com/search?q=https://opensource.org/licenses/MIT).

Copyright (c) 2026 Researchers from College of Cyber Security, Jinan University

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.