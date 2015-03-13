            CREATE TABLE hospital.data (
                patient_id text,
                event_time timestamp,
                heart_rate text,
                PRIMARY KEY (patient_id, event_time)
            ) WITH CLUSTERING ORDER BY (event_time DESC);




            INSERT INTO hospital.data (patient_id, date, event_time, heart_rate)
            VALUES (
                '1',
                '2015-02-27',
                '2015-02-27 22:00:00',
                '70'
            );



            SELECT * FROM hospital.data
            WHERE patient_id = '1'
            AND date= '2015-02-28'
            AND event_time > '2015-02-28 23:58:50'
          AND event_time < '2015-02-28 23:58:55';
