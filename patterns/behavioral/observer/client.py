from observers import (
    AndressaObserver,
    LukempolObserver,
    CanturilObserver,
    BrancoObserver,
    SalesObserver
)

from subjects import ConcreteSubject


subject = ConcreteSubject()

andressa = AndressaObserver()

lukempol = LukempolObserver()

canturil = CanturilObserver()

branco = BrancoObserver()

sales = SalesObserver()

observers: list[Observer] = [
    andressa, lukempol, canturil, branco, sales
]

for observer in observers:
    subject.subscribe(observer)

for _ in range(0, 10):
    subject.run_business_logic()
