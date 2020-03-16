#### Install packages
`$ pip install -r requirements.txt`

#### Testing
`$ pytest --benchmark-disable -s -v test_finder.py`

#### Performance benchmarking
`$ pytest -s -v test_finder.py -k TestFinderBenchmark`


#### Assumptions:
- Return string from list of strings that contains characters from input string in any order.
- Return string if input string char exist multiple time in list of string.

``` 
     eg: find = 'aabc'
        string_list = ['aabbc', 'abc']
        output = ['aabbc', 'abc']
```
