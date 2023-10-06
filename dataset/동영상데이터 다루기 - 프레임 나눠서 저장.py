import cv2
import os

cap = cv2.VideoCapture("./blooms-113004.mp4")

fps = 25  # 25FPS 기준으로 프레임 나눠서 저장

count = 0
if cap.isOpened():  # 캡처 객체 초기화 확인
    while True:
        ret, frame = cap.read()  # 다음 프레임 읽기

        if ret:
            if(int(cap.get(1)) % fps == 0):
                os. makedirs("./frame_image_save/", exist_ok=True)  # 이미지 저장 할 폴더 생성
                cv2.imwrite(f"./frame_image_save/image_{str(count).zfill(4)}.png", frame)
                count = count + 1
        else:
            break
else:
    print("can't open video.")  # 캡처 객체 초기화 실패

cap.release()  # 캡처 지원 반납
cv2.destroyAllWindows()
