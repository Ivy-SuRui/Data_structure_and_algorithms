def detect_arbitrage(N, edges):
    dist = [0] * N

    for i in range(N-1):
        for u,v,w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
        
    for u,v,w in edges:
        if dist[v] > dist[u] + w:
            return "There is a currency arbitrage."
    return "No, there isn't a currency arbitrage."



def main():
    N = 4
    edges = [
        (0, 1, 1),
        (1, 2, 1),
        (2, 3, -3),
        (3, 1, 1),
        (0, 2, 10)
    ]
    print("Arbitrage Detected:", detect_arbitrage(N, edges))

if __name__ == "__main__":
    main()