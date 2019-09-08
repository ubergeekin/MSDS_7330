##############################################################
##############################################################

Initial writeup: 2/7/2019

Editor: Paul Marquardt

MSDS7330-DBProject

##############################################################
##############################################################

##############################################################

February 7, 2019 	MSDS7330-DBProject

##############################################################

MSDS7330-DBProject_ProjectProposal.pdf contains the initial guidance of the overall project guidelines, tasks and process for testing purposes

Stock data information is contained in the following files:
amex_p_v_1.1.2019.to.2.6.2019.csv
nasdaq_p_v_1.1.2019.to.2.6.2019.csv
nyse_p_v_1.1.2019.to.2.6.2019.csv

Symbol pulls are from the following locations: 

NASDAQ: 
http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download 

NYSE: 
http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download 

AMEX: 
http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download 

Symbol listings only files:

NASDAQ: 

nasdq_symbols_clean.csv

NYSE: 

nyse_symbols_clean.csv

AMEX: 

amex_symbols_clean.csv

Pull process for corresponding exchanges and corresponding file name:

AMEX: 

amex_symbol_histdata_pull.py

NASDAQ: 

nasdaq_symbol_histdata_pull.py

NYSE: 

NYSE_symbol_histdata_pull.py

NOTE: You will need to edit the location of your symbol files and the out-path location for output of the historical data csv file

