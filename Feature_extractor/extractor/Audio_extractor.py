import numpy as np
import librosa

import os
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen


class Audio_extractor(object):
    def __init__(self):
        self.models = ['wav2mfcc', 'wavenet']

    def wav2mfcc(self, file_path, max_pad_len=11, **kwargs):
        wave, sr = librosa.load(file_path, mono=True, sr=None, res_type='kaiser_fast')
        wave = wave[::3]
        mfcc = librosa.feature.mfcc(wave, sr=16000)
        pad_width = max_pad_len - mfcc.shape[1]
        pad_width = max(0, pad_width)
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
        return mfcc

    def wavenet_encode(self, file_path, **kwargs):

        if os.path.exists('../../Pretrained_models/wavenet-ckpt/'):

            # Load the model weights.
            checkpoint_path = '../../Pretrained_models/wavenet-ckpt/model.ckpt-200000'
        else:
            raise Exception('you should download pretrained model to pretrained_models folder make prediction, the link is: http://download.magenta.tensorflow.org/models/nsynth/wavenet-ckpt.tar')

        # Load and downsample the audio.
        neural_sample_rate = 16000
        audio = utils.load_audio(file_path,
                                 sample_length=400000,
                                 sr=neural_sample_rate)

        # Pass the audio through the first half of the autoencoder,
        # to get a list of latent variables that describe the sound.
        # Note that it would be quicker to pass a batch of audio
        # to fastgen.
        encoding = fastgen.encode(audio, checkpoint_path, len(audio))

        # Reshape to a single sound.
        return encoding.reshape((-1, 16))

    # An array of n * 16 frames.
    # wavenet_z_data = wavenet_encode(file_path)
