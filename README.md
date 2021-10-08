# Arb Master
Experimental repository for finding arbitrage opportunities on an exchange. More of a learning experience than a practical project.
Currently, contains a script that will check for triangular arbitrage opportunities of given pairs on binance.
Will move on to checking more than one triangle at a time and eventually checking for cyclic arbitrage over market graph in the future.

## Requirements:
Project is developed using python 3.9 and makes use of asynchronous libraries such as aiohttp and asyncio.

## Basic Usage:
Run arb-master py and give it three pairs in the following order:
```bash
python arb-master.py $A_B $C_B $C_A 
```
The script will log any arbitrage opportunities to a file called arbitrage.log .
Output file can be changed with `--logfile=$LOGFILE`.
You can also enable debug by passing in the `-d` flag. This tells the script to log the result every time a cycle is checked, regardless of profitability.

Here's an example of configuring the script:
```bash
python arb-master.py -d --logfile=$PATH_TO_LOGFILE $A_B $C_B $C_A 
```