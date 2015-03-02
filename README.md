# RestingPython

This is a simple Python project that currently streams data to [plot.ly](https://plot.ly/python/streaming/) from an [Arduino + e-health PCB](http://www.cooking-hacks.com/documentation/tutorials/ehealth-biometric-sensor-platform-arduino-raspberry-pi-medical#step3_1)

[![IMAGE ALT TEXT HERE](http://i.imgur.com/rFGR3WA.png)](http://www.youtube.com/watch?v=SDatAH0Gpgs)


![Alt text](http://i.imgur.com/IIUJwPV.png "Arduino + e-health PCB")
![e-Health PCB](http://i.imgur.com/TShU0FI.png "e-health PCB")


# Optional
Deploy Cassandra cluster on [Google Compute](https://cloud.google.com/solutions/cassandra/)
How to [Youtube Video](https://www.youtube.com/watch?v=YYruoSxMAJw)

Once deployed SSH into each C* node run this command
It opens up port 9042 for CQL and 9160 for Thrift

(You will be prompted to login and update "gcloud")

`gcutil addfirewall cassandra-rule --allowed="tcp:9042,tcp:9160" --network="default" --description="Allow external Cassandra Thrift/CQL connections"`


#Python installation
pip install requirements.txt

#Next steps
* Answer specific questions: e.g: When was my Temp. higher than 30c? What was my HR between 7:00am and 7:05am?
