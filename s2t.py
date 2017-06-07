import os
import sys
from ctypes import *
from contextlib import contextmanager

import pyaudio
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

script_dir = os.path.dirname(os.path.realpath(__file__))
model_dir = "/home/akhil/Desktop/sphinx-source/pocketsphinx/model/en-us"

hmm = os.path.join(model_dir, "/home/akhil/Desktop/sphinx-source/pocketsphinx/model/en-us/en-us")
lm = os.path.join(model_dir, "/home/akhil/Desktop/sphinx-source/pocketsphinx/model/en-us/en-us.lm.bin")
dic = os.path.join(model_dir, "/home/akhil/Desktop/sphinx-source/pocketsphinx/model/en-us/cmudict-en-us.dict")

sys.stderr = open(os.path.join(script_dir, "stderr.log"), "a")



 
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    pass
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)



@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

config = Decoder.default_config()
config.set_string('-hmm', hmm)
config.set_string('-lm', lm)
config.set_string('-dict', dic)
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)

with noalsaerr():
    p = pyaudio.PyAudio()
    
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()
in_speech_bf = True
decoder.start_utt()
while True:
    buf = stream.read(1024)
    
    if buf:
        decoder.process_raw(buf, False, False)
        
        try:
            if decoder.hyp().hypstr != '':
                print('Partial decoding result:', decoder.hyp().hypstr)
                
        except AttributeError:
            pass
        if decoder.get_in_speech():
            sys.stdout.write('.')
            sys.stdout.flush()
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                try:
                    if decoder.hyp().hypstr != '':
                        print('Stream decoding result:', decoder.hyp().hypstr)
                except AttributeError:
                    pass
                decoder.start_utt()
    else:
        break
decoder.end_utt()
print('An Error occured:', decoder.hyp().hypstr)