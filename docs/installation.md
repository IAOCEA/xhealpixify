# Installation

**xHEALPixify** is designed to convert georeferenced data expressed in latitude and longitude into a Healpix grid (https://healpix.sourceforge.io) and make use of the array indexing system provided by **Xarray** (http://xarray.pydata.org).

The development of xHEALPixify was initiated to meet the specific requirements of oceanography studies, which involve the analysis of geospatial data with varying precisions. This tool enables the performance of computations such as convolution while considering land masks through the utilization of a Hierarchical Equal Area Grid.

Given the particular characteristics of the Hierarchical Equal Area Grid, our aim is to provide solutions for Travel Time Analysis (like, H3 Travel Times - https://observablehq.com/@nrabinowitz/h3-travel-times), taking into account land masks and oceanic physical properties using xHEALPixify, with the goal of improving the tracking of fish habitats.

## How to test examples on your jupyterlab enviroment

```
git clone https://github.com/IAOCEA/xhealpixify.git
cd xhealpixify
micromamba create -n xhealpixify-test -f ci/requirements/environment.yaml
micromamba activate xhealpixify-test
pip install -e .
ipython kernel install --name xhealpixify-test --user

```
