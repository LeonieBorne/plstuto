# CCA/PLS tutorials in Python
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-9-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
***Tutorials to apply cross decomposition methods in Python (focus on application in neuroimaging)***

## Welcome!

First of all, welcome! If you're here, it's because we probably have one thing in common: you're ~~incredibly smart~~ interested in using cross-decomposition algorithms (e.g. Canonical Correlation Analysis - CCA, Partial Least Square - PLS, etc.).

This project has been proposed during the [OHBM Hackathon 2020](https://ohbm.github.io/hackathon2020/) and gather a set of tutorials to help the application of these methods (especially in neuroscience).

## Get started

### Install dependencies
```
pip install -r requirements.txt
```

### Tutorials

Cross decomposition algorithms look for the relations between two (or more) blocks of variables. These methods are particularly used in neuroimaging to analyze associations between physiological/behavioral variables and brain structure/function.
Between unsupervised and supervised modeling, this family of algorithms has many members (e.g. CCA, PLS regression, PLS canonical, PLS-PM, etc.) and many approaches are possible to validate the trained model (e.g. cross validation, bootstrapping, permutation test, etc.).
Here, we propose several Python tutorials to help the application and interpretation of these models in practice.

- [Tutorial: Introduction](tutorials/introduction.ipynb) This tutorial explains the general principles of cross-decomposition algorithms, their possible applications and practical considerations. It also give an overview of the different cross-decomposition algorithms that exist, including CCA, PLS regression, PLS canonical and PLS-PM.
- [Tutorial: Data simulation](tutorials/cca_data_simulation.ipynb) This tutorial simulates data with different underlying structures and allow to see how this affects CCA results. This is an important step in understanding the usefulness and meaning of the method.
- Tutorial: Data preprocessing *work in progress*
- Tutorial: Data reduction *work in progress*
- Tutorial: Model selection *work in progress*

## Please help us to complete this set of tutorials!

### Who are we?

This project brings together a group of collaborators (neuroscientists participating to the 2020 OHBM Hackathon) interested in this issue and you are very welcome to join us!

### How can you get involved?

In order to help the development of this project, please check out the [contributors' guidelines](CONTRIBUTING.md) and the [roadmap](../../issues/3).

### Contact us

If you want to report a problem or suggest an enhancement we'd love for you to [open an issue](../../issues) at this github repository because then we can get right on it. But you can also contact [Léonie Borne](https://www.newcastle.edu.au/profile/leonie-borne-749) by email (leonie.borne AT gmail DOT com) or on [twitter](https://twitter.com/LeonieBorne).

### Find out more
You might be interested in:

* [Initial project proposition](https://github.com/ohbm/hackathon2020/issues/149)
* [Roadmap](../../issues/3)
* [Contributors' guidelines](CONTRIBUTING.md)
* [Kanban board for OHBM Hackathon 2020](https://github.com/LeonieBorne/plstuto/projects/1)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/LeonieBorne"><img src="https://avatars0.githubusercontent.com/u/19991748?v=4" width="100px;" alt=""/><br /><sub><b>Léonie Borne</b></sub></a><br /><a href="#design-LeonieBorne" title="Design">🎨</a> <a href="https://github.com/LeonieBorne/plstuto/commits?author=LeonieBorne" title="Code">💻</a> <a href="#tutorial-LeonieBorne" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://wanghaoting.com/"><img src="https://avatars3.githubusercontent.com/u/13743617?v=4" width="100px;" alt=""/><br /><sub><b>Hao-Ting Wang</b></sub></a><br /><a href="#ideas-htwangtw" title="Ideas, Planning, & Feedback">🤔</a> <a href="#question-htwangtw" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/likeajumprope"><img src="https://avatars0.githubusercontent.com/u/23728822?v=4" width="100px;" alt=""/><br /><sub><b>Johanna Bayer</b></sub></a><br /><a href="#ideas-likeajumprope" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/LeonieBorne/plstuto/commits?author=likeajumprope" title="Code">💻</a> <a href="#tutorial-likeajumprope" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/diiobo"><img src="https://avatars3.githubusercontent.com/u/32033439?v=4" width="100px;" alt=""/><br /><sub><b>diiobo</b></sub></a><br /><a href="#ideas-diiobo" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/LeonieBorne/plstuto/commits?author=diiobo" title="Code">💻</a> <a href="#tutorial-diiobo" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/nadinespy"><img src="https://avatars0.githubusercontent.com/u/46372572?v=4" width="100px;" alt=""/><br /><sub><b>nadinespy</b></sub></a><br /><a href="#ideas-nadinespy" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/LeonieBorne/plstuto/commits?author=nadinespy" title="Code">💻</a> <a href="#tutorial-nadinespy" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/IsabellaBreukelaar"><img src="https://avatars2.githubusercontent.com/u/16314387?v=4" width="100px;" alt=""/><br /><sub><b>IsabellaBreukelaar</b></sub></a><br /><a href="#ideas-IsabellaBreukelaar" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/LeonieBorne/plstuto/commits?author=IsabellaBreukelaar" title="Documentation">📖</a> <a href="#tutorial-IsabellaBreukelaar" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/SaraMorsy"><img src="https://avatars2.githubusercontent.com/u/41592024?v=4" width="100px;" alt=""/><br /><sub><b>SaraMorsy</b></sub></a><br /><a href="#ideas-SaraMorsy" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/LeonieBorne/plstuto/pulls?q=is%3Apr+reviewed-by%3ASaraMorsy" title="Reviewed Pull Requests">👀</a> <a href="#example-SaraMorsy" title="Examples">💡</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/fBeyer89"><img src="https://avatars2.githubusercontent.com/u/9799829?v=4" width="100px;" alt=""/><br /><sub><b>fBeyer89</b></sub></a><br /><a href="#ideas-fBeyer89" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://orcid.org/0000-0003-4652-3758"><img src="https://avatars1.githubusercontent.com/u/7570456?v=4" width="100px;" alt=""/><br /><sub><b>Sin Kim</b></sub></a><br /><a href="#ideas-AKSoo" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/LeonieBorne/plstuto/commits?author=AKSoo" title="Documentation">📖</a> <a href="#tutorial-AKSoo" title="Tutorials">✅</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
