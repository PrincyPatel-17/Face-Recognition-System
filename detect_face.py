from deepface import DeepFace

result = DeepFace.extract_faces(
    img_path="faces/Princy/1.jpg",
    detector_backend="retinaface",
    enforce_detection=True
)

print("Face detected successfully.")
print("Number of faces:", len(result))

for face in result:
    print("Confidence:", face["confidence"])