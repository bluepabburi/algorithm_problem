# def solution(n, w):
#     answer = 0
#     height = 1
#     box_line = []
    
#     for _ in range(1, n+1):

#         if len(box_line([height])) < w:
#             for i in range(w):
#                box_line[height].append(i)
#         else:
#             height += 1
#             box_line[height] = []
    
    
        
#     return box_line


# def solution(n, w):
#     box_line = []
#     h = -1
    
#     for i in range(n):
#         if i % w == 0:
#             box_line.append([])  # 새 줄 추가
#             h *= -1
#         box_line[h].append(i+1)
    
#     return box_line

# print(solution(10, 3))


# def solution(n, w, num):
#     answer = 0
#     box_line = []
#     ans = 0
#     ans = (n + w - 1) // w

#     for i in range(n):
#         if i % w == 0:
#             box_line.append([])

#         current_row = len(box_line) - 1
        
#         if current_row % 2 == 0:
#             box_line[current_row].append(i+1)
        
#         else:
#             box_line[current_row].insert(0, i+1)
    
#     box_line.reverse()
    
#     for i in range(len(box_line)):
#         for k in range(len(box_line[i])):
        
#             if box_line[i][k] == num:
#                 answer = ans - i
#                 print(answer)
   
    
#     return answer

# def solution(n, w, num):
#     box_line = []
#     total_rows = (n + w - 1) // w

#     for i in range(n):
#         if i % w == 0:
#             box_line.append([])

#         row = len(box_line) - 1

#         if row % 2 == 0:
#             box_line[row].append(i + 1)
#         else:
#             box_line[row].insert(0, i + 1)

#     box_line.reverse()

#     for i in range(len(box_line)):
#         for j in range(len(box_line[i])):
#             if box_line[i][j] == num:
#                 answer = i + 1
#                 print(answer)
#                 return answer

#     return 0


a = (solution(29, 5))
