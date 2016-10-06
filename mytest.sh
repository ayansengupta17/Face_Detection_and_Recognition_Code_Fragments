rm /home/itachi3/Documents/Research/codes/torch/openface_modified/demos/people.p
for filename in /home/itachi3/Documents/Research/codes/torch/workspace/face_detection/cropped_images/*;do
/home/itachi3/Documents/Research/codes/torch/openface_modified/demos/classifier.py infer /home/itachi3/Documents/Research/codes/torch/openface_modified/generated-embeddings/classifier.pkl $filename
done
python /home/itachi3/Documents/Research/codes/torch/openface_modified/demos/read_people.py
