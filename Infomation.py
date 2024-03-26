# This Python file uses the following encoding: utf-8
import math

#constant value
kEmpryColor = 0
kWhite = 1
kBlack = 2

kBlockSize = 60
kMargin = 10
kBlockNum = 8
kDirection = ([0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1])



kMaxAIThinkTimes = 30
kMaxAITryTimes = 100
kScalar = 1
kSelectPolicyProbability = 0.3
kMaxStimulateTimes = 10


#variable quantity
ai_color = 1
player_color = 2





def opponent_color(color):
    if color == kWhite:
        return kBlack
    return kWhite

def ucb(node_visit, son_visit, son_reward, scalar):
    return son_reward / son_visit + scalar * math.sqrt(2.0 * math.log(node_visit) / float(son_visit))
# if __name__ == "__main__":
#     pass
