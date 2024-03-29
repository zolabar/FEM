[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zolabar/FEM/HEAD)

# FEM: Finite Element Method 
## not only for solid mechanics :)

FEM 1D example with Python created by Zoufiné Lauer-Baré

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/zolabar)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zoufine-lauer-bare-14677a77)
[![Google Scholar](https://img.shields.io/badge/google%20scholar-4285F4?style=for-the-badge&logo=google%20assistant&logoColor=white)](https://scholar.google.com/citations?user=Gsm7ZzUAAAAJ&hl=en&oi=sra)

5 Node example for 1D PDE with constant right hand side and prescribed Dirichlet boundary conditions. Example could be a rod displacement or plane gap flow.

### Meshing: Nodes and Elements

<img src=FIGURES/diskretisierung.PNG height='200'>

![meshing](/FEM/assets/diskretisierung.PNG)

### Assemble system: Shape Functions

<img src=FIGURES/formfunktionen.PNG height='200'>

![shape functions](/FEM/assets/formfunktionen.PNG)

### Solution: Numerical FEM approximation exact at the nodes!

<img src=FIGURES/verschiebung.PNG height='200'>

![solution](/FEM/assets/verschiebung.PNG)

### Usage

Click on the binder button [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zolabar/FEM/HEAD) for using the Python Code in Cloud

or install Python, Jupyter etc... and download or clone this repository.


### FEM vs. FVM: Find the difference!

<img src=FIGURES/fem_vs_fvm.PNG height='500'>

![fem vs fvm](/FEM/assets/fem_vs_fvm.PNG)

**-> FEM exact on nodes and FVM exact at gradients between nodes**

### Visualization of analytical plate deformation in 3D!

<img src=FIGURES/plate_analytical_uz_scaled.PNG height='500'>

![fem vs fvm](/FEM/assets/plate_analytical_uz_scaled.PNG)


