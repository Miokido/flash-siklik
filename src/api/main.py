import j2l.pytactx.agent as pytactx

agent = pytactx.Agent(playerId="demo",
						arena="flashsiklik",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

while True:
	agent.update()
