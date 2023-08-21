N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)

new_list = []
for score in score_list:
    new_list.append(score/max_score*100)

avg = sum(new_list)/N
print(avg)