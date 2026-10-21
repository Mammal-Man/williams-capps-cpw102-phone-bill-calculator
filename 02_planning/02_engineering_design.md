# Engineering Design

**Team members:**

Plan how your code will meet the product requirements. Keep answers brief.

## Inputs

(float) data usage in GB, (float) base cost

## Processing and decisions

if data usage < 10GB 
    user is within plan
    multiply base rate by GB
if data usage > 10 GB
    moderate usage
    add over use rate multiplied by GB to base cost
if data usage > 15 GB
    high usage


## Output

*What will the program display for each usage category?*
program will display how far over the limit they are, or how much data until they hit the limit.
program will display if their usage is moderate or high
program will display total bill

## Function design

*Give your data-allowance-checking function's name, parameters, and returned result. How will the program use that result?*

