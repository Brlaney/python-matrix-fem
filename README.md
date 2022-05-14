<div align="center" id="top">
  <img
    src="https://user-images.githubusercontent.com/64326462/154530618-fe4635e6-3884-42e3-9f51-d46541306b79.png"
    alt="python-matrix-fem"
  />
</div>
<div align="center">
  <p>
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

The solver **(1.)** is where users can go through an a multi-part form inputting all of the necessary information about either a Truss, Beam, or Frame system and a detailed solution will be output. The pages within the stiffness **(2.)** directory contain tutorials, walkthroughs, and examples which allow the user to better understand the matrix displacement method or build a solid foundation of the basics. The bridge-design **(3.)** directory will eventually contain similar tutorials as the stiffness **(2.)** directory, but as of `9/29/2021` I have mainly been building the features within solver **(1.)** and stiffness **(2.)**.

Let me know if you have any questions and feel free to reach out to me through any of the provided contacts at the bottom of this readme. Have fun!

</br>

## Demo

</br>

<div align="center">
  <h4><b>Truss Example 1 - figure 1.</b></h4>
  <img 
    src="https://user-images.githubusercontent.com/64326462/153637273-42628283-439c-49b4-86f9-c988d79a3a7b.png" 
    alt="truss-example-1"  
    align="center"
    width="900"
  />
</div>

</br>
</br>

```python
# truss1.py
from lib.trusses import *
import numpy as np
import time

# Node coordinates
nodes = np.array([
    [0, 0],
    [120, 120],
    [240, 120],
    [360, 0]])

# Member connection matrix
members = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
    [2, 4]])

L1 = []                      # length in inches
L2 = []                      # length in feet
a1 = []                      # units: degrees
a2 = []                      # units: radians
n = len(nodes)               # number of nodes
m = len(members)             # number of members
A = np.repeat(2, m)          # Cross-sectional areas of each element
E = np.repeat(29*10**6, m)   # Modulus of elasticity for each element

# 1 => Un-restrained global degrees of freedom
dgf = np.array([0, 0, 1, 1, 1, 1, 0, 0])

# External forces (lbs)
fg = np.array([2, -30000])

# Unknown global forces
fu = np.array([0, 1, 6, 7])

# given displacements
dp = np.array([[1, -0.6], [6, -0.3]])

Kl = []  # Each elems local [k] (global coords)
Kg = np.zeros((2*n, 2*n))  # global stiffness matrix

newKg = KgTruss(n, m, nodes, members, E, A, L1,
        L2, a1, a2, Kg, Kl, fg, dgf)

```

</br>

Appending the following code to the file will output the following.

```python
#...

newKg = KgTruss(n, m, nodes, members, E, A, L1,
        L2, a1, a2, Kg, Kl, fg, dgf)

print('\nLength in inches')
print(L1)
print('\nLength in feet')
print(L2)
print('\nAngles in degrees')
print(a1)
print('\nAngles in radians')
print(a2)

print('\nGlobal stiffness matrix')
print(newKg)
```

