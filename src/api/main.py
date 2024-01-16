import j2l.pytactx.agent as pytactx

agent = pytactx.Agent(playerId=input("👾 id: "),
						arena=input("🎲 arena: "),
						username="demo",
						password=input("🔑 password: "),
						server="mqtt.jusdeliens.com",
						verbosity=2)

while True:
	agent.update()
	print("Agent direction : " + str(agent.dir))
	print("Agent position : " + str(agent.x) + " ; " + str(agent.y))
	