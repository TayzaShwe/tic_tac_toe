# TIC-TAC-TOE GAME #

This is the official repository for my Tic-Tac-Toe Game. 

### Table of Contents ###
1) Why I developed this tic-tac-toe game
2) How the game works
3) How the minimax algorithm works
4) Using PyQt5 and PyInstaller
5) Technologies involved 

## WHY I DEVELOPED THIS TRADING BOT ##

It's a pretty simple but fun game and I was initially just interested in how to create an algorithm that would be hard to beat. So, I coded it and even added a user interface!

## HOW MY TRADING BOT WORKS ##

You can play against three kinds of opponents:
* Player 2. Just takes in another input from user.
* Easy Bot. Randomizes the next move.
* Hard Bot. Uses the minimax algorithm to find optimal move.

[Demonstration video.](https://youtu.be/EiNxiaXhf8w)

## HOW THE MINIMAX ALGORITHM WORKS ##

The minimax algorithm is a recursive algorithm that simulates every possible move. The score that is returned when I win would be 1 and the score that is returned when my opponent wins is -1. The score is 0 when nobody has won yet and it is not a draw. We will refer to the number of moves as depth. The algorithm tries every available move at one depth and if it is my turn, picks the move with the highest score. The algorithm picks the lowest score for if it is my opponent's turn. The idea is that the algorithm picks the best move for me and the best move for the opponent since the lowest score is the best score for my opponent. It does this until all possible moves are calculated. If there are multiple highest scores, it arbitrarily picks a highest score. 

## USING PYQT5 AND PYINSTALLER ##

The first version I created used the terminal for user interface. I then switched to PyQt5. 
1) Design the windows in designer. This is PyQt5's drag-and-drop style application that allows you to build the interface. 
2) Save the design as a .ui file.
3) Convert the .ui file into a python file with the following command:
    pyuic5 -x filename.ui -o filename.py

## HOW TO USE THE SECOND VERSION OF BOT (USES PAPER MONEY) ##

For the second version that uses paper money (fake money), you have more control over how you want to simulate actual trading. In __trading_bot_paper_money_config.txt__, you can enter the cryptocurrency to trade, the __gap__, the amount of money to use, the start and end dates, the time range (days, hours, minutes), and the percentage of loss incurred from sending __market orders__. After inputting this information, run __trading_bot_paper_money.py__. 

The net profit gained from using the bot and the net profit gained from the normal strategy will be displayed along with a matlibplot plot of the results. 
* Yellow line - cryptocurrency price
* Orange line - total value of money and the cryptocurrency from using the trading bot
* Pink line -  total value of money and the cryptocurrency without using the trading bot
* Blue line - the buy/sell price levels
* Red dot - the sell price
* Green dot - the buy price

A simple rule to remember is that the trading bot has outperformed the normal strategy if the orange line ends at a higher price than the pink line. 

## TECHNOLOGIES INVOLVED ##

* Python (for the versions 1 and 2)
* Matplotlib (for the version 2)
* [Coinbase Pro API](https://github.com/danpaquin/coinbasepro-python) (for the version 1) 
* [Cryptocompare API](https://github.com/lagerfeuer/cryptocompare) (for the versions 2 and 3) 
* [Chart.js](https://www.chartjs.org/) (for version 3)

