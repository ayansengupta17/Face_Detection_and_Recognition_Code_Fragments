rm -r /home/itachi3/Documents/Research/codes/torch/openface_modified/aligned-images/cache.t7
/home/itachi3/Documents/Research/codes/torch/openface_modified/util/align-dlib.py /home/itachi3/Documents/Research/codes/torch/openface_modified/training-images/ align outerEyesAndNose /home/itachi3/Documents/Research/codes/torch/openface_modified/aligned-images/ --size 96
/home/itachi3/Documents/Research/codes/torch/openface_modified/batch-represent/main.lua -outDir /home/itachi3/Documents/Research/codes/torch/openface_modified/generated-embeddings/ -data /home/itachi3/Documents/Research/codes/torch/openface_modified/aligned-images/
/home/itachi3/Documents/Research/codes/torch/openface_modified/demos/classifier.py train /home/itachi3/Documents/Research/codes/torch/openface_modified/generated-embeddings/

