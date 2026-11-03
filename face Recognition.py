import tkinter as tk
from tkinter import messagebox
import cv2
import os
import socket
import platform
import time
from datetime import datetime
from deepface import DeepFace

camera = None

root = tk.Tk()

root.title("Secure Face Authentication")
root.geometry("1000x700")
root.configure(bg="#08111f")
root.resizable(False, False)

APP_BG = "#08111f"
HEADER_BG = "#0d1b2a"
CARD_BG = "#102235"
INPUT_BG = "#172d43"
CYAN = "#5ee7ff"
GREEN = "#65e6a8"
RED = "#ff4d6d"
YELLOW = "#f4c95d"
WHITE = "#ffffff"
MUTED = "#8da2b8"


def clear_window():

    for widget in root.winfo_children():
        widget.destroy()


def get_system_info():

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M:%S")

    try:
        ip = socket.gethostbyname(
            socket.gethostname()
        )
    except:
        ip = "127.0.0.1"

    device = platform.system()

    return date, current_time, ip, device


def create_header(title, subtitle):

    header = tk.Frame(
        root,
        bg=HEADER_BG,
        height=95
    )

    header.pack(
        fill="x"
    )

    tk.Label(
        header,
        text="●",
        bg=HEADER_BG,
        fg=CYAN,
        font=("Arial", 22, "bold")
    ).place(
        x=45,
        y=30
    )

    tk.Label(
        header,
        text=title,
        bg=HEADER_BG,
        fg=CYAN,
        font=("Arial", 22, "bold")
    ).place(
        x=75,
        y=27
    )

    tk.Label(
        header,
        text=subtitle,
        bg=HEADER_BG,
        fg=MUTED,
        font=("Arial", 9, "bold")
    ).place(
        x=77,
        y=58
    )


def show_login_page():

    clear_window()

    root.configure(
        bg=APP_BG
    )

    create_header(
        "SECURE IDENTITY",
        "MULTI-LAYER AUTHENTICATION SYSTEM"
    )

    card = tk.Frame(
        root,
        bg=CARD_BG,
        highlightbackground="#1e3a52",
        highlightthickness=1
    )

    card.place(
        x=150,
        y=145,
        width=700,
        height=470
    )

    tk.Label(
        card,
        text="FACE ID LOGIN",
        bg=CARD_BG,
        fg=WHITE,
        font=("Arial", 28, "bold")
    ).pack(
        pady=(40, 5)
    )

    tk.Label(
        card,
        text="Secure access begins with your identity",
        bg=CARD_BG,
        fg=MUTED,
        font=("Arial", 11)
    ).pack(
        pady=(0, 35)
    )

    tk.Label(
        card,
        text="USERNAME",
        bg=CARD_BG,
        fg=CYAN,
        font=("Arial", 10, "bold")
    ).place(
        x=100,
        y=135
    )

    username_entry = tk.Entry(
        card,
        width=38,
        font=("Arial", 14),
        bg=INPUT_BG,
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat"
    )

    username_entry.place(
        x=100,
        y=165,
        height=42
    )

    tk.Label(
        card,
        text="PASSWORD",
        bg=CARD_BG,
        fg=CYAN,
        font=("Arial", 10, "bold")
    ).place(
        x=100,
        y=225
    )

    password_entry = tk.Entry(
        card,
        width=38,
        show="●",
        font=("Arial", 14),
        bg=INPUT_BG,
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat"
    )

    password_entry.place(
        x=100,
        y=255,
        height=42
    )

    status_label = tk.Label(
        card,
        text="● SYSTEM READY",
        bg=CARD_BG,
        fg=GREEN,
        font=("Arial", 10, "bold")
    )

    status_label.place(
        x=100,
        y=320
    )

    login_button = tk.Button(
        card,
        text="START SECURE LOGIN",
        command=lambda: start_face_camera(
            username_entry.get().strip(),
            password_entry.get()
        ),
        bg="#087f8c",
        fg=WHITE,
        activebackground="#0aa6b5",
        activeforeground=WHITE,
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2",
        width=25,
        height=2
    )

    login_button.place(
        x=100,
        y=365
    )

    clear_button = tk.Button(
        card,
        text="CLEAR",
        command=lambda: (
            username_entry.delete(0, tk.END),
            password_entry.delete(0, tk.END),
            status_label.config(
                text="● SYSTEM READY",
                fg=GREEN
            )
        ),
        bg="#26384a",
        fg=WHITE,
        activebackground="#344d64",
        activeforeground=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        width=12,
        height=2
    )

    clear_button.place(
        x=470,
        y=365
    )

    tk.Label(
        card,
        text="FACE  •  BEHAVIOR  •  IDENTITY",
        bg=CARD_BG,
        fg="#526b82",
        font=("Arial", 9, "bold")
    ).place(
        x=235,
        y=425
    )

    username_entry.focus_set()

