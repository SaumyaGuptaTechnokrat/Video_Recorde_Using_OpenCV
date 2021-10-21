import streamlit as st
import cv2

st.title("VIDEO RECORDER") #    using Open Cv ## st.title is used to give title to your webpage
video_name = st.text_input("Enter the video name to save: ")
def record_video():
    camera = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f'{video_name}.avi', fourcc, 20.0, (640, 480))
    while True:
        b, fro = camera.read()
        cv2.imshow('ReadingWebcam_2nd',fro)
        out.write(fro)
        if not b:
            break
        if cv2.waitKey(10) & 0xFF == ord('y'): ## Ord - When key pressed it will find the code of key 
            break
    camera.release()
    cv2.destroyAllWindows()
    out.release()

cb = st.checkbox("Start Recording") #It will tell whether to record the video or not

if cb:
    record_video() # calling the method
    





