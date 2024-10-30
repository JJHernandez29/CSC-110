"""
Program: Wormhole.py
Author: JJ Hernandez
Last date modified:5/5/2024
"""

def min_travel_time(n, m, k, wormholes):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for x in range(n + 1):
        for y in range(m + 1):
            if (x, y) in wormholes:
                continue
            if x > 0:
                dp[x][y] += dp[x - 1][y]
            if y > 0:
                dp[x][y] += dp[x][y - 1]

    return dp[n][m]

def main():
    # Sample Input 1
    n1, m1, k1 = 1, 1, 0
    wormholes1 = set()
    result1 = min_travel_time(n1, m1, k1, wormholes1)
    print("Output for Sample Input 1:", result1)

    # Sample Input 2
    n2, m2, k2 = 2, 2, 0
    wormholes2 = set()
    result2 = min_travel_time(n2, m2, k2, wormholes2)
    print("Output for Sample Input 2:", result2)

    # Sample Input 3
    n3, m3, k3 = 2, 2, 1
    wormholes3 = {(0, 0), (1, 1)}
    result3 = min_travel_time(n3, m3, k3, wormholes3)
    print("Output for Sample Input 3:", result3)

if __name__ == "__main__":
    main()
