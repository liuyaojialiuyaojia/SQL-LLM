# CodeGeex2

## CodeGeex2 - 6B - int4
1. 
```sql
SELECT PlantName, Location
    FROM PowerPlant
    ORDER BY PlantName;
```

2. 
```sql
SELECT *
    FROM Generator
    WHERE Capacity > 1000;
```

3. 
```sql
SELECT SubstationID, Capacity
    FROM Substation
    WHERE Location = 'Beijing';
```

4. 
```sql
SELECT *
    FROM MeterReading
    WHERE DateTime BETWEEN '2023-09-08 12:00:00' AND '2023-09-08 12:00:00'
    ORDER BY ReadingID;
```

5. 
```sql
SELECT SUM(LoadValue) AS TotalLoadValue
    FROM Load
    WHERE SubstationID = 1;
```

6. 
```sql
SELECT PlantName
    FROM PowerPlant
    WHERE PlantID IN (
        SELECT PowerPlant.PlantID
        FROM PowerPlant, Generator
        WHERE PowerPlant.PlantID = Generator.PlantID
        AND Capacity > 1000
    );
```

7. 
```sql
SELECT SUM(LoadValue)
    FROM Load
    WHERE SubstationID IN (SELECT SubstationID
    FROM Substation
    WHERE Location LIKE '%北京%');
```

8. 
```sql
SELECT Type, PlantName
    FROM PowerPlant
    INNER JOIN Generator
    ON PowerPlant.PlantID = Generator.PlantID
    ORDER BY Capacity DESC LIMIT 1;
```

9. 
```sql
SELECT
        SUM(ReadingValue) AS TotalElectricityConsumption
    FROM
        MeterReading
    WHERE
        MeterID = 1 AND
        DATE(DateTime) = '2023-09-08';
```

10. 
```sql
SELECT PlantName, Capacity
    FROM PowerPlant, Generator
    WHERE PowerPlant.PlantID = Generator.PlantID
    ORDER BY Capacity DESC LIMIT 1;
```
