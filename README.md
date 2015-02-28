# RestingPython

Deploy Cassandra cluster on Google Compute
https://console.developers.google.com
https://www.youtube.com/watch?v=YYruoSxMAJw

Once deployed SSH into each C* node run this command
It opens up port 9042 for CQL and 9160 for Thrift

(You will be prompted to login and update "gcloud")

`gcutil addfirewall cassandra-rule --allowed="tcp:9042,tcp:9160" --network="default" --description="Allow external Cassandra Thrift/CQL connections"`


#Python installation
pip install requirements.txt
