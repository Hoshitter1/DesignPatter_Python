## Issue

### 1. Object creation logic gets too convoluted

### 2. Initializer is not descriptive
#### 2-1. name is always __init__ no matter how variables interact each other or
    how they will be used to calculate for a particular instance.

## Solution
### Wholesale object creation(outsource the process of creation of an object)
#### 1. A separate method(factory method)
#### 2. A separate class(factory)
#### 3. create hierarchy of factories with Abstract Factory



