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

My name is Wenhao Zheng (郑文浩) and I am currently a master's student in the Computer Science department at Zhejiang University, supervised by [Prof. Jian Wu](https://person.zju.edu.cn/0004274). Before that, I graduated with a B.E. degree in Computer Science and Technology from Chu Kochen Honors College at Zhejiang University.

My current research interest primarily includes **<span style="color:#73E87A">Computer Vision (CV)</span>**, **<span style="color:#76AFE5">Natural Language Processing (NLP)</span>** based on LLMs and **<span style="color:#76E5D2">Multi-Modal Learning (MML)</span>** involving Vision and Language modalities, especially for **<span style="color:#E57694">Healthcare (AI4H)</span>**. Specifically, I have published several papers <a href='https://scholar.google.com/citations?user=dR1J_4EAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> on the following topics:

- Tabular data prediction and text classification based on LLM[**<span style="color:#76AFE5">NLP</span>**].
- Weakly-supervised instance segmentation on medical images[**<span style="color:#73E87A">CV</span>**, **<span style="color:#E57694">AI4H</span>**].
- Object detection with multiple modalities for healthcare[**<span style="color:#73E87A">CV</span>**, **<span style="color:#76E5D2">MML</span>**, **<span style="color:#E57694">AI4H</span>**].
- Image classification with ordinal regression and generation for healthcare[**<span style="color:#73E87A">CV</span>**, **<span style="color:#E57694">AI4H</span>**].

In addition, I am also interested in the following topics:

- High-performance AI systems, including AI chips, operators in AI framework and performance optimization in distributed training.
- Reinforcement learning, especially for the application in LLM and games, such as StarCraft II.
- Physics, physical simulation and physics-guided learning.
- Any interesting technical topics in computer science, physics and finance I am not familiar with now.

