import cv2

cap = cv2.VideoCapture("./video01.mp4")

# 비디오 파일 읽기
cap = cv2.VideoCapture("blooms-113004.mp4")

# 비디오 정보 가져오기
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# 비디오 정보 보기
print(f"Original width and height: {width}x{height}")
print(f"fps: {fps}")
print(f"frame count: {frame_count}")

# 동영상 파일 읽기 예시
if cap.isOpened():  # 캡처 객체 초기화 확인
    while True:
        ret, frame = cap.read()  # 다음 프레임 읽기
        if ret:  # 프레임 읽기가 정상일 때
            # 프레임 크기 조정 -> 영상 크기 수정
            frame = cv2.resize(frame, (640, 480))

            cv2.imshow('Video', frame)  # 화면 표시
            # q를 누르면 종료
            if cv2.waitKey(25) & 0xFF == ord('q'):  # 25ms 지연(40fps로 가정)
                exit()
        else:
            break
else:
    print("can't open")  # 캡처 객체 초기화 실패
    
cap.release()  # 캡처 지원 반납
cv2.destryAllwindows()