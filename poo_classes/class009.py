"""
Association
"""

class Musician:

    def __init__(self, name) -> None:
        self.name = name
        self._instrument = list()
    
    @property
    def instrument(self) -> str:
        return self._instrument
    
    @instrument.setter
    def instrument(self, name) -> None:
        self._instrument.append(name)
    
    def musician_playing(self) -> str:
        instruments_name = ''
        for instrument in self._instrument:
            instruments_name += f'{instrument} '
        return f'{self.name} is playing 🎵 {instruments_name}.'

    def __str__(self) -> str:
        return f'{self.name}'

class Instrument:

    def __init__(self, name) -> None:
        self.name = name
    
    def playing(self) -> str:
        return f'{self.name} is playing... 🎵'

    def __str__(self) -> str:
        return f'{self.name}'

romeo = Musician('Romeo')
guitar = Instrument('Guitar')
piano = Instrument('Piano')

romeo.instrument = guitar
romeo.instrument = piano


print(guitar.playing())
print(piano.playing())
print(romeo.musician_playing())
for instrument in romeo.instrument:
    print(instrument.playing())