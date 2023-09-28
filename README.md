# financialPredictions
Sample Input: `python3 movingAverages.py --input stockValues.csv --output other_output.csv`

Arguments:
`--input` Path to the input csv file, this script is tailored to the specific format in the initial problem
`--output` Path to the output csv file

Makes predicitions to buy sell or hold using the simple moving averages algorithm, when the average of one mean crosses another one (like in a line graph) a buy or sell decision is made, otherwise we hold.
This algorithm is traditionally used in day trading and may not function the same in a larger time scale.

The short average uses 5 previous data points,
The medium average uses 10,
The long average uses 25

Because the first set of entries doesn't have a long enough history to make a full medium and long average, a smaller history is used for the medium and short averages initially.
Let n be the current number of entries, for n < 25: long average = n, for n < 20: medium average = n/2, small average = n/4
