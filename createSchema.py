#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cassandra.cluster import Cluster
import logging
import time

log = logging.getLogger()
log.setLevel('INFO')
with open('server.conf') as f:
    content = f.readlines()

class SimpleClient:

    session = None

    def connect(self, nodes):
        cluster = Cluster(nodes)
        metadata = cluster.metadata
        self.session = cluster.connect()
        log.info('Connected to cluster: ' + metadata.cluster_name)
        # for host in metadata.all_hosts():
        #     log.info('Datacenter: %s; Host: %s; Rack: %s',
        #         host.datacenter, host.address, host.rack)

    def close(self):
        self.session.cluster.shutdown()
        self.session.shutdown()
        log.info('Connection closed.')

    def create_keyspace(self):
        self.session.execute("""CREATE KEYSPACE hospital WITH replication = {'class':'SimpleStrategy', 'replication_factor':3};""")
        log.info('hospital keyspace and schema created.')

    def connect_keyspace(self):
        self.session = cluster.connect('hospital')
        log.info('Connected to hopital KeySpace')

    def create_schema(self):
        self.session.execute("""
            CREATE TABLE hospital.patients (
                patient_id text PRIMARY KEY,
                name text,
                email text,
                address text
            );
        """)
        self.session.execute("""
            CREATE TABLE hospital.data (
                patient_id text,
                date text,
                event_time timestamp,
                heart_rate text,
                PRIMARY KEY ((patient_id, date), event_time)
            ) WITH CLUSTERING ORDER BY (event_time DESC);
        """)
        log.info('Schema created')


    def load_data(self):
        self.session.execute("""
            INSERT INTO hospital.patients (patient_id, name, email, address)
            VALUES (
                '1',
                'Shehaaz Saif',
                'Shehaaz@gmail.com',
                '123 fake street U.S.A'
            );
        """)
        self.session.execute("""
            INSERT INTO hospital.data (patient_id, date, event_time, heart_rate)
            VALUES (
                '1',
                '2015-02-27',
                '2015-02-27 22:00:00',
                '70'
            );
        """)
        log.info('Data loaded.')

    def query_schema(self):
        results = self.session.execute("""
    SELECT * FROM hospital.data
    WHERE patient_id = '1'
    AND date= '2015-02-28'
    AND event_time > '2015-02-28 23:58:50'
	AND event_time < '2015-02-28 23:58:55';
""")
        print "%-30s\t%-20s\t%-20s\n%s" % \
    ("patient_id", "event_time", "heart rate",
        "-------------------------------+-----------------------+--------------------")
        for row in results:
            print "%-30s\t%-20s\t%-20s" % (row.patient_id, row.event_time, row.heart_rate)
        log.info('Schema queried.')

def main():
    logging.basicConfig()
    client = SimpleClient()
    client.connect([content[1].rstrip()])
    #client.create_keyspace()
    #client.connect_keyspace()
    #client.create_schema()
    #time.sleep(10)
    #client.load_data()
    client.query_schema()
    client.close()

if __name__ == "__main__":
    main()
