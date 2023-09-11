# 一个电力系统的数据库例子
1. PowerPlant（电厂表）：

    PlantID: 电厂的唯一标识符。

    PlantName: 电厂的名称。

    PlantType: 电厂的类型（如火力、水力、核能、风能等）。
    
    Location: 电厂的地理位置。 
```sql
CREATE TABLE PowerPlant (
    PlantID INT PRIMARY KEY,
    PlantName VARCHAR(255),
    PlantType VARCHAR(255),
    Location VARCHAR(255)
);
```

2. Generator（发电机表）：

    GeneratorID: 发电机的唯一标识符。

    PlantID: 发电机所在电厂的ID。

    Capacity: 发电机的产能（单位可能是兆瓦）。

    Type: 发电机的类型（如蒸汽涡轮机、燃气涡轮机等）。
```sql
CREATE TABLE Generator (
    GeneratorID INT PRIMARY KEY,
    PlantID INT,
    Capacity DECIMAL(10,2),
    Type VARCHAR(255),
    FOREIGN KEY (PlantID) REFERENCES PowerPlant(PlantID)
);
```

3. TransmissionLine（输电线路表）：

    LineID: 输电线路的唯一标识符。
    
    StartLocation: 输电线路的起始地点。
    
    EndLocation: 输电线路的结束地点。
    
    Capacity: 输电线路的容量（单位可能是兆瓦）。
    
    Substation（变电站表）：
```sql
CREATE TABLE TransmissionLine (
    LineID INT PRIMARY KEY,
    StartLocation VARCHAR(255),
    EndLocation VARCHAR(255),
    Capacity DECIMAL(10,2)
);
```

4. SubstationID: 变电站的唯一标识符。

    Location: 变电站的地理位置。

    Capacity: 变电站的容量（单位可能是兆伏安）。
```sql
CREATE TABLE Substation (
    SubstationID INT PRIMARY KEY,
    Location VARCHAR(255),
    Capacity DECIMAL(10,2)
);
```

5. Load（负荷表）：

    LoadID: 负荷的唯一标识符。

    SubstationID: 负荷所在变电站的ID。

    LoadValue: 负荷值（单位可能是兆瓦）。
```sql
CREATE TABLE Load (
    LoadID INT PRIMARY KEY,
    SubstationID INT,
    LoadValue DECIMAL(10,2),
    FOREIGN KEY (SubstationID) REFERENCES Substation(SubstationID)
);
```

6. MeterReading（电表读数表）：

    ReadingID: 读数的唯一标识符。

    MeterID: 电表的ID。

    DateTime: 读数的日期和时间。

    ReadingValue: 电表的读数。
```sql
CREATE TABLE MeterReading (
    ReadingID INT PRIMARY KEY,
    MeterID INT,
    DateTime DATETIME,
    ReadingValue DECIMAL(10,2)
);
```

# 问题
1. 问题：查询所有的水力电厂的名称和位置。

    相关的表和字段：PowerPlant表，PlantName和Location字段。

    SQL语句：
    ```sql
    SELECT PlantName, Location 
    FROM PowerPlant 
    WHERE PlantType = '水力';
    ```
    prompt:
    CREATE TABLE PowerPlant (
        PlantID INT PRIMARY KEY,
        PlantName VARCHAR(255),
        PlantType VARCHAR(255),
        Location VARCHAR(255)
    );
    /* Query the names and locations of all hydroelectric power plants. */

2. 问题：查找所有产能超过1000MW的发电机的ID和它们所在的电厂ID。

    相关的表和字段：Generator表，GeneratorID和PlantID字段。
    SQL语句：
    ```sql
    SELECT GeneratorID, PlantID 
    FROM Generator 
    WHERE Capacity > 1000;
    ```
    prompt:
    CREATE TABLE Generator (
        GeneratorID INT PRIMARY KEY,
        PlantID INT,
        Capacity DECIMAL(10,2),
        Type VARCHAR(255),
        FOREIGN KEY (PlantID) REFERENCES PowerPlant(PlantID)
    );
    /* Find the IDs of all generators with a capacity exceeding 1000MW and their corresponding power plant IDs. */

3. 问题：找出所有位于特定位置（比如"北京"）的变电站的ID和容量。

    相关的表和字段：Substation表，SubstationID和Capacity字段。

    SQL语句：
    ```sql
    SELECT SubstationID, Capacity 
    FROM Substation 
    WHERE Location = '北京';
    ```
    prompt:
    CREATE TABLE Substation (
        SubstationID INT PRIMARY KEY,
        Location VARCHAR(255),
        Capacity DECIMAL(10,2)
    );
    /* Find the IDs and capacities of all substations located at specific locations (such as "Beijing"). */

4. 问题：查询某个特定时间（比如"2023-09-08 12:00:00"）的所有电表读数。

    相关的表和字段：MeterReading表，MeterID和ReadingValue字段。
    
    SQL语句：
    ```sql
    SELECT MeterID, ReadingValue 
    FROM MeterReading 
    WHERE DateTime = '2023-09-08 12:00:00';
    ```
    prompt:
    CREATE TABLE MeterReading (
        ReadingID INT PRIMARY KEY,
        MeterID INT,
        DateTime DATETIME,
        ReadingValue DECIMAL(10,2)
    );
    /* Retrieve all the electricity meter readings for a specific time (e.g., "2023-09-08 12:00:00"). */

