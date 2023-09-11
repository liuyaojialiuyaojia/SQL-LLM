# code llama

## code llama - 7B
1. 
```sql
SELECT PlantName, Location FROM PowerPlant WHERE PlantType = 'hydroelectric';
```

2. 
```sql
SELECT GeneratorID, PlantID FROM Generator WHERE Capacity > 1000;
```

3. 
```sql
SELECT SubstationID, Capacity FROM Substation WHERE Location = 'Beijing';
```

4. 
```sql
SELECT * FROM MeterReading
    WHERE DateTime = '2023-09-08 12:00:00';
```

5. 
```sql
SELECT SUM(LoadValue) FROM Load WHERE SubstationID = 1;
```

6. 
```sql
SELECT PlantName FROM PowerPlant WHERE Capacity > 1000;
```

7. 
```sql
SELECT SUM(LoadValue) AS TotalLoad
    FROM Load
    WHERE SubstationID IN (
        SELECT SubstationID
        FROM Substation
        WHERE Location = 'Beijing'
    );
```

8. 
```sql
SELECT Type, PlantName
    FROM Generator
    INNER JOIN PowerPlant ON Generator.PlantID = PowerPlant.PlantID
    WHERE Capacity = (SELECT MAX(Capacity) FROM Generator);
```

9. 
```sql
SELECT SUM(ReadingValue) AS TotalElectricityConsumption
    FROM MeterReading
    WHERE DateTime = '2023-09-08';
```

10. 
```sql
SELECT PlantName, SUM(Capacity) AS TotalCapacity
    FROM Generator
    INNER JOIN PowerPlant
    ON Generator.PlantID = PowerPlant.PlantID
    GROUP BY PlantName
    ORDER BY TotalCapacity DESC;
```

## code llama - python - 7B
1. 
```sql
SELECT PlantName, Location
    FROM PowerPlant
    WHERE PlantType = 'Hydroelectric';
```

2. 
```sql
SELECT GeneratorID, PlantID
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
SELECT * FROM MeterReading WHERE DateTime = '2023-09-08 12:00:00';
```

5. 
```sql
SELECT SUM(LoadValue) AS TotalLoad
    FROM Load
    WHERE SubstationID = 1;
```

6. 
```sql
SELECT PowerPlant.PlantName
    FROM PowerPlant
    INNER JOIN Generator ON PowerPlant.PlantID = Generator.PlantID
    WHERE Generator.Capacity > 1000;
```

7. 
```sql
SELECT Substation.SubstationID, Substation.Location, Substation.Capacity, Load.LoadValue
    FROM Substation, Load
    WHERE Substation.Location = 'Beijing' AND Substation.SubstationID = Load.SubstationID;
```

8. 
```sql
SELECT PowerPlant.PlantName, Generator.Type
    FROM Generator
    INNER JOIN PowerPlant ON Generator.PlantID = PowerPlant.PlantID
    WHERE Generator.Capacity = (SELECT MAX(Capacity) FROM Generator);
```

9. 
```sql
SELECT SUM(ReadingValue) AS TotalElectricityConsumption
    FROM MeterReading
    WHERE MeterID = 1
    AND DATEDIFF(DAY, DateTime, '2023-09-08') = 0;
```

10. 
```sql
SELECT PowerPlant.PlantName, PowerPlant.PlantType, PowerPlant.Location, SUM(Generator.Capacity) AS TotalCapacity
    FROM PowerPlant
    INNER JOIN Generator ON PowerPlant.PlantID = Generator.PlantID
    GROUP BY PowerPlant.PlantName, PowerPlant.PlantType, PowerPlant.Location
    ORDER BY TotalCapacity DESC
    LIMIT 1;
```

## code llama - instruct
1. 
```sql
SELECT PlantName, Location
    FROM PowerPlant
    WHERE PlantType = 'Hydroelectric';
```

2. 
```sql
SELECT GeneratorID, PlantID FROM Generator WHERE Capacity > 1000;
```

3. 
```sql
SELECT SubstationID, Capacity
    FROM Substation
    WHERE Location = 'Beijing';
```

4. 
```sql
SELECT * FROM MeterReading WHERE DateTime = '2023-09-08 12:00:00';
```

5. 
```sql
SELECT SUM(LoadValue) AS TotalLoad
    FROM Load
    WHERE SubstationID = 1;
```

6. 
```sql
SELECT PlantName
    FROM PowerPlant
    WHERE Capacity > 1000;
```

7. 
```sql
SELECT SUM(LoadValue) AS TotalLoad
    FROM Load
    WHERE SubstationID IN (
        SELECT SubstationID
        FROM Substation
        WHERE Location = 'Beijing'
    );
```

8. 
```sql
SELECT Type, PlantName
    FROM Generator
    JOIN PowerPlant ON Generator.PlantID = PowerPlant.PlantID
    WHERE Capacity = (SELECT MAX(Capacity) FROM Generator);
```

9. 
```sql
SELECT SUM(ReadingValue) AS TotalElectricityConsumption
    FROM MeterReading
    WHERE DateTime = '2023-09-08';
```

10. 
```sql
SELECT PowerPlant.PlantName, SUM(Capacity) AS TotalCapacity
    FROM PowerPlant
    JOIN Generator ON PowerPlant.PlantID = Generator.PlantID
    GROUP BY PowerPlant.PlantName
    ORDER BY TotalCapacity DESC
    LIMIT 1;
```
