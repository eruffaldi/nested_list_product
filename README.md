# nested_list_product
The product (or in other terms the combination) of multiple lists generates all the combination of list elements equivalent to the elements of a tensor. In algorithm testing or in other experimental settings we need to generate products with nested lists. This is a small code in MATLAB

# Context "Disciplined Multi-Algorithm Testing"
The aim is to run multiple algorithms and their variants and keep track of all the outcomes for comparison. We identify the following concepts:

- Case: one of the possible data input situations
- SubCase: some decomposition of the case, associated with some Case Parameters
- Algorithm: the name of the algorithm
- Variant: a major variant of the algorithm (exclusive)
- Algorithm Parameter: an enumeration or numeric argument for the given Algorithm or Variant
- Algorithm Instance: combines Algorithm+Variant+Parameters 
- Unique Identifier: unique identification of Algorithm Instance that should be compatible with a given naming scheme (e.g. Matlab structure variable)
- Reference: the reference value of the given Case/SubCase, that will be compared against algorithm result by means of metrics
- Measure: performance measure of the case given the execution of the Algorithm with unit of measure
- Repetition: repetition index of the Case by AlgorithmInstance in case the Algorithm has some random aspect

The idea is to execute all the Cases by AlgorithmInstances and build a single table. This table will have the following field (or field families):

# Approach

We model this with enumerations (e.g. list of algorithms), with the possibility of nested enumeration for a given value (e.g. list of variants for a given algorithm),
and finally parameters variations (e.g. for specific version). Also datasets are an enumeration.

We then generate a matrix M by N, where M is any possible enumeration (NaN if not applicable) and N is the list of all possible cases. The matrix contains

## Case Study is the Paper on Inertial Measure Review on Sensors:

- Algorithms: zhu, yun, young, pep, peps
- Variants: 
  - Young: pure or perfect
  - Peppoloni: original or svd or reordered
  - ...
- Case:
  - Real Case: Aug10
  - Simulation


