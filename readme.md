### LaTeX Figure Rendering

- The 'standalone' package is used for plotting figures with 'pgfplot'
Compare: [Package Documentation](http://mirror.ox.ac.uk/sites/ctan.org/macros/latex/contrib/standalone/standalone.pdf)


### CRI Simulation

_Simulates the illumination of an input image by an arbitrary light source,
given its the specrtral power distribution._ 

#### Packages

- [LuxPy](https://github.com/ksmet1977/luxpy)
- [Colour](https://www.colour-science.org/) (aka Colour Science)
- [scikit-image](https://scikit-image.org/)

#### Documentation

[LuxPy introductory article](https://doi.org/10.1080/15502724.2018.1518717) in LEUKOS.

#### Caveats

- Error while using [`luxpy.toolboxes.hypspcim.render_image`](https://ksmet1977.github.io/luxpy/build/html/toolboxes.html?highlight=hyper#luxpy.toolboxes.hypspcim.render_image): `cannot reshape array of size XXX into shape (XXX,3)`

  Solution:
  
  _Convert RGBK image to uint8 RGB image._
  Function input must be an array of unsigned, 8-bit integer RGB values. An additional key (RGB_K_) value will throw an error.
  
  