def start_face_camera(username, password):

    global camera

    # -----------------------------
    # Validate username
    # -----------------------------
    if username == "":
        messagebox.showerror(
            "Login Error",
            "Please enter your username."
        )
        return

    # -----------------------------
    # Validate password
    # -----------------------------
    if password == "":
        messagebox.showerror(
            "Login Error",
            "Please enter your password."
        )
        return

    # -----------------------------
    # Clear login screen
    # -----------------------------
    clear_window()

    root.configure(bg=APP_BG)

    create_header(
        "FACE ID VERIFICATION",
        "BIOMETRIC IDENTITY SCAN"
    )

    tk.Label(
        root,
        text="USER : " + username.upper(),
        bg=HEADER_BG,
        fg=MUTED,
        font=("Arial", 10, "bold")
    ).place(
        x=810,
        y=45
    )

    # -----------------------------
    # Camera card
    # -----------------------------
    card = tk.Frame(
        root,
        bg=CARD_BG,
        highlightbackground="#1e3a52",
        highlightthickness=1
    )

    card.place(
        x=150,
        y=140,
        width=700,
        height=500
    )

    tk.Label(
        card,
        text="IDENTITY SCAN",
        bg=CARD_BG,
        fg=WHITE,
        font=("Arial", 27, "bold")
    ).pack(
        pady=(30, 5)
    )

    tk.Label(
        card,
        text="Look directly at the camera",
        bg=CARD_BG,
        fg=MUTED,
        font=("Arial", 11)
    ).pack(
        pady=(0, 20)
    )

    status_label = tk.Label(
        card,
        text="● OPENING CAMERA...",
        bg=CARD_BG,
        fg=YELLOW,
        font=("Arial", 11, "bold")
    )

    status_label.pack(
        pady=10
    )

    tk.Label(
        card,
        text=(
            "A camera window will open automatically.\n\n"
            "Place your face inside the GREEN BOX.\n"
            "Press Q to capture your face.\n"
            "Press ESC to cancel."
        ),
        bg=CARD_BG,
        fg=MUTED,
        font=("Arial", 11),
        justify="center"
    ).pack(
        pady=25
    )

    root.update()

    # -----------------------------
    # Open camera
    # -----------------------------
    camera = cv2.VideoCapture(
        0,
        cv2.CAP_DSHOW
    )

    # Try camera 1 if camera 0 fails
    if not camera.isOpened():

        camera.release()

        camera = cv2.VideoCapture(
            1,
            cv2.CAP_DSHOW
        )

    # -----------------------------
    # Camera failed
    # -----------------------------
    if not camera.isOpened():

        status_label.config(
            text="● CAMERA ERROR",
            fg=RED
        )

        messagebox.showerror(
            "Camera Error",
            "Camera could not be opened.\n\n"
            "Please check:\n"
            "1. Camera is connected.\n"
            "2. No other application is using it.\n"
            "3. Windows Camera permission is enabled."
        )

        show_login_page()
        return

    # -----------------------------
    # Camera successfully opened
    # -----------------------------
    status_label.config(
        text="● CAMERA ACTIVE",
        fg=GREEN
    )

    root.update()

    captured = False

    # -----------------------------
    # Camera loop
    # -----------------------------
    while True:

        ret, frame = camera.read()

        if not ret:
            break

        # Mirror camera
        frame = cv2.flip(
            frame,
            1
        )

        # -----------------------------
        # GREEN FACE GUIDE BOX
        # -----------------------------
        cv2.rectangle(
            frame,
            (150, 60),
            (490, 400),
            (0, 255, 0),
            3
        )

        # -----------------------------
        # Box title
        # -----------------------------
        cv2.putText(
            frame,
            "PLACE FACE INSIDE GREEN BOX",
            (105, 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        # -----------------------------
        # Instructions
        # -----------------------------
        cv2.putText(
            frame,
            "Q = CAPTURE",
            (20, 450),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "ESC = CANCEL",
            (430, 450),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # -----------------------------
        # Show camera
        # -----------------------------
        cv2.imshow(
            "Face ID Verification",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        # -----------------------------
        # Capture
        # -----------------------------
        if key == ord("q"):

            status_label.config(
                text="● FACE CAPTURED — ANALYZING...",
                fg=YELLOW
            )

            root.update()

            cv2.imwrite(
                "current_face.jpg",
                frame
            )

            captured = True

            break

        # -----------------------------
        # Cancel
        # -----------------------------
        elif key == 27:
            break

    # -----------------------------
    # Close camera
    # -----------------------------
    camera.release()

    cv2.destroyAllWindows()

    cv2.waitKey(1)

    # -----------------------------
    # If cancelled
    # -----------------------------
    if not captured:

        status_label.config(
            text="● SCAN CANCELLED",
            fg=RED
        )

        messagebox.showwarning(
            "Authentication Cancelled",
            "Face authentication was cancelled."
        )

        show_login_page()

        return

    # -----------------------------
    # Compare captured face
    # -----------------------------
    status_label.config(
        text="● FACE CAPTURED — ANALYZING...",
        fg=YELLOW
    )

    root.update()

    compare_face(
        username,
        password
    )

def compare_face(username, password):

    captured_image = "current_face.jpg"
    registered_folder = os.path.join("faces", username)

    print()
    print("========================================")
    print("FACE RECOGNITION STARTED")
    print("========================================")

    if not os.path.exists(captured_image):

        messagebox.showerror(
            "Face Recognition Error",
            "Captured face image was not found."
        )

        show_login_page()
        return

    if not os.path.exists(registered_folder):

        messagebox.showerror(
            "Face Recognition Error",
            "Registered face folder was not found:\n\n"
            + registered_folder
        )

        show_login_page()
        return

    registered_images = []

    for filename in os.listdir(registered_folder):

        if filename.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):

            registered_images.append(
                os.path.join(
                    registered_folder,
                    filename
                )
            )

    if len(registered_images) == 0:

        messagebox.showerror(
            "Face Recognition Error",
            "No registered face images were found."
        )

        show_login_page()
        return

    print(
        "Captured image:",
        captured_image
    )

    print(
        "Registered folder:",
        registered_folder
    )

    print(
        "Registered images:",
        len(registered_images)
    )

    best_distance = None
    best_image = None
    matched = False

    for registered_image in registered_images:

        print()
        print(
            "Comparing:",
            registered_image
        )

        try:

            result = DeepFace.verify(

                img1_path=captured_image,

                img2_path=registered_image,

                model_name="Facenet512",

                detector_backend="retinaface",

                distance_metric="cosine",

                enforce_detection=False
            )

            distance = result.get(
                "distance"
            )

            verified = result.get(
                "verified",
                False
            )

            print(
                "Distance:",
                distance
            )

            print(
                "Verified:",
                verified
            )

            if distance is not None:

                if (
                    best_distance is None
                    or distance < best_distance
                ):

                    best_distance = distance

                    best_image = registered_image

            if verified:

                matched = True
                break

        except Exception as e:

            print(
                "Comparison failed:"
            )

            print(
                str(e)
            )

    print()
    print("========================================")
    print("FINAL FACE RECOGNITION RESULT")
    print("========================================")

    print(
        "Best image:",
        best_image
    )

    print(
        "Best distance:",
        best_distance
    )

    print(
        "Matched:",
        matched
    )

    if matched:

        print(
            "Prediction : AUTHORIZED USER"
        )

        print(
            "Access : GRANTED"
        )

        messagebox.showinfo(
            "Authentication Successful",
            "✓ FACE VERIFIED\n\n"
            "AUTHORIZED USER\n\n"
            "ACCESS GRANTED."
        )

        show_key_stroke_page(
            username,
            password,
            best_distance
        )

        return

    print(
        "Prediction : IMPOSTOR USER"
    )

    print(
        "Access : DENIED"
    )

    if best_distance is None:

        distance_text = "No valid comparison"

    else:

        distance_text = str(
            round(
                best_distance,
                4
            )
        )

    messagebox.showerror(
        "Authentication Failed",
        "✕ IMPOSTOR USER\n\n"
        "Face does not match the registered profile.\n\n"
        "Best Distance : "
        + distance_text
        + "\n\n"
        "ACCESS DENIED."
    )
def show_keystroke_page(username, password, face_distance):

    clear_window()

    root.configure(
        bg=APP_BG
    )

    create_header(
        "SECURE ACCESS",
        "MULTI-FACTOR IDENTITY VERIFICATION"
    )

    card = tk.Frame(
        root,
        bg=CARD_BG,
        highlightbackground="#1e3a52",
        highlightthickness=1
    )

    card.place(
        x=150,
        y=135,
        width=700,
        height=530
    )

    tk.Label(
        card,
        text="ACCESS VERIFIED",
        bg=CARD_BG,
        fg=GREEN,
        font=("Arial", 27, "bold")
    ).pack(
        pady=(35, 5)
    )

    tk.Label(
        card,
        text="Biometric identity confirmed successfully",
        bg=CARD_BG,
        fg=MUTED,
        font=("Arial", 11)
    ).pack(
        pady=(0, 25)
    )

    info_frame = tk.Frame(
        card,
        bg="#10263a"
    )

    info_frame.pack(
        padx=45,
        fill="x"
    )

    tk.Label(
        info_frame,
        text="USER",
        bg="#10263a",
        fg=MUTED,
        font=("Arial", 10, "bold")
    ).grid(
        row=0,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    tk.Label(
        info_frame,
        text=username.upper(),
        bg="#10263a",
        fg=WHITE,
        font=("Arial", 11, "bold")
    ).grid(
        row=0,
        column=1,
        padx=20,
        pady=15,
        sticky="w"
    )

    tk.Label(
        info_frame,
        text="FACE STATUS",
        bg="#10263a",
        fg=MUTED,
        font=("Arial", 10, "bold")
    ).grid(
        row=1,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    tk.Label(
        info_frame,
        text="VERIFIED",
        bg="#10263a",
        fg=GREEN,
        font=("Arial", 11, "bold")
    ).grid(
        row=1,
        column=1,
        padx=20,
        pady=15,
        sticky="w"
    )

    if face_distance != float("inf"):

        distance_text = str(
            round(
                face_distance,
                4
            )
        )

    else:

        distance_text = "N/A"

    tk.Label(
        info_frame,
        text="FACE DISTANCE",
        bg="#10263a",
        fg=MUTED,
        font=("Arial", 10, "bold")
    ).grid(
        row=2,
        column=0,
        padx=20,
        pady=15,
        sticky="w"
    )

    tk.Label(
        info_frame,
        text=distance_text,
        bg="#10263a",
        fg="#65e6a8",
        font=("Arial", 11, "bold")
    ).grid(
        row=2,
        column=1,
        padx=20,
        pady=15,
        sticky="w"
    )

    tk.Label(
        card,
        text="SECOND SECURITY CHECK",
        bg=CARD_BG,
        fg=WHITE,
        font=("Arial", 16, "bold")
    ).pack(
        pady=(25, 5)
    )

    tk.Label(
        card,
        text="Enter your security password to continue",
        bg=CARD_BG,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(
        pady=(0, 12)
    )

    password_frame = tk.Frame(
        card,
        bg="#0b1a2a"
    )

    password_frame.pack(
        padx=190,
        fill="x"
    )

    security_entry = tk.Entry(
        password_frame,
        bg="#0b1a2a",
        fg=WHITE,
        insertbackground=WHITE,
        font=("Arial", 13),
        relief="flat",
        show="●"
    )

    security_entry.pack(
        padx=12,
        pady=12,
        fill="x"
    )

    status_label = tk.Label(
        card,
        text="● WAITING FOR SECURITY PASSWORD",
        bg=CARD_BG,
        fg=YELLOW,
        font=("Arial", 10, "bold")
    )

    status_label.pack(
        pady=12
    )

    def verify_security():

        entered_password = security_entry.get()

        if entered_password == "":

            status_label.config(
                text="● ENTER PASSWORD",
                fg=RED
            )

            messagebox.showwarning(
                "Security Check",
                "Please enter your password."
            )

            return

        status_label.config(
            text="● VERIFYING SECURITY PASSWORD...",
            fg=YELLOW
        )

        root.update()

        if entered_password == password:

            status_label.config(
                text="● SECURITY CHECK PASSED",
                fg=GREEN
            )

            messagebox.showinfo(
                "Access Granted",
                "✓ ALL SECURITY CHECKS PASSED\n\n"
                "Face Identity : VERIFIED\n"
                "Password : VERIFIED\n\n"
                "ACCESS GRANTED"
            )

            show_success_page(
                username,
                distance_text
            )

        else:

            status_label.config(
                text="● INVALID PASSWORD",
                fg=RED
            )

            security_entry.delete(
                0,
                tk.END
            )

            messagebox.showerror(
                "Access Denied",
                "✕ SECURITY CHECK FAILED\n\n"
                "Incorrect password.\n\n"
                "ACCESS DENIED."
            )

    button_frame = tk.Frame(
        card,
        bg=CARD_BG
    )

    button_frame.pack(
        pady=10
    )

    verify_button = tk.Button(
        button_frame,
        text="VERIFY & CONTINUE",
        command=verify_security,
        bg="#0d9b68",
        fg=WHITE,
        activebackground="#12b77c",
        activeforeground=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        width=20,
        height=2
    )

    verify_button.grid(
        row=0,
        column=0,
        padx=8
    )

    back_button = tk.Button(
        button_frame,
        text="BACK TO LOGIN",
        command=show_login_page,
        bg="#26384a",
        fg=WHITE,
        activebackground="#344d64",
        activeforeground=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        width=15,
        height=2
    )

    back_button.grid(
        row=0,
        column=1,
        padx=8
    )

    security_entry.focus_set()


def show_success_page(username, distance_text):

    clear_window()

    root.configure(
        bg="#06131f"
    )

    create_header(
        "ACCESS GRANTED",
        "SECURE AUTHENTICATION COMPLETE"
    )

    card = tk.Frame(
        root,
        bg=CARD_BG,
        highlightbackground="#1e3a52",
        highlightthickness=1
    )

    card.place(
        x=150,
        y=150,
        width=700,
        height=450
    )

    tk.Label(
        card,
        text="✓",
        bg=CARD_BG,
        fg=GREEN,
        font=("Arial", 55, "bold")
    ).pack(
        pady=(35, 0)
    )

    tk.Label(
        card,
        text="ACCESS GRANTED",
        bg=CARD_BG,
        fg=GREEN,
        font=("Arial", 30, "bold")
    ).pack(
        pady=5
    )

    tk.Label(
        card,
        text="Identity successfully authenticated",
        bg=CARD_BG,
        fg=WHITE,
        font=("Arial", 13)
    ).pack(
        pady=5
    )

    details = tk.Frame(
        card,
        bg="#10263a"
    )

    details.pack(
        padx=80,
        pady=25,
        fill="x"
    )

    tk.Label(
        details,
        text="USER",
        bg="#10263a",
        fg=MUTED,
        font=("Arial", 10, "bold")
    ).grid(
        row=0,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    tk.Label(
        details,
        text=username.upper(),
        bg="#10263a",
        fg=WHITE,
        font=("Arial", 11, "bold")
    ).grid(
        row=0,
        column=1,
        padx=20,
        pady=12,
        sticky="w"
    )

    tk.Label(
        details,
        text="FACE",
        bg="#10263a",
        fg=MUTED,
        font=("Arial", 10, "bold")
    ).grid(
        row=1,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    tk.Label(
        details,
        text="VERIFIED",
        bg="#10263a",
        fg=GREEN,
        font=("Arial", 11, "bold")
    ).grid(
        row=1,
        column=1,
        padx=20,
        pady=12,
        sticky="w"
    )

    tk.Label(
        details,
        text="DISTANCE",
        bg="#10263a",
        fg=MUTED,
        font=("Arial", 10, "bold")
    ).grid(
        row=2,
        column=0,
        padx=20,
        pady=12,
        sticky="w"
    )

    tk.Label(
        details,
        text=distance_text,
        bg="#10263a",
        fg=WHITE,
        font=("Arial", 11, "bold")
    ).grid(
        row=2,
        column=1,
        padx=20,
        pady=12,
        sticky="w"
    )

    tk.Label(
        card,
        text="Your secure session has been authenticated.",
        bg=CARD_BG,
        fg=MUTED,
        font=("Arial", 10)
    ).pack(
        pady=5
    )

    tk.Button(
        card,
        text="RETURN TO LOGIN",
        command=show_login_page,
        bg="#0d9b68",
        fg=WHITE,
        activebackground="#12b77c",
        activeforeground=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        width=20,
        height=2
    ).pack(
        pady=15
    )

def logout_user():

    result = messagebox.askyesno(
        "Logout",
        "Are you sure you want to logout?"
    )

    if result:

        show_login_page()


def close_application():

    result = messagebox.askyesno(
        "Exit Application",
        "Are you sure you want to exit?"
    )

    if result:

        try:
            if camera is not None:
                camera.release()
        except:
            pass

        cv2.destroyAllWindows()

        root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_application
)


show_login_page()


root.mainloop()
