import configparser

configfile = configparser.ConfigParser()
configfile.read("../config/position.conf","UTF-8")

print(configfile.get("channel1", "now"))

configfile.set("channel1","now","100")

with open("../config/position.conf","w") as configfig:
	configfile.write(configfig)
