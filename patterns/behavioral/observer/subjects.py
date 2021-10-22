from abstract_objects import Subject, Observer


class ConcreteSubject(Subject):
    _state: int = None

    _observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def run_business_logic(self) -> None:
        print(f"Estou rodando minha lógica de negócio")
        
        self._state = randrange(0, 10)
        
        print(f"Atualizei meu estado para: {self._state}")
        
        self.notify()
