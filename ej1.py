import os

class ping:

    def execute(self, string):
        if string.startswith("192."):
            for i in range(10):
                os.system(f"ping -n 1 {string}")
        else:
            print("No se puede ejecutar el ping a esa dirección IP")

    def executeFree(self, string):
        for i in range (10):
            os.system(f"ping -n 1 {string}")

class pingProxy(ping):

    def execute(self, string):
        
        if string == "192.168.0.254":
            super().executeFree("www.google.com")
        else:
            super().execute(string)

p=pingProxy()
p.execute("192.168.0.254")
p.execute("8.8.8.8")
p.execute("192.123.3.123")