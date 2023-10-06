import cv2

cap = cv2. VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"Original width and height: {width}x{height}")

# 1280 x 720 종횡비에 맞게 이미지 크기 수정해야 함!

while True:
    ret, frame = cap.read()

    # 화면 사이즈 조정
    frame = cv2.resize(frame, (864, 486))

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break
    
cap.realease()
cv2.destroyAllWindows()