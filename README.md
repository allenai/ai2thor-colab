<p align="center"><img width="80%" src="doc/static/cover.svg" /></p>

<h2 align="center"><em>Run AI2-THOR on the Cloud using Google Colab</em></h2>

<p align="center">
    <a href="//github.com/allenai/ai2thor/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/allenai/ai2thor.svg?color=blue">
    </a>
    <a href="https://colab.research.google.com/drive/1VyvpUahrlakrlwebuuFZl73ioqCuVF33?usp=sharing" target="_blank">
        <img src="https://img.shields.io/badge/colab-template-orange">
    </a>
    <a href="https://ai2thor.allenai.org/" target="_blank">
        <img src="https://img.shields.io/badge/ai2thor-website-blue">
    </a>
    <a href="https://github.com/allenai/ai2thor" target="_blank">
        <img src="https://img.shields.io/badge/ai2thor-github-green">
    </a>
</p>

## 💡 Templates

#### 💪 Full Starter Template

<a href="https://colab.research.google.com/github/allenai/ai2thor-colab/blob/main/templates/AI2_THOR_Full_Starter_Template.ipynb">
    <img src="/doc/static/full-starter-template.svg" />
</a>

To get started, we recommend saving a copy of the <a href="https://colab.research.google.com/github/allenai/ai2thor-colab/blob/main/templates/AI2_THOR_Full_Starter_Template.ipynb" target="_blank">AI2-THOR Colab Full Starter Template</a> to your drive. It goes over many helper functions that are often useful.

<br/>

https://user-images.githubusercontent.com/28768645/119420726-06d8bc80-bcb2-11eb-9acf-e9b151121506.mp4

<br/>

#### 👑 Minimal Starter Template

<a href="https://colab.research.google.com/drive/1dCxcvgpj1VKkn9X2_8Zdg9kL1QkzHYA1?usp=sharing">
    <img src="/doc/static/minimal-starter-template.svg" />
</a>

We also provide a <a href="https://colab.research.google.com/drive/1VyvpUahrlakrlwebuuFZl73ioqCuVF33?usp=sharing" target="_blank">Minimal Starter Template</a> that does not showcase any helper functions. This is often useful as a starting point to minimally reproduce issues, highlight, or test functionality.

<br/>

![image](https://user-images.githubusercontent.com/28768645/119420252-e5c39c00-bcb0-11eb-84d8-98ed862a687b.png)

<br/>

## 🐱‍💻 Setup Overview

#### 💻 Installation

Using Python's packaging manager, `ai2thor_colab` can be installed with

```python
pip install ai2thor_colab
```

#### 🔥 Start X Server

AI2-THOR requires an X Server to run on a Linux machine. It allows us to open a Unity window where we can render scenes and observe images. Colab runs Linux, but it does not start an X Server by default. Using `ai2thor_colab.start_xserver()`, we can install all required X Server dependencies and start it up:

```python
import ai2thor_colab
ai2thor_colab.start_xserver()
```

## 💬 Support

**Questions.** If you have any questions on AI2-THOR, please ask them on [AI2-THOR's GitHub Discussions Page](https://github.com/allenai/ai2thor/discussions).

**Issues.** If you encounter any issues while using AI2-THOR, please open an [Issue on AI2-THOR's GitHub](https://github.com/allenai/ai2thor/issues). If you encounter an issue with AI2-THOR Colab, please open an [Issue on our GitHub](https://github.com/allenai/ai2thor-colab/issues)

## 🏫 Learn more

| Section | Description |
| :-- | :-- |
| [AI2-THOR Website](https://ai2thor.allenai.org/) | The AI2-THOR website, which contains extensive documentation on using the API. |
| [AI2-THOR GitHub](https://github.com/allenai/ai2thor) | Contains the source code and development of AI2-THOR. |
| [AI2-THOR Demo](https://ai2thor.allenai.org/demo/) | Interact and play with AI2-THOR live in the browser. |

## 👋 Our Team

AI2-THOR and AI2-THOR Colab are open-source projects built by the [PRIOR team](//prior.allenai.org) at the [Allen Institute for AI](//allenai.org) (AI2).
AI2 is a non-profit institute with the mission to contribute to humanity through high-impact AI research and engineering.

<br />

<a href="//prior.allenai.org">
<p align="center"><img width="100%" src="https://raw.githubusercontent.com/allenai/ai2thor/main/doc/static/ai2-prior.svg" /></p>
</a>
