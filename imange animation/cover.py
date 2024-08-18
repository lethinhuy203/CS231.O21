import cv2
# Buoc 1: Doc 2 anh A va B
A = cv2.imread("D:/Pictures/Adobe illustrator/art01-01.png", cv2.IMREAD_COLOR)
B = cv2.imread("D:/Pictures/Adobe illustrator/bo-01.png", cv2.IMREAD_COLOR)

# Buoc 2: Resize
A = cv2.resize(A, [800, 500])
B = cv2.resize(B, [800, 500])

view = A.copy()
W = A.shape[1]

for D in range(W):
    view[:,W-D:W] = B[:,0:D]
    cv2.imshow("View", view)
    cv2.waitKey(10)