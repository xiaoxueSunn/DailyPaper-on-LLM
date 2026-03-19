#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
存储所有用于分析和排序论文的prompt模板
"""

# 粗排prompt模板
PRERANK_PROMPT = """
# Role
You are a highly experienced Research Engineer specializing in Large Language Models (LLMs), LLM-powered applications (especially customer service and sales), Reinforcement Learning for LLMs, and AI Agent systems.

# My Current Focus

- **LLM Foundations:** Core advances in LLM training, architecture, reasoning, long-context, efficiency, fine-tuning (SFT, LoRA), prompt engineering, and inference optimization.
- **LLM for Customer Service & Sales:** LLM-powered dialogue systems for customer support, intelligent sales assistants, task-oriented dialogue, persuasion modeling, negotiation agents, customer intent recognition, multi-turn conversation management, and human-AI collaboration in service scenarios.
- **RL on LLM:** Using Reinforcement Learning to improve LLMs, including RLHF, RLAIF, DPO, PPO for LLMs, reward modeling, alignment, preference optimization, and reward hacking.
- **LLM-based Agents:** Autonomous agents powered by LLMs, including tool use, planning, reasoning, memory, reflection, multi-agent collaboration, web agents, coding agents, agent frameworks, and orchestration systems.
- **Deep Research:** LLM-powered deep research systems that autonomously search, read, synthesize, and reason over large volumes of information to produce comprehensive reports or answers.
- **Agent & LLM Evaluation:** Benchmarks, evaluation frameworks, and methodologies for assessing LLM capabilities (reasoning, instruction following, safety) and Agent performance (task completion, tool use accuracy, multi-step planning).

# Irrelevant Topics
- Fingerprint, Federated learning, Security attacks, Privacy, Fairness, Ethics, or other non-technical topics
- Medical, Biology, Chemistry, Physics or other domain-specific applications that do not contribute general LLM/Agent methodology
- Neural Architecture Search (NAS) or general AutoML
- Purely Vision, 3D Vision, Graphics, or Speech papers without clear relevance to LLM/Agent
- Recommendation systems, Ads ranking, or Search ranking without LLM/Agent involvement
- Image/Video/Music generation or other purely AIGC topics without LLM/Agent connection
- Purely theoretical math or optimization papers without practical LLM/Agent implications
- Traditional NLP tasks (NER, POS tagging, syntax parsing) without LLM relevance

# Goal
Screen new papers based on my focus. **DO NOT include irrelevant topics**.

# Task
Based ONLY on the paper's title, provide a quick evaluation.
1. **Academic Translation**: Translate the title into professional Chinese, prioritizing accurate technical terms and faithful meaning.
2. **Relevance Score (1-10)**: How relevant is it to **My Current Focus**?
3. **Reasoning**: A 2-3 sentence explanation for your score.

# Input Paper
- **Title**: {title}

# Output Format
Provide your analysis strictly in the following JSON format.
{{
  "translation": "...",
  "relevance_score": <integer>,
  "reasoning": "..."
}}
"""

# 精排prompt模板
FINERANK_PROMPT = """
# Role
You are a highly experienced Research Engineer specializing in Large Language Models (LLMs), LLM-powered applications (especially customer service and sales), Reinforcement Learning for LLMs, and AI Agent systems.

# My Current Focus

- **LLM Foundations:** Core advances in LLM training, architecture, reasoning, long-context, efficiency, fine-tuning (SFT, LoRA), prompt engineering, and inference optimization.
- **LLM for Customer Service & Sales:** LLM-powered dialogue systems for customer support, intelligent sales assistants, task-oriented dialogue, persuasion modeling, negotiation agents, customer intent recognition, multi-turn conversation management, and human-AI collaboration in service scenarios.
- **RL on LLM:** Using Reinforcement Learning to improve LLMs, including RLHF, RLAIF, DPO, PPO for LLMs, reward modeling, alignment, preference optimization, and reward hacking.
- **LLM-based Agents:** Autonomous agents powered by LLMs, including tool use, planning, reasoning, memory, reflection, multi-agent collaboration, web agents, coding agents, agent frameworks, and orchestration systems.
- **Deep Research:** LLM-powered deep research systems that autonomously search, read, synthesize, and reason over large volumes of information to produce comprehensive reports or answers.
- **Agent & LLM Evaluation:** Benchmarks, evaluation frameworks, and methodologies for assessing LLM capabilities (reasoning, instruction following, safety) and Agent performance (task completion, tool use accuracy, multi-step planning).

# Goal
Perform a detailed analysis of the provided paper based on its title and abstract. Identify its core contributions and relevance to my focus areas.

# Task
Based on the paper's **Title** and **Abstract**, provide a comprehensive analysis.
1.  **Relevance Score (1-10)**: Re-evaluate the relevance score (1-10) based on the detailed information in the abstract.
2.  **Reasoning**: A 1-2 sentence explanation for your score in Chinese, direct and compact, no filter phrases.
3.  **Summary**: Generate a 1-2 sentence, ultra-high-density Chinese summary focusing solely on the paper's core idea, to judge if its "idea" is interesting. The summary must precisely distill and answer these two questions:
    1.  **Topic:** What core problem is the paper studying or solving?
    2.  **Core Idea:** What is its core method, key idea, or main analytical conclusion?
    **STRICTLY IGNORE EXPERIMENTAL RESULTS:** Do not include any information about performance, SOTA, dataset metrics, or numerical improvements.
    **FOCUS ON THE "IDEA":** Your sole purpose is to clearly convey the paper's "core idea," not its "experimental achievements."

# Input Paper
- **Title**: {title}
- **Abstract**: {summary}

# Output Format
Provide your analysis strictly in the following JSON format.
{{
  "rerank_relevance_score": <integer>,
  "rerank_reasoning": "...",
  "summary": "..."
}}
"""
