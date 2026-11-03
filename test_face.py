from deepface import DeepFace

result = DeepFace.verify(
    img1_path="current_face.jpg",
    img2_path="faces/Princy/1.jpg",
    model_name="Facenet512",
    detector_backend="retinaface",
    enforce_detection=True
)

print()
print("========== FACE VERIFICATION ==========")
print("Verified :", result["verified"])
print("Distance :", round(result["distance"], 4))
print("Threshold:", round(result["threshold"], 4))
print("Confidence:", result.get("confidence"))