```cmd
C:\Users\Brlan\Documents\coding\python-matrix-fem>py truss1.py

Time elapsed: 0.0076985

C:\Users\Brlan\Documents\coding\python-matrix-fem>py truss2.py
[[ 6.54217472e+05  1.70884139e+05 -1.70884139e+05 -1.70884139e+05
   0.00000000e+00  0.00000000e+00 -4.83333333e+05  0.00000000e+00]
 [ 1.70884139e+05  1.70884139e+05 -1.70884139e+05 -1.70884139e+05
   0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00]
 [-1.70884139e+05 -1.70884139e+05  3.41768278e+05  1.16415322e-10
  -1.70884139e+05 -1.70884139e+05 -1.63098876e-26 -4.83333333e+05]
 [-1.70884139e+05 -1.70884139e+05  1.16415322e-10  8.25101611e+05
   1.70884139e+05 -1.70884139e+05 -8.87868929e-11 -4.83333333e+05]
 [ 0.00000000e+00  0.00000000e+00 -1.70884139e+05  1.70884139e+05
   6.54217472e+05 -1.70884139e+05 -4.83333333e+05 -7.24883895e-27]
 [ 0.00000000e+00  0.00000000e+00  1.70884139e+05 -1.70884139e+05
  -1.70884139e+05  1.70884139e+05  5.91912620e-11 -7.24883895e-27]
 [-4.83333333e+05  0.00000000e+00 -1.63098876e-26 -8.87868929e-11
  -4.83333333e+05  5.91912620e-11  9.66666667e+05  2.95956310e-11]
 [ 0.00000000e+00  0.00000000e+00 -8.87868929e-11 -4.83333333e+05
   5.91912620e-11 -7.24883895e-27  2.95956310e-11  4.83333333e+05]]

Final time: 0.0

C:\Users\Brlan\Documents\coding\python-matrix-fem>py truss1.py

Length in inches
[169.7056274847714, 120.0, 169.7056274847714, 268.32815729997475, 268.32815729997475]

Length in feet
[14.142135623730951, 10.0, 14.142135623730951, 22.360679774997894, 22.360679774997894]

Angles in degrees
[45.0, 0, 315.0, 26.56505117707799, 333.434948822922]

Angles in radians
[0.7853981633974483, 0.0, 5.497787143782138, 0.4636476090008061, 5.81953769817878]

Global stiffness matrix
[[ 343806.72904673  257345.43391674 -170884.13878675 -170884.13878675
  -172922.59025998  -43230.647565         0.               0.        ]
 [ 257345.43391674  214114.78635174 -170884.13878675 -170884.13878675
   -86461.29512999  -43230.647565         0.               0.        ]
 [-170884.13878675 -170884.13878675  827140.06238007   84422.84365676
  -483333.33333333       0.         -172922.59025998  -43230.647565  ]
 [-170884.13878675 -170884.13878675   84422.84365676  214114.78635174
        0.               0.           86461.29512999  -43230.647565  ]
 [-172922.59025998  -86461.29512999 -483333.33333333       0.
   827140.06238007  -84422.84365676 -170884.13878675 -170884.13878675]
 [ -86461.29512999  -43230.647565         0.               0.
   -84422.84365676  214114.78635175  170884.13878675 -170884.13878675]
 [      0.               0.         -172922.59025998   86461.29512999
  -170884.13878675  170884.13878675  343806.72904673 -257345.43391674]
 [      0.               0.           86461.29512999  -43230.647565
   170884.13878675 -170884.13878675 -257345.43391674  214114.78635175]]
```

</br>

<div align="center">
  <h4><b>Truss Example 2 - figure 2.</b></h4>
  <img 
    src="https://user-images.githubusercontent.com/64326462/153637276-041a25ce-f460-4d2e-a87c-470977d9650c.png" 
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
    src="https://user-images.githubusercontent.com/64326462/153637271-d16ef5d6-97ab-4e2f-b1ae-70de4fc4ddea.png" 
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

Note: you can do this many different ways - or you don't necessarily even need to start a virtual environment if you have all of the necessary dependencies. My reason for using one is to easily keep up with all of the dependencies used in the project. The instructions below are what work for me using my Windows terminal.

```bash
# Step i.)

virtualenv ll_env

# or

virtualenv <your-venv-name>

# Step ii.)

ll_env\scripts\activate.bat

# or

<your-venv-name>\scripts\activate.bat
```

### 3. Install dependencies

```bash
(ll_env) C:\PATH\>pip install -r requirements.txt

```

### 4. Run example scripts

truss1.py, truss2.py, and beam1.py are all example scripts I have written that model the figures 1, 2, & 3 shown in the Demo section above.

```bash
# Can use truss2.py or beam1.py instead if desired.
py truss1.py

# or

python truss1.py

```

The solution to the system should be output in your terminal after running the script.
</br>

## Connect with me

- Email: <brlaney@outlook.com>
- Twitter: [brendan_webdev](https://twitter.com/Brendan_webdev)
- Instagram: [brlaney94](https://www.instagram.com/brlaney94/)

</br>

## References and resources

- Great intro lesson: [Dr. Structure](https://youtu.be/kFkU1M7xVbg)
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
