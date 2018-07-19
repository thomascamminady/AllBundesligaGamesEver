History of every Bundesliga game ever played

Data is obtained from Kicker. The website was crawled and the obtained html files have been filtered to reduce everything to a single csv file.

The 3 Point rule was starting in season 1995/96, before that winning yielded 2 points (0 to loser), after that 3 points (0 to loser). A draw is always 1 point each.

The summary is in the following format:

     SeasonFrom | SeasonTo |Matchday| Day| Date| Time| Home| Guest| Score90| Score45| Score90Home| Score90Guest| Score45Home| Score45Guest| PointsHome| PointsGuest 
     ------------| ------------ |------------| ------------| ------------| ------------| ------------| ------------| ------------| ------------| ------------| ------------| ------------| ------------| ------------| ------------ 
     1963  |  1964  |  1  |  Saturday  |  1963-08-24  |  17:00  |  TSV 1860  |  Braunschweig  |  1:1 | 1:0  | 1 | 1  |  1 | 0  | 1 | 1
     1963  |  1964  |  1  |  Saturday  |  1963-08-24  |  17:00  |  Münster  |  HSV  |  1:1 | 0:0  | 1 | 1  |  0 | 0  | 1 | 1
     1963  |  1964  |  1  |  Saturday  |  1963-08-24  |  17:00  |  Saarbrücken  |  Köln  |  0:2 | 0:2  | 0 | 2  |  0 | 2  | 0 | 2
     1963  |  1964  |  1  |  Saturday  |  1963-08-24  |  17:00  |  Karlsruhe  |  Meidericher SV  |  1:4 | 0:3  | 1 | 4  |  0 | 3  | 0 | 2


Remark: 
For these four games we inserted the half time score as 0:0 since this information was missing.
	
	1970  ,  1971  ,  27  ,  Saturday  ,  1971-04-03  ,  15:30  ,  Gladbach  ,  Bremen
	
	1976  ,  1977  ,  15  ,  Saturday  ,  1976-11-27  ,  15:30  ,  K'lautern  ,  Düsseldorf 
	
	1992  ,  1993  ,  32  ,  Saturday  ,  1993-05-22  ,  15:30  ,  Uerdingen  ,  Frankfurt  
	
	1994  ,  1995  ,  26  ,  Saturday  ,  1995-04-15  ,  15:30  ,  Frankfurt  ,  Bayern  



Finally, we manually removed the entries corresponding to two following games that were terminated and then repeated on another day( see: http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/1963-64/14/0/spieltag.html and http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/2007-08/28/0/spieltag.html)

Procedure to get the data:

- gather html files from kicker via
	python  crawlkicker

- filter by keywords and write to csv file via 
	python filder.py >results.csv    

 