In my spare time, I also enjoy writing some helpful and interesting tools for research and daily life. You can find them on my [GitHub](https://github.com/shenmishajing).

# 🔥 News

- *2023.12*: 🎉 One [paper](https://ieeexplore.ieee.org/document/10354298) was accepted by JBHI. 
- *2023.10*: 🎉 One [paper](https://ieeexplore.ieee.org/document/10294274) was accepted by TMI. 
- *2023.01*: 🔥 A helpful [library](https://github.com/shenmishajing/lightning_template) with a collection of tools wrapped on [pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) was released. 
- *2022.05*: 🎉 One [paper](https://ieeexplore.ieee.org/document/9784879) was accepted by TCBB. 
- *2022.03*: 🎉 One [paper](https://ieeexplore.ieee.org/document/9744114) was accepted by TMI. 

# 📝 Publications 

<span style="color:blue">($\dagger$: Equal contribution; $^\*$: Corresponding author(s))</span>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">JBHI</div><img src='images/papers/2023jbhi_segment_by_rotate_detection.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
It is the first work to propose a bespoke approach, called PAL, for instance segmentation of convex objects, leveraging the convex shapes of biomedical targets to generate the profile (i.e., masks) with bounding boxes. PAL outperforms other box-supervised models (e.g., BoxInst), and achieves comparable performance with mask-supervised models including Mask R-CNN and Cascade Mask R-CNN, on convex object instance segmentation tasks. In addition, we show that PAL demonstrates promising performance even for non-convex objects in practical applications.
</div>
<div markdown="1">
[Polygonal Approximation Learning for Convex Object Segmentation in Biomedical Images with Bounding Box Supervision](https://ieeexplore.ieee.org/document/10354298)[**<span style="color:#73E87A">CV</span>**, **<span style="color:#E57694">AI4H</span>**], **Wenhao Zheng**, Jintai Chen, Kai Zhang, Jiahuan Yan, Jinhong Wang, Yi Cheng, Bang Du, Danny Z. Chen, Honghao Gao$^\*$, Jian Wu, Hongxia Xu$^\*$, **IEEE Journal of Biomedical and Health Informatics**, 2023.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TMI</div><img src='images/papers/2022TMI_task_decomposing_cell_comparing_for_cervical_lesion_cell_detection.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
We propose a novel task-decomposing and cell-comparing framework for cervical lesion cell detection. The original detection task is decomposed into two detection subtasks first and a decompose-and-integrate head is introduced to model those tasks encouraging the network to focus on specific cell structures. In addition, cell comparison is performed by introducing a dynamic comparing module and an instance contrastive loss for both normal-abnormal and abnormal-abnormal cells comparison, enhancing the ability of the model to distinguish different kinds of lesion cells.
</div>
<div markdown="1">
[A Task Decomposing and Cell Comparing Method for Cervical Lesion Cell Detection](https://ieeexplore.ieee.org/document/9744114)[**<span style="color:#73E87A">CV</span>**, **<span style="color:#76E5D2">MML</span>**, **<span style="color:#E57694">AI4H</span>**], Tingting Chen$^\dagger$, **Wenhao Zheng$^\dagger$**, Haochao Ying, Xiangyu Tan, Kexin Li, Xiaoping Li, Danny Z. Chen, Jian Wu$^\*$, **IEEE Transactions on Medical Imaging**, 2022.
</div>
</div>

- [A Transformer-based Knowledge DistillationNetwork for Cortical Cataract Grading](https://ieeexplore.ieee.org/document/10294274)[**<span style="color:#73E87A">CV</span>**, **<span style="color:#E57694">AI4H</span>**], Jinhong Wang$^\dagger$, Zhe Xu$^\dagger$, **Wenhao Zheng$^\dagger$**, Haochao Ying$^\*$, Tingting Chen, Zuozhu Liu, Danny Z. Chen, Ke Yao$^\*$, Jian Wu. **IEEE Transactions on Medical Imaging**, 2023.
- [Robust Image Ordinal Regression with Controllable Image Generation](https://arxiv.org/abs/2305.04213)[**<span style="color:#73E87A">CV</span>**], Yi Cheng, Haochao Ying$^\*$, Renjun Hu, Jinhong Wang, **Wenhao Zheng**, Xiao Zhang, Danny Z. Chen, Jian Wu, **International Joint Conference on Artificial Intelligence**, 2023.
- [A Corresponding Region Fusion Framework for Multi-modal Cervical Lesion Detection](https://ieeexplore.ieee.org/document/9784879)[**<span style="color:#73E87A">CV</span>**, **<span style="color:#76E5D2">MML</span>**, **<span style="color:#E57694">AI4H</span>**], Tingting Chen, **Wenhao Zheng**, Heping Hu, Chunhua Luo, Jintai Chen, Chunnv Yuan, Weiguo Lu, Danny Z. Chen, Honghao Gao$^\*$ and Jian Wu$^\*$, **IEEE/ACM Transactions on Computational Biology and Bioinformatics**, 2022.
- [CTT-Net: A Multi-view Cross-token Transformer for Cataract Postoperative Visual Acuity Prediction](https://ieeexplore.ieee.org/document/9995392)[**<span style="color:#73E87A">CV</span>**, **<span style="color:#E57694">AI4H</span>**], Jinhong Wang$^\dagger$, Jingwen Wang$^\dagger$, Tingting Chen, **Wenhao Zheng**, Zhe Xu, Xingdi Wu, Wen Xu$^\*$, Haochao Ying$^\*$, Danny Z. Chen, and Jian Wu, **IEEE International Conference on Bioinformatics and Biomedicine**, 2022.
- [Automating Blastocyst Formation and Quality Prediction in Time-Lapse Imaging with Adaptive Key Frame Selection](https://link.springer.com/chapter/10.1007/978-3-031-16440-8_43)[**<span style="color:#73E87A">CV</span>**, **<span style="color:#E57694">AI4H</span>**], Tingting Chen$^\dagger$, Yi Cheng$^\dagger$, Jinhong Wang, Zhaoxia Yang, **Wenhao Zheng**, Danny Z. Chen, and Jian Wu$^\*$, **Medical Image Computing and Computer Assisted Intervention**, 2022.

# 🎖 Honors and Awards

- *2022.11* Zhijun He Scholarship, Zhejiang University
- *2022.10* First Class Academic Excellence Scholarship, Zhejiang University
- *2019.08* 1$^{st}$ Prize in The 12$^{th}$ World Robotics Sailing Championship(WRSC)

# 📖 Educations
- *2021.09 - now*, M.E. in Software Engineering, College of Computer Science and Technology, Zhejiang University.
- *2017.09 - 2021.06*, B.E. in Computer Science and Technology, Chu Kochen Honors College, Zhejiang University.
