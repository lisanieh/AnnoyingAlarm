import scipy.io.wavfile
import scipy.signal
import shutil
import os

def ste(x, win):
  """Compute short-time energy."""
  if isinstance(win, str):
    win = scipy.signal.get_window(win, max(1, len(x) // 8))
  win = win / len(win)
  return scipy.signal.convolve(x**2, win**2, mode="same")

def copy_and_replace(source_path, destination_path):
    if os.path.exists(destination_path):
        print("ready to remove...")
        os.remove(destination_path)
    shutil.copy2(source_path, destination_path)
 
# Source and destination file paths
source_file = 'recording0.wav'
destination_file = 'alarm.wav'

audio_path = "recording0.wav"
fs, x = scipy.io.wavfile.read(audio_path)
threshold = 1.5

e = ste(x, scipy.signal.get_window("hamming", int(0.1 * fs)))

if any(e > threshold):
    copy_and_replace(source_file, destination_file)
    print("change!")
else:
   print("not change") 
