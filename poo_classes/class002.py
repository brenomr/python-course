"""
States of Class
"""

class Camera:

    def __init__(self, name, recording=False) -> None:
        self.name = name
        self.recording = recording

    def __str__(self) -> str:
        return f'{self.name}'

    def start_recording(self) -> str:
        if self.recording:
            return f'{self.name} is already recording...'
        else:
            self.recording = True
            return f'{self.name} is starting to record...'
    
    def stop_recording(self) -> str:
        if not self.recording:
            return f'{self.name} isn\'t recording...'
        else:
            self.recording = False
            return f'{self.name} is stopping to record...'
    
    def take_a_picture(self) -> str:
        if self.recording:
            return f'{self.name} can\'t take a picture, because it\'s already recording...'
        else:
            return'Took a photograph!'

sonyJ1 = Camera('Sony J1')

print(sonyJ1.start_recording())
print(sonyJ1.start_recording())
print(sonyJ1.stop_recording())
print(sonyJ1.take_a_picture())