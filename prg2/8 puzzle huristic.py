def bfs(src, target):
    queue = []
    queue.append(src)
    vis = []
    while len(queue) &gt; 0:
        source = queue.pop(0)
        vis.append(source)
        print(source)
        if source == target:
            print(&quot;success&quot;)
    return
    poss_moves_to_do = []
    poss_moves_to_do = possible_moves(source, vis)
    for move in poss_moves_to_do:
        if move not in vis and move not in queue:
            queue.append(move)

def possible_moves(state, visited_states):
# Find index of empty spot and assign it to b
b = state.index(-1)
# &#39;d&#39; for down, &#39;u&#39; for up, &#39;r&#39; for right, &#39;l&#39; for left - directions array
d = []
# Add all possible direction into directions array - Hint using if statements

if b not in [0, 1, 2]:
d.append(&#39;u&#39;)
if b not in [6, 7, 8]:
d.append(&#39;d&#39;)
if b not in [0, 3, 6]:
d.append(&#39;l&#39;)
if b not in [2, 5, 8]:
d.append(&#39;r&#39;)
# If direction is possible then add state to move
pos_moves_it_can = []
# for all possible directions find the state if that move is played
### Jump to gen function to generate all possible moves in the given
directions
for i in d:
pos_moves_it_can.append(gen(state, i, b))
return [move_it_can for move_it_can in pos_moves_it_can if move_it_can
not in visited_states]

# Generate move for given direction
def gen(state, m, b):
temp = state.copy()
# if move is to slide empty spot to the left and so on
if m == &#39;d&#39;:
temp[b + 3], temp[b] = temp[b], temp[b + 3]
if m == &#39;u&#39;:
temp[b - 3], temp[b] = temp[b], temp[b - 3]
if m == &#39;l&#39;:

temp[b - 1], temp[b] = temp[b], temp[b - 1]
if m == &#39;r&#39;:
temp[b + 1], temp[b] = temp[b], temp[b + 1]
# return new state with tested move to later check if &quot;src == target&quot;
return temp
# # Test 1
#src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
#target = [1, 2, 3, 4, 5, -1, 6, 7, 8]
# bfs(src, target)
# Test 2
src = [1,2,3,-1,4,5,6,7,8]
target = [1,2,3,4,5,-1,6,7,8]
bfs(src, target)