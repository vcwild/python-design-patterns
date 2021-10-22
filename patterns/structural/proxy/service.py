from proxy import Service, Proxy

real_service = Service()

service = Proxy(real_service)
