import time
import json

class Recorder:
    def __init__(self):
        self.recording = []
        self.is_recording = False
        self.start_time = None

    def start_recording(self):
        self.is_recording = True
        self.start_time = time.time()
        self.recording = []

    def stop_recording(self):
        self.is_recording = False
        self.start_time = None

    def record_key_press(self, key):
        if self.is_recording:
            if self.start_time is None:
                self.start_time = time.time()
            self.recording.append({
                'key': key,
                'timestamp': time.time() - self.start_time
            })

    def record_key_release(self, key):
        if self.is_recording:
            for note in self.recording:
                if note['key'] == key and 'duration' not in note:
                    note['duration'] = time.time() - (self.start_time + note['timestamp'])
                    break

    def save_recording(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.recording, f)

    def load_recording(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def play_recording(self, recording, sounds):
        start_time = time.time()
        for note in recording:
            key = note['key']
            duration = note['duration']
            timestamp = note['timestamp']
            time_to_wait = timestamp - (time.time() - start_time)
            if time_to_wait > 0:
                time.sleep(time_to_wait)
            if key in sounds:
                sounds[key].play()
                time.sleep(duration)
                sounds[key].stop()
