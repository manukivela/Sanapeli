
<div id="top"></div>




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/manukivela/sanapeli">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">Sanapeli</h3>

  <p align="center">
    Finnish Wordle-like game, coded in Python.
    <br />
    <a href="https://github.com/manukivela/sanapeli"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/manukivela/sanapeli">View Demo</a>
    ·
    <a href="https://github.com/manukivela/sanapeli/issues">Report Bug</a>
    ·
    <a href="https://github.com/manukivela/sanapeli/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#screenshots">Screenshots</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

One slow day at my job as a salesman in a consumer electronics store we were playing Wordle with my colleagues. I bet them I could code a similar game. I installed VScode on one of the Macs on display and started coding.

I soon had a working version which I kept working on every now and then.

First I added a point system so we could keep track who's in the lead. Game asked players name and would increase or decrease points depending on the results. To no ones surprise players soon started to sabotage each other by using each others names and losing games on purpose. At this point the score could go to negatives and boy did they ever.

After resetting the leaderboards I created a simple account system. Also the points won't go in the negatives anymore.

Most competitive players were not happy with the slow point gathering, so I added an betting system. First you could bet as much points as you had, which led into exponential point growth. After resetting the leaderboards once again, I set 500 point maximum bet limit.

Next thing I noticed is that Finnish language has some weird words. Now after finishing a game, the meaning of the word is fetched from dictionary. The site I'm using sometimes has an ad that messes this print up, but it works most of the time.

That's about it! 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3
* pip
* virtualenv (optional)


### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/manukivela/sanapeli.git
   cd /PATH/TO/sanapeli/
   ```
2. (Optional but recommended) Create and activate virtual environment
   ```sh
   virtualenv venv
   source venv/bin/activate
   ```
3. Install required libraries
   ```sh
   pip3 install -r requirements.txt
   ```
4. Run the game
   ```sh
   python3 sanapeli.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Screenshots

![Login screen][login-screenshot]
Login screen

![Main menu][menu-screenshot]
Main menu

![Ingame][product-screenshot]
In game

![Leaderboard][leaderboard-screenshot]
Leaderboard

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/manukivela/sanapeli/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

 -->

<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 
<p align="right">(<a href="#top">back to top</a>)</p>-->




<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- CONTACT -->
## Contact

Manu Kivelä -  manu.kivela@student.samk.fi

Project Link: [https://github.com/manukivela/sanapeli](https://github.com/manukivela/sanapeli)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/manukivela/sanapeli.svg?style=for-the-badge
[contributors-url]: https://github.com/manukivela/sanapeli/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/manukivela/sanapeli.svg?style=for-the-badge
[forks-url]: https://github.com/manukivela/sanapeli/network/members
[stars-shield]: https://img.shields.io/github/stars/manukivela/sanapeli.svg?style=for-the-badge
[stars-url]: https://github.com/manukivela/sanapeli/stargazers
[issues-shield]: https://img.shields.io/github/issues/manukivela/sanapeli.svg?style=for-the-badge
[issues-url]: https://github.com/manukivela/sanapeli/issues
[license-shield]: https://img.shields.io/github/license/manukivela/sanapeli.svg?style=for-the-badge
[license-url]: https://github.com/manukivela/sanapeli/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/manu-kivelä-a034301b9/
[product-screenshot]: screenshots/ss_game.png
[login-screenshot]: screenshots/ss_login.png
[menu-screenshot]: screenshots/ss_menu.png
[leaderboard-screenshot]: screenshots/ss_leaderboard.png