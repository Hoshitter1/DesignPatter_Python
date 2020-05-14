## Issue
Sometime people instantiate object more than once although initialization is expensive
for example,
1. Database repository
2. Object factory

## Solution
Prevent anyone creating additional copies
Take care of lazy instantiation

## What is singleton
A component which is instantiated  only once
