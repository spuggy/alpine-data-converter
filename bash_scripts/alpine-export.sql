use alpines;
SELECT *
FROM registeredusertable
    INTO OUTFILE '/tmp/registeredusertable-exp.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';


SELECT *
FROM mastermembershiptable
    INTO OUTFILE '/tmp/mastermembershiptable-exp.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT *
FROM mastermembertable
    INTO OUTFILE '/tmp/mastermembertable-exp.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
