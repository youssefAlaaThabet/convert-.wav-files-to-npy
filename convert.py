import librosa 
import numpy as np
import glob, os
for infile in glob.glob("*.wav"):
	filename=infile
	y, sr = librosa.load(filename)
	m=librosa.feature.melspectrogram(y=y, sr=sr)

	np.save(filename+".npy",m)
	print(sr)