5. 问题：查询某个特定变电站（比如ID为1）的总负荷值。

    相关的表和字段：Load表，SubstationID和LoadValue字段。
    
    SQL语句：
    ```sql
    SELECT SUM(LoadValue) 
    FROM Load 
    WHERE SubstationID = 1;
    ```
    prompt:
    CREATE TABLE Load (
        LoadID INT PRIMARY KEY,
        SubstationID INT,
        LoadValue DECIMAL(10,2),
        FOREIGN KEY (SubstationID) REFERENCES Substation(SubstationID)
    );
    /* Query the total load value of a specific substation (e.g., ID 1). */

6. 问题：查询所有产能超过1000MW的发电机所在的电厂的名称。

    相关的表和字段：Generator表和PowerPlant表，GeneratorID，PlantID和PlantName字段。
    
    SQL语句：
    ```sql
    SELECT PowerPlant.PlantName 
    FROM Generator 
    INNER JOIN PowerPlant ON Generator.PlantID = PowerPlant.PlantID 
    WHERE Generator.Capacity > 1000;
    ```
    prompt:
    CREATE TABLE Generator (
        GeneratorID INT PRIMARY KEY,
        PlantID INT,
        Capacity DECIMAL(10,2),
        Type VARCHAR(255),
        FOREIGN KEY (PlantID) REFERENCES PowerPlant(PlantID)
    );
    CREATE TABLE PowerPlant (
        PlantID INT PRIMARY KEY,
        PlantName VARCHAR(255),
        PlantType VARCHAR(255),
        Location VARCHAR(255)
    );
    /* Query the names of power plants where the generating capacity exceeds 1000MW. */

7. 问题：查询"北京"所有变电站的负荷总和。

    相关的表和字段：Substation表和Load表，SubstationID，Location和LoadValue字段。

    SQL语句：
    ```sql
    Copy
    SELECT SUM(Load.LoadValue) 
    FROM Load 
    INNER JOIN Substation ON Load.SubstationID = Substation.SubstationID 
    WHERE Substation.Location = '北京';
    ```
    prompt:
    CREATE TABLE Substation (
        SubstationID INT PRIMARY KEY,
        Location VARCHAR(255),
        Capacity DECIMAL(10,2)
    );
    CREATE TABLE Load (
        LoadID INT PRIMARY KEY,
        SubstationID INT,
        LoadValue DECIMAL(10,2),
        FOREIGN KEY (SubstationID) REFERENCES Substation(SubstationID)
    );
    /* Query the total load of all substations in "Beijing." */

8. 问题：查找产能最大的发电机的类型和所在电厂的名字。

    相关的表和字段：Generator表和PowerPlant表，GeneratorID，PlantID，PlantName和Type字段。

    SQL语句：
    ```sql
    SELECT PowerPlant.PlantName, Generator.Type 
    FROM Generator 
    INNER JOIN PowerPlant ON Generator.PlantID = PowerPlant.PlantID 
    WHERE Generator.Capacity = (SELECT MAX(Capacity) FROM Generator);
    ```
    prompt:
    CREATE TABLE Generator (
        GeneratorID INT PRIMARY KEY,
        PlantID INT,
        Capacity DECIMAL(10,2),
        Type VARCHAR(255),
        FOREIGN KEY (PlantID) REFERENCES PowerPlant(PlantID)
    );
    CREATE TABLE PowerPlant (
        PlantID INT PRIMARY KEY,
        PlantName VARCHAR(255),
        PlantType VARCHAR(255),
        Location VARCHAR(255)
    );
    /* Find the type of the generator with the highest capacity and the name of the power plant where it is located. */

9. 问题：查询某一天（比如"2023-09-08"）的总电力消耗（所有电表读数的总和）。

    相关的表和字段：MeterReading表，DateTime和ReadingValue字段。

    SQL语句：
    ```sql
    Copy
    SELECT SUM(ReadingValue) 
    FROM MeterReading 
    WHERE DATE(DateTime) = '2023-09-08';
    ```
    prompt:
    CREATE TABLE MeterReading (
        ReadingID INT PRIMARY KEY,
        MeterID INT,
        DateTime DATETIME,
        ReadingValue DECIMAL(10,2)
    );
    /* Query the total electricity consumption for a specific day (e.g., '2023-09-08'), which is the sum of all electricity meter readings. */

10. 问题：找出哪个电厂的发电机产能总和最大。

    相关的表和字段：Generator表和PowerPlant表，GeneratorID，PlantID，PlantName和Capacity字段。

    SQL语句：
    ```sql
    Copy
    SELECT PowerPlant.PlantName, SUM(Generator.Capacity) as TotalCapacity 
    FROM Generator 
    INNER JOIN PowerPlant ON Generator.PlantID = PowerPlant.PlantID 
    GROUP BY Generator.PlantID 
    ORDER BY TotalCapacity DESC 
    LIMIT 1;
    ```
    prompt:
    CREATE TABLE Generator (
        GeneratorID INT PRIMARY KEY,
        PlantID INT,
        Capacity DECIMAL(10,2),
        Type VARCHAR(255),
        FOREIGN KEY (PlantID) REFERENCES PowerPlant(PlantID)
    );
    CREATE TABLE PowerPlant (
        PlantID INT PRIMARY KEY,
        PlantName VARCHAR(255),
        PlantType VARCHAR(255),
        Location VARCHAR(255)
    );
    /* Find out which power plant has the largest total generator capacity. */
