<div align="center" id="top">
  <img
    src="https://user-images.githubusercontent.com/64326462/134097233-d1484521-9ee7-4160-832c-c0bd18a1b07d.png"
    alt="Mtrx_Logo"
    style="margin: 0; padding: 0;"
  />
  <p>
    <a href="https://github.com/brlaney/python-matrix-fem/commits/master">
      <img src="https://img.shields.io/github/last-commit/brlaney/python-matrix-fem?style=flat-square">
    </a>
    <a href="#status">
      <img src="https://img.shields.io/badge/Maintained-yes-green.svg?style=flat-square">
    </a>
  </p>
</div>

<div align="center">
  <h1>Python Stiffness Method</h1>
  <p style="text-align: justify">
    A Python program that solves trusses, beams, and frames using the stiffness method.
  </p>
</div>

## Table Of Contents

- [Project summary](#Summary)
- [Project demo](#Demo)
- [Quick start](#quick-start)
  - [1. Clone repository](#1-clone-repository)
  - [2. Install dependencies](#2-install-dependencies)
  - [3. Run example scripts](#3-run-example-scripts)
- [Connect with me](#connect-with-me)
- [References and resources](#references-and-resources)
- [License](#license)
- [Contributions and issues](#contributions-and-issues)

</br>

## Summary

The main goal of this project is to allow the user to understand the [matrix displacement method](https://en.wikipedia.org/wiki/Direct_stiffness_method) by learning visually and interactively. The **matrix displacement method**, or the **stiffness method**, usually requires an understanding of statics and structural mechanics (analysis) - my goal is to make content that is approachable from any level of understanding of these topics.

I am referring to statics and structural analysis within the context of *Civil Engineering*, they are both courses required for [ABET](https://www.abet.org/) accredited Civil Engineering degrees. Regardless if you are a Civil Engineer (or studying to become one), they are interesting and intuitive subjects that are a direct implication of [Newtonian Mechanics](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion). Newton's first law states that `an object at rest will stay at rest` implying that the sum of all forces on that object equal zero.

How does this apply to Civil Engineering? Well, when designing and modeling any structure, our end goal is for the structure to be rigid - Civil Engineers call this **static equalibrium**. This is pretty obvious, but this basic concept is the foundation for analysing any structural system.

This project contains three **components** or **page directories** (see src/pages/). 

- **1. Solver** (*./src/pages/solver/*)
- **2. Stiffness** (*./src/pages/stiffness/*)
- **3. Bridge-Design** (*./src/pages/bridge-design/*)

The solver **(1.)** is where users can go through an a multi-part form inputting all of the necessary information about either a Truss, Beam, or Frame system and a detailed solution will be output. The pages within the stiffness **(2.)** directory contain tutorials, walkthroughs, and examples which allow the user to better understand the matrix displacement method or build a solid foundation of the basics. The bridge-design **(3.)** directory will eventually contain similar tutorials as the stiffness **(2.)** directory, but as of `9/29/2021` I have mainly been building the features within solver **(1.)** and stiffness **(2.)**.

Let me know if you have any questions and feel free to reach out to me through any of the provided contacts at the bottom of this readme. Have fun!

</br>

## Demo

</br>

<div align="center">
  <h4><b>Truss Example 1 - figure 1.</b></h4>
  <img 
    src="https://user-images.githubusercontent.com/64326462/153630740-d688f8b7-ae1c-456a-9ce6-65346a0cb8e6.png" 
    alt="truss-example-1"  
    align="center"
    width="900"
  />
</div>

</br>
</br>

<div align="center">
  <h4><b>Truss Example 2 - figure 2.</b></h4>
  <img 
    src="https://user-images.githubusercontent.com/64326462/153630929-d517f6f5-e932-4c62-869b-1ed3c9da9c21.png" 
    alt="truss-example-2"  
    align="center"
    width="900"
  />
</div>

</br>
</br>

<div align="center">
  <h4><b>Beam Example 1 - figure 3.</b></h4>
  <img 
    src="https://user-images.githubusercontent.com/64326462/153630923-d32d3e31-8c36-4077-95b2-17c5fb92a94a.png" 
    alt="beam-example-1"  
    align="center"
    width="900"
  />
</div>

</br>
</br>

## Quick start

### 1. Clone repository

```bash
git clone https://github.com/Brlaney/python-matrix-fem.git
```

### 2. Start virtual environment


### 3. Install dependencies

```bash
cd mtrx

# then for yarn users:
yarn install

# or npm users:
npm i 
```

### 4. Run example scripts

truss1.py, truss2.py, and beam1.py are all example scripts I have written that model the figures shown in the Demo section above.

```bash
py truss1.py

# or

python truss1.py

```

Now navigate to [http://localhost:3000/](http://localhost:3000/) and check it out.

</br>

## Connect with me

- Email: <brlaney@outlook.com>
- Twitter: [brendan_webdev](https://twitter.com/Brendan_webdev)
- Instagram: [brlaney94](https://www.instagram.com/brlaney94/)

</br>

## References and resources

- Great introduction video by [Dr. Structure](https://youtu.be/kFkU1M7xVbg)
- Wikipedia:
  - [Direct Stiffness Method](https://en.wikipedia.org/wiki/Direct_stiffness_method)
  - [Finite Element Method](https://en.wikipedia.org/wiki/Finite_element_method)
  - [Newtonian Mechanics](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion)
  - [Structural Analysis](https://en.wikipedia.org/wiki/Structural_analysis)
- [ABET](https://www.abet.org/)

</br>

## License

```text
MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files, to deal 
in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Brendan Laney | Copyright (c) 2021
```

</br>

## Contributions and issues

I would love your feedback on my project - please feel free to make a pull request or submit an issue if you find any. Thanks for checking out my project!
