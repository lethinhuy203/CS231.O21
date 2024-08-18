import cv2

# Buoc 1: Doc 2 anh A va B
A = cv2.imread("D:/Pictures/Adobe illustrator/art01-01.png", cv2.IMREAD_COLOR)
B = cv2.imread("D:/Pictures/Adobe illustrator/bo-01.png", cv2.IMREAD_COLOR)

# Buoc 2: Resize
A = cv2.resize(A, [800, 500])
B = cv2.resize(B, [800, 500])

# Buoc 3: Show hinh A va B de kiem tra
#cv2.imshow("image A", A)
#cv2.imshow("image B", B)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Buoc 4: Tao anh View
view = A.copy() # B.copy() cung duoc
H = A.shape[0]

for D in range(H):
    # Buoc 5: Copy phan duoi cua A vào View
    view[0:H-D] = A[D:H]
    # Buoc 6: Copy phan tren cua B vào View
    view[H-D:] = B[0:D]
    # Buoc 7: Show hinh
    cv2.imshow("View", view)
    cv2.waitKey(1)
