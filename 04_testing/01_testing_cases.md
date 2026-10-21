# Test Cases

Run each case separately. Determine the expected results by hand before running your program.

From the repository folder, run:

```text
python 03_execution/data_bill.py
```

Check the usage message, overage amount when applicable, and total bill. Paste each terminal run as evidence, then mark Pass or Fail and explain why.

## Case 1: At the data limit

- Data used (GB): 10
- Base plan cost: 40

**Expected results:**
within limit
$40
**Evidence (paste your terminal run):**

```
Enter GB used: 10
Enter base cost: 40
You are within your limit
your bill is $40.0

```

**Pass / Fail and why:**
Pass, returns expected results
## Case 2: At 5 GB over the limit

- Data used (GB): 15
- Base plan cost: 40

**Expected results:**
5 over, moderate usage, $50
**Evidence (paste your terminal run):**

```
Enter GB used: 15
Enter base cost: 40
you are 5.0 GB over your limit
moderate extra usage.
your bill is $50.0

```

**Pass / Fail and why:**
pass, results match expected
## Case 3: Above 5 GB over the limit

- Data used (GB): 15.5
- Base plan cost: 50

**Expected results:**
5.5 over, high usage, $61
**Evidence (paste your terminal run):**

```
Enter GB used: 15.5
Enter base cost: 50
you are 5.5 GB over your limit
high extra usage.
your bill is $61.0

```

**Pass / Fail and why:**
Pass, results match expectation
If a case fails, fix the program and add evidence of the rerun below that case.
