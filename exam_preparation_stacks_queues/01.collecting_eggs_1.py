from collections import deque

eggs = deque([int(i) for i in input().split(", ")])
papers = [int(i) for i in input().split(", ")]

count_boxes = 0

while len(eggs) > 0 and len(papers) > 0:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue

    if current_egg == 13:
        temp = papers[0]
        papers[0] = papers[-1]
        papers[-1] = temp
        continue


    current_paper = papers.pop()

    if current_egg + current_paper <= 50:
        count_boxes += 1

if count_boxes > 0:
    print(f"Great! You filled {count_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    result = [str(egg) for egg in eggs]
    print(f"Eggs left: {', '.join(result)}")
if papers:
    result = [str(paper) for paper in papers]
    print(f"Pieces of paper left: {', '.join(result)}")