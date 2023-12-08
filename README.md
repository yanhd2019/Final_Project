# Econimate
<p align="center">
  <img src="EconimateR/static/Econimate_logo.png" width="388">
</p>


<h3 align="center">ECONIMATE</h3>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Have you ever tried to dive into the world of economics, only to find yourself overwhelmed by the countless graphs and complex notes? Well, don't worry! Meet Econimate, your friendly AI tutor that makes learning economic concepts a breeze. Whether you're a student, a professional, or simply curious about the world of economics, Econimate is here to help you grasp these concepts in a fun and easy-to-understand manner through engaging and informative videos.
This release builds upon the previous version that utilized Google PALM2 ([Our previous project](https://github.com/yanhd2019/GoogleHackathon)), introducing some advancements. It enhances overall performance and content by incorporating the advanced GPT-4.0 Turbo model. Additionally, a user-friendly UI has been implemented to elevate the overall user experience. 


<!-- GETTING STARTED -->
## Getting Started


### Importing Libraries

1. Follow the requirements.txt to install the packages needed for running Econimate and import necessary modules.

   ```js
    import openai
    from openai import OpenAI
    import gtts
    import moviepy.editor as mpy
    import cv2
    import matplotlib.pyplot as plt
    import os
    from gtts import gTTS
    from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, \
    ImageClip, ColorClip, AudioFileClip, vfx
    import numpy as np
    import shutil
    import pandas as pd
    import subprocess
    import sys
   ```
   
3. We utilized GPT-4.0 Turbo to assist in generating both the explanation and the code for creating a reference graph. To access the GPT-4.0 Turbo API, you can obtain an API_KEY from [here](https://platform.openai.com/api-keys).


   ```js
    copenai.api_key = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use Econimate, simply run the provided code in your local Python environment and enter your Economics doubts on the prompt and press "ASK". Econimate will then return a video that explains the concept in a clear and concise way, using graphs and audio to make your learning easy and fun.

Have a look at how the webpage looks like:

![WhatsApp 이미지 2023-12-03, 16 51 41_946a3f92](https://github.com/yanhd2019/Final_Project/assets/48376588/3c80017f-d253-48a5-aad3-8f40e870bfd0)

Have a look at how amazing videos Econimate generates:

https://github.com/yanhd2019/GoogleHackathon/assets/149416928/68382afd-158e-41e1-93e0-fe67ab864576

Here are some examples of how you can use Econimate:
1. To learn about a new economic concept, such as inflation or supply and demand.
2. To get help with a specific economics assignment or problem.
3. To stay up-to-date on the latest economic news and research.

Econimate is a great resource for anyone who wants to learn more about economics, regardless of the level of expertise. However, please keep in mind that it is still in beta and may not be able to answer all queries perfectly. So, please be patient and understanding as we continue to develop and improve Econimate.

An example of potential usage can be seen in [this video](new_video_link).


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Limitations and Future Plans

Here are some known problems and limitations of the project that we strive to resolve in future implementations:

Econimate currently faces a notable limitation in its extended time required for video generation, taking 4 or 7minutes due to local model execution variations in user computing power. To address this, a migration to a cloud server is planned to enhance computing capabilityies and ensure quicker and more consistent video generation. It will also allow Econimate to accomodate multiple simulateneous users as well. 

Future plans involve transforming Econimate into a mobile Application for broader accessibility, expanding its scope to cover various subjects, and enabling multilingual support for a more diverse user base. 

<!-- ROADMAP -->
## Roadmap

At present, we've set up a process where you can ask your economics questions from our website which runs on a local environment. In response, you'll receive a video providing answers, which will be displayed directly on the website. You can check out the steps Econimate have followed in the diagram below, and you can access the code to see how it all works. 
<p align="center">
  <img src="/roadmap.png">
</p>


This is the steps we've followed to develop the website:

<p align="center">
  <img src="/website implementation.png">
</p>

A pivotal milestone in reaching this stage involved training the GPT 4.0 Turbo API using our prompts. If you're interested in seeing how this was accomplished, you can access the [video](new_video_link) that demonstrates the process. It's a great way to gain insight into the behind-the-scenes work that contributes to the chatbot's performance.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Created with ❤️ by:
<ol>
<li> Haodong Yan - hyan3@andrew.cmu.edu (Technical Integration) </li>
<li> Sewon Hong - sewonh@andrew.cmu.edu (Technical Integration) </li>
<li> Yuchen Zhu - yzhu7@andrew.cmu.edu  (AI Training) </li>
<li> Jiayuan Ye - jye3@andrew.cmu.edu   (Prompt Engineering) </li>
<li> Yukta Butala - ybutala@andrew.cmu.edu (Report Writing) </li>
</ol>
We are excited to continue this project for the rest of our Experiential Learning Programme.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

In our journey through this hackathon, we've received invaluable support and guidance from some remarkable individuals. Special gratitude goes out to Josh Gordon for his invaluable introduction to the Palm2 API, which played a pivotal role in our project. We also want to express our appreciation to the entire Google team for their dedicated guidance and mentorship over the past week. We would like to extend our heartfelt thanks to Prof. Ganesh Mani for his unwavering support and encouragement. Your collective efforts and insights have been instrumental in our success. Thank you all for your contributions to this incredible experience!


<p align="right">(<a href="#readme-top">back to top</a>)</p>
