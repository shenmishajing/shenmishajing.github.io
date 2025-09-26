---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

My name is Wenhao Zheng (郑文浩). I am currently a PhD student at The University of North Carolina at Chapel Hill majoring in Computer Science, supervised by Prof. [Huaxiu Yao](https://www.huaxiuyao.io/). Before that, I graduated as a master's student in the Computer Science department at Zhejiang University, supervised by Prof. [Jian Wu](https://person.zju.edu.cn/0004274) in 2024 and graduated with a B.E. degree in Computer Science and Technology from Chu Kochen Honors College at Zhejiang University in 2021.

My current research interest primarily includes two frontiers of Large Language Models (LLMs): **LLM Agent** and **LLM Inference Acceleration**.

Regarding **LLM Agent**, I focus on exploring and enhancing the capabilities and endurance of agents in long-horizon tasks. My research includes:
* **Constructing Benchmarks**: To address the limitations of existing benchmarks, which often rely on human-crafted tasks requiring only a few, fixed-sequence tool invocations, we have proposed and developed a novel framework to programmatically generate benchmarks of arbitrary length and complexity. This enables a more rigorous evaluation of agent capabilities in extended interaction scenarios.
* **Designing and Evaluating Agent Frameworks**: I am also interested in designing agent frameworks that can learn from verifiable domains (e.g., mathematics, code generation) and apply that knowledge to unverifiable ones. This involves training an "agent-judge" to assess the quality of complex outputs and generate reward signals for new, unverifiable tasks.
* **Enhancing Foundation Models for Agentic Tasks**: Explore how to leverage the data and insights from these benchmarks to improve the reasoning and execution abilities of foundation models, enabling them to handle more complex agent tasks.

In the area of **LLM Inference Acceleration**, my research focuses on co-designing systems and algorithms to boost LLM inference efficiency, especially for multi-turn interactive scenarios like Agents. This includes:
* **Collaborative Inference between Large and Small Models**: I have designed collaborative inference systems, such as CITER, that use token-level routing to distribute the computational load between edge devices and cloud-based large models, significantly reducing inference cost and latency.
* **Efficient Attention Operators and Inference Systems**: I'm also working on building more efficient computational operators and inference systems to tackle the challenges posed by multi-turn interactions in Agent-based applications.

Additionally, my research interests also include **Multi-Modal Learning**, **Computer Vision (CV)**, and **AI for Healthcare (AI4H)**. You can find more about my work on my [Google Scholar](https://scholar.google.com/citations?user=dR1J_4EAAAAJ) <a href='https://scholar.google.com/citations?user=dR1J_4EAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> and [GitHub](https://github.com/shenmishajing).

<!-- My current research interest primarily includes **<span style="color:#73E87A">Computer Vision (CV)</span>**, **<span style="color:#76AFE5">Natural Language Processing (NLP)</span>** based on LLMs and **<span style="color:#76E5D2">Multi-Modal Learning (MML)</span>** involving Vision and Language modalities, especially for **<span style="color:#E57694">Healthcare (AI4H)</span>**. Specifically, I have published several papers <a href='https://scholar.google.com/citations?user=dR1J_4EAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> on the following topics:

- Tabular data prediction and text classification based on LLM[**<span style="color:#76AFE5">NLP</span>**].
- Weakly-supervised instance segmentation on medical images[**<span style="color:#73E87A">CV</span>**, **<span style="color:#E57694">AI4H</span>**].
- Object detection with multiple modalities for healthcare[**<span style="color:#73E87A">CV</span>**, **<span style="color:#76E5D2">MML</span>**, **<span style="color:#E57694">AI4H</span>**].
- Image classification with ordinal regression and generation for healthcare[**<span style="color:#73E87A">CV</span>**, **<span style="color:#E57694">AI4H</span>**].

In addition, I am also interested in the following topics:

- High-performance AI systems, including AI chips, operators in AI framework and performance optimization in distributed training.
- Reinforcement learning, especially for the application in LLM and games, such as StarCraft II.
- Physics, physical simulation and physics-guided learning.
- Any interesting technical topics in computer science, physics and finance I am not familiar with now.

In my spare time, I also enjoy writing some helpful and interesting tools for research and daily life. You can find them on my [GitHub](https://github.com/shenmishajing). -->

<!-- # 🔥 News

- *2024.02*: 🎉 One [paper](https://arxiv.org/abs/2402.06512) was released on arXiv. 
- *2023.12*: 🎉 One [paper](https://ieeexplore.ieee.org/document/10354298) was accepted by JBHI. 
- *2023.10*: 🎉 One [paper](https://ieeexplore.ieee.org/document/10294274) was accepted by TMI. 
- *2023.01*: 🔥 A helpful [library](https://github.com/shenmishajing/lightning_template) with a collection of tools wrapped on [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) was released. 
- *2022.05*: 🎉 One [paper](https://ieeexplore.ieee.org/document/9784879) was accepted by TCBB. 
- *2022.03*: 🎉 One [paper](https://ieeexplore.ieee.org/document/9744114) was accepted by TMI.  -->

# 📖 Educations

<!-- AUTO_EDUCATION_START -->
- *Sep. 2024 - May. 2029$^*$*, PhD. of Computer Science, Department of Computer Science, The University of North Carolina at Chapel Hill, Chapel Hill
- *Sep. 2021 - Jun. 2024*, Master of Software Engineering, College of Computer Science and Technology, Zhejiang University, Hangzhou
- *Sep. 2017 - Jun. 2021*, Bachelor of Computer Science, Chu Kochen Honors College, Zhejiang University, Hangzhou
<!-- AUTO_EDUCATION_END -->

# 📝 Selected Publications (Full list on [Google Scholar](https://scholar.google.com/citations?user=dR1J_4EAAAAJ))

<span style="color:blue">($^\dagger$: Equal contribution; $^*$: Corresponding author(s))</span>

<!-- AUTO_PUBLICATIONS_START -->
- **Wenhao Zheng**, Xinyu Ye, Peng Xia, Fang Wu, Linjie Li, Weitong Zhang, Lijuan Wang, Yejin Choi, Yun Li, Huaxiu Yao$^*$. "The Agent's Marathon: Probing the Limits of Endurance in Long-Horizon Tasks," **The International Conference on Learning Representations**, 2026, under review.
- **Wenhao Zheng**, Jianshu She, Weitong Zhang, Yixiao Chen, Leshang Chen, Souvik Kundu, Eric P. Xing, Zhengzhong Liu, Qirong Ho, Hongyi Wang, Yun Li, Huaxiu Yao$^*$. "CLEAR: A Cost-Aware Routing System for Edge-Cloud Language Model Collaborative Inference," **The International Conference on Learning Representations**, 2026, under review.
- **Wenhao Zheng$^\dagger$**, Yixiao Chen$^\dagger$, Weitong Zhang, Souvik Kundu, Yun Li, Zhengzhong Liu, Eric P. Xing, Hongyi Wang, Huaxiu Yao$^*$. "CITER: Collaborative Inference for Efficient Large Language Model Decoding with Token-Level Routing," **Conference on Language Modeling**, 2025. [[Link]](https://openreview.net/forum?id=nqX9UYW9Af)
- **Wenhao Zheng$^\dagger$**, Liaoyaqi Wang$^\dagger$, Dongsheng Peng, Hongxia Xu, Hongtu Zhu, Tianfan Fu, Huaxiu Yao$^*$. "LIFTED: Multimodal Clinical Trial Outcome Prediction via Large Language Models and Mixture-of-Experts," **The Conference on Empirical Methods in Natural Language Processing**, 2025. [[Link]](https://openreview.net/forum?id=HS4XgL5JyP)
- Jianshu She, **Wenhao Zheng**, Zhengzhong Liu, Hongyi Wang, Eric Xing, Huaxiu Yao, Qirong Ho$^*$. "Token Level Routing Inference System for Edge Devices," **Annual Meeting of the Association for Computational Linguistics**, 2025. [[Link]](https://aclanthology.org/2025.acl-demo.16/)
- Zhaoyang Wang, Jinqi Jiang, Huichi Zhou, **Wenhao Zheng**, Xuchao Zhang, Chetan Bansal, Huaxiu Yao$^*$. "Verifiable Format Control for Large Language Model Generations," **Annual Meeting of the Association for Computational Linguistics**, 2025. [[Link]](https://aclanthology.org/2025.findings-naacl.194/)
- Peng Xia$^\dagger$, Siwei Han$^\dagger$, Shi Qiu$^\dagger$, Yiyang Zhou, Zhaoyang Wang, **Wenhao Zheng**, Zhaorun Chen, Chenhang Cui, Mingyu Ding, Linjie Li, Lijuan Wang, Huaxiu Yao$^*$, Tingting Chen, Zuozhu Liu, Danny Z. Chen, Ke Yao$^*$. "MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models," **International Conference on Learning Representations**, 2025. [[Link]](https://openreview.net/forum?id=HnhNRrLPwm)
- Yiyang Zhou, Zhaoyang Wang, Tianle Wang, Shangyu Xing, Peng Xia, Bo Li, Kaiyuan Zheng, Zijian Zhang, Zhaorun Chen, **Wenhao Zheng**, Xuchao Zhang, Chetan Bansal, Weitong Zhang, Ying Wei, Mohit Bansal, Huaxiu Yao$^*$. "AnyPrefer: An Automatic Framework for Preference Data Synthesis," **International Conference on Learning Representations**, 2025. [[Link]](https://openreview.net/forum?id=WpZyPk79Fu)
- Tony Lee$^\dagger$, Haoqin Tu$^\dagger$, Chi Heem Wong$^\dagger$, **Wenhao Zheng**, Yiyang Zhou, Yifan Mai, Josselin Somerville Roberts, Michihiro Yasunaga, Huaxiu Yao, Cihang Xie, Percy Liang$^*$. "VHELM: A Holistic Evaluation of Vision Language Models," **Conference on Neural Information Processing Systems**, 2024. [[Link]](https://crfm.stanford.edu/helm/vhelm/latest/)
- Peng Xia$^\dagger$, Ming Hu$^\dagger$, Feilong Tang, Wenxue Li, **Wenhao Zheng**, Lie Ju, Peibo Duan, Huaxiu Yao$^*$, Zongyuan Ge$^*$. "Generalizing to Unseen Domains in Diabetic Retinopathy with Disentangled Representations," **Medical Image Computing and Computer Assisted Intervention**, 2024. [[Link]](https://link.springer.com/chapter/10.1007/978-3-031-72117-5_40)
- Peng Xia, Ze Chen, Juanxi Tian$^\dagger$, Yangrui Gong$^\dagger$, Ruibo Hou, Yue Xu, Zhenbang Wu, Zhiyuan Fan, Yiyang Zhou, Kangyu Zhu, **Wenhao Zheng**, Zhaoyang Wang, Xiao Wang, Xuchao Zhang, Chetan Bansal, Marc Niethammer, Junzhou Huang, Hongtu Zhu, Yun Li, Jimeng Sun, Zongyuan Ge$^*$, Gang Li, James Zou, Huaxiu Yao$^*$. "CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models," **Conference on Neural Information Processing Systems**, 2024. [[Link]](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Wenhao Zheng**, Jintai Chen, Kai Zhang, Jiahuan Yan, Jinhong Wang, Yi Cheng, Bang Du, Danny Z. Chen, Honghao Gao$^*$, Jian Wu, Hongxia Xu$^*$. "Polygonal Approximation Learning for Convex Object Segmentation in Biomedical Images with Bounding Box Supervision," **IEEE Journal of Biomedical and Health Informatics**, 2023. [[Link]](https://ieeexplore.ieee.org/document/10354298)
- Jinhong Wang$^\dagger$, Zhe Xu$^\dagger$, **Wenhao Zheng$^\dagger$**, Haochao Ying$^*$, Tingting Chen, Zuozhu Liu, Danny Z. Chen, Ke Yao$^*$, Jian Wu. "A Transformer-based Knowledge DistillationNetwork for Cortical Cataract Grading," **IEEE Transactions on Medical Imaging**, 2023. [[Link]](https://ieeexplore.ieee.org/abstract/document/10294274)
- Tingting Chen$^\dagger$, **Wenhao Zheng$^\dagger$**, Haochao Ying, Xiangyu Tan, Kexin Li, Xiaoping Li, Danny Z. Chen, Jian Wu$^*$. "A Task Decomposing and Cell Comparing Method for Cervical Lesion Cell Detection," **IEEE Transactions on Medical Imaging**, 2022. [[Link]](https://ieeexplore.ieee.org/document/9744114)
- Yi Cheng, Haochao Ying$^*$, Renjun Hu, Jinhong Wang, **Wenhao Zheng**, Xiao Zhang, Danny Z. Chen, Jian Wu. "Robust Image Ordinal Regression with Controllable Image Generation," **International Joint Conference on Artificial Intelligence**, 2023. [[Link]](https://dl.acm.org/doi/abs/10.24963/ijcai.2023/70)
- Tingting Chen, **Wenhao Zheng**, Heping Hu, Chunhua Luo, Jintai Chen, Chunnv Yuan, Weiguo Lu, Danny Z. Chen, Honghao Gao$^*$ and Jian Wu$^*$. "A Corresponding Region Fusion Framework for Multi-modal Cervical Lesion Detection," **IEEE/ACM Transactions on Computational Biology and Bioinformatics**, 2022. [[Link]](https://ieeexplore.ieee.org/document/9784879)
- Jinhong Wang$^\dagger$, Jingwen Wang$^\dagger$, Tingting Chen, **Wenhao Zheng**, Zhe Xu, Xingdi Wu, Wen Xu$^*$, Haochao Ying$^*$, Danny Z. Chen, and Jian Wu. "CTT-Net: A Multi-view Cross-token Transformer for Cataract Postoperative Visual Acuity Prediction," **IEEE International Conference on Bioinformatics and Biomedicine**, 2022. [[Link]](https://ieeexplore.ieee.org/document/9995392)
- Tingting Chen$^\dagger$, Yi Cheng$^\dagger$, Jinhong Wang, Zhaoxia Yang, **Wenhao Zheng**, Danny Z. Chen, and Jian Wu$^*$. "Automating Blastocyst Formation and Quality Prediction in Time-Lapse Imaging with Adaptive Key Frame Selection," **Medical Image Computing and Computer Assisted Intervention**, 2022. [[Link]](https://link.springer.com/chapter/10.1007/978-3-031-16440-8_43)
<!-- AUTO_PUBLICATIONS_END -->

# 🎖 Honors and Awards

<!-- AUTO_AWARDS_START -->
- *Nov 2022*, **Scholarship**: "Zhijun He Scholarship", Zhejiang University
- *Dec 2022*, **Scholarship**: "First Class Academic Excellence Scholarship", Zhejiang University
- *Oct 2022*, **Honorary Title**: "Miyoshi graduate student", Zhejiang University
- *Oct 2022*, **Honorary Title**: "Outstanding graduate student", Zhejiang University
- *Aug 2019*, **Award**: "1$^\text{st}$ Prize in The 12$^\text{th}$ World Robotics Sailing Championship(WRSC)", Zhejiang University
<!-- AUTO_AWARDS_END -->

## 📈 More statistics

[![](https://github-readme-stats.vercel.app/api?username=shenmishajing&show_icons=true&include_all_commits=true&rank_icon=github)](https://github.com/shenmishajing)
[![](https://github-readme-stats.vercel.app/api/top-langs/?username=shenmishajing&layout=compact&langs_count=8)](https://github.com/shenmishajing)

