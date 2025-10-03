/*
import sys
from collections import defaultdict, deque


def input():
    return sys.stdin.readline().rstrip()


def print_2d(lst, sep=None):
    """
    2次元配列を出力する関数だっピ\n
    ￣￣V￣￣￣￣￣￣￣￣￣￣￣￣\n
    ( ・3・)\n
    /｜｜｜\\

    Parameters
    ----------
    lst : list
        出力したい2次元配列
    sep : str
        区切り文字(デフォルトはNone)
    """
    for LIST in lst:
        print(*LIST, sep=sep)


# UnionFindに連結成分以外の情報を乗せたいとき
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [[-1, False] for _ in range(n)]

    def find(self, x):
        if self.parents[x][0] < 0:
            return x
        else:
            self.parents[x][0] = self.find(self.parents[x][0])
            return self.parents[x][0]

    def connect_kabe(self, x):
        root = self.find(x)
        self.parents[root][1] = True
        return self.parents[root][1]

    def is_connected_kabe(self, x):
        root = self.find(x)
        return self.parents[root][1]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x][0] > self.parents[y][0]:
            x, y = y, x

        self.parents[x][0] += self.parents[y][0]
        self.parents[x][1] = self.parents[x][1] or self.parents[y][1]
        self.parents[y][0] = x
        self.parents[y][1] = False

    def size(self, x):
        return -self.parents[self.find(x)][0]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents[0]) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(
                (member, self.is_connected_kabe(member))
            )
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


def main():
    from time import time
    import random
    import copy

    start = time()

    N, ti, tj = map(int, input().split())
    b = []
    tree_masu = []
    enpty_masu = set()
    all_masu = []
    for i in range(N):
        bt = list(input())
        b.append(bt)
        for j in range(N):
            all_masu.append((i, j))
            if bt[j] == "T":
                tree_masu.append((i, j))
            else:
                enpty_masu.add((i, j))

    boukensha = (0, int(N / 2))

    enpty_masu.discard(boukensha)
    enpty_masu.discard((ti, tj))

    direction = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    tateyoko_direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    naname_direction = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

    def is_out_of_range(ii, jj):
        return ii < 0 or jj < 0 or N <= ii or N <= jj

    def is_hasi(ii, jj):
        return ii == 0 or jj == 0 or N - 1 == ii or N - 1 == jj

    def ij_to_num(ii, jj):
        return ii * N + jj

    base_uf = UnionFind(N * N)
    # 0. あらかじめ周囲8方向で隣接していたらufでつないぎ、集合とする
    for i, j in tree_masu:
        if is_hasi(i, j):
            base_uf.connect_kabe(ij_to_num(i, j))
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if not is_out_of_range(ni, nj) and b[ni][nj] == "T":
                base_uf.union(ij_to_num(i, j), ij_to_num(ni, nj))

    torrent = set()
    path_len = 0
    while time() - start < 1.88:
        torrent_t = set()
        enpty_masu_t = copy.deepcopy(enpty_masu)
        uf = copy.deepcopy(base_uf)

        def kabenobashi(masu_lst):
            for i, j in random.sample(masu_lst, len(masu_lst)):
                rand_direction = random.sample(naname_direction, 4)
                # 自身が空きマスだったら
                if (i, j) in enpty_masu_t:
                    kabe_cnt = 0
                    breaked = False
                    kabe_is_hasi = False
                    root_lst = set()
                    kabe_lst = []
                    # 周囲に壁8方向を見る
                    for di, dj in direction:
                        ni, nj = i + di, j + dj
                        if not is_out_of_range(ni, nj):
                            if (ni, nj) not in enpty_masu_t:
                                root_node = uf.find(ij_to_num(ni, nj))
                                # 同じ壁集合がすでにあれば
                                if root_node in root_lst:
                                    breaked = True
                                    break
                                # 端に繋がっている壁をカウント
                                kabe_cnt += uf.is_connected_kabe(ij_to_num(ni, nj))
                                kabe_lst.append((ni, nj))
                                root_lst.add(root_node)
                        else:
                            kabe_is_hasi = True

                    # 死に領域が発生するならば
                    if 1 < kabe_cnt + kabe_is_hasi or breaked:
                        continue

                    torrent_t.add((i, j))
                    enpty_masu_t.discard((i, j))
                    if is_hasi(i, j):
                        uf.connect_kabe(ij_to_num(i, j))
                    if len(kabe_lst) != 0:
                        for tni, tnj in kabe_lst:
                            uf.union(ij_to_num(i, j), ij_to_num(tni, tnj))

                # rand_direction += random.sample(tateyoko_direction, 4)

                now_i, now_j = i, j
                is_united = False
                while True:
                    # 2. 斜め4方向を移動候補とし、ランダムでみる
                    for di, dj in rand_direction:
                        ni, nj = now_i + di, now_j + dj
                        # 3. 移動候補から見て自身が空きマスかつスタートでもゴールでもない、かつ自分が端に繋がってて、壁と隣接してない場合
                        if (
                            not is_out_of_range(ni, nj)
                            and (ni, nj) in enpty_masu_t
                            and (ni, nj) != boukensha
                            and (ni, nj) != (ti, tj)
                            and (
                                not is_hasi(ni, nj)
                                if uf.is_connected_kabe(ij_to_num(now_i, now_j))
                                else True
                            )
                        ):
                            # 3. 周囲8方向を見る
                            for ddi, ddj in direction:
                                nni, nnj = ni + ddi, nj + ddj
                                # (now_i, now_j)のマス以外で
                                if not is_out_of_range(nni, nnj) and (now_i, now_j) != (
                                    nni,
                                    nnj,
                                ):
                                    # (now_i, now_j)と同じ集合のマスがあったら
                                    if uf.same(
                                        ij_to_num(now_i, now_j), ij_to_num(nni, nnj)
                                    ):
                                        break
                                    # (now_i, now_j)のマスが壁に繋がっていて、他に壁につながる木があったら
                                    if uf.is_connected_kabe(
                                        ij_to_num(now_i, now_j)
                                    ) and uf.is_connected_kabe(ij_to_num(nni, nnj)):
                                        break
                            else:
                                # 周囲8マスが大丈夫だったら、塗りつぶし、隣接する壁をつなぎ、nowを更新し、2を抜ける
                                torrent_t.add((ni, nj))
                                enpty_masu_t.discard((ni, nj))
                                # print((now_i, now_j), (ni, nj))
                                uf.union(ij_to_num(now_i, now_j), ij_to_num(ni, nj))
                                for ddi, ddj in direction:
                                    nni, nnj = ni + ddi, nj + ddj
                                    if not is_out_of_range(nni, nnj) and (
                                        b[nni][nnj] == "T" or (nni, nnj) in torrent_t
                                    ):
                                        uf.union(ij_to_num(ni, nj), ij_to_num(nni, nnj))
                                        is_united = False
                                now_i, now_j = ni, nj
                                break
                    # 一度どこかとunitしたら
                    if is_united:
                        break
                    else:
                        # 2を抜けることがない場合、移動候補全てがダメなマスなので、
                        break

        kabenobashi(all_masu)

        # bfs (straight segments cost 1)
        enpty_masu_t.add((ti, tj))
        INF = 10**9
        NONE_DIR = len(tateyoko_direction)
        dist = [[[INF] * (NONE_DIR + 1) for _ in range(N)] for _ in range(N)]

        si, sj = boukensha
        dist[si][sj][NONE_DIR] = 0
        dq = deque([(si, sj, NONE_DIR)])

        while dq:
            i, j, dir_idx = dq.popleft()
            current_dist = dist[i][j][dir_idx]

            for nd_idx, (di, dj) in enumerate(tateyoko_direction):
                ni, nj = i + di, j + dj

                if is_out_of_range(ni, nj):
                    continue
                if (ni, nj) not in enpty_masu_t:
                    continue

                if dir_idx == NONE_DIR:
                    add_cost = 1
                elif dir_idx == nd_idx:
                    add_cost = 0
                else:
                    add_cost = 1

                ndist = current_dist + add_cost
                if ndist < dist[ni][nj][nd_idx]:
                    dist[ni][nj][nd_idx] = ndist
                    if add_cost == 0:
                        dq.appendleft((ni, nj, nd_idx))
                    else:
                        dq.append((ni, nj, nd_idx))

        path_len_t = min(dist[ti][tj][:NONE_DIR])
        if path_len_t == INF:
            path_len_t = -1
        if path_len < path_len_t:
            path_len = path_len_t
            torrent = copy.deepcopy(torrent_t)

    # debug
    # print(path_len)
    # print(torrent)
    # for nr, nc in torrent:
    #     b[nr][nc] = "T"
    # if b[boukensha[0]][boukensha[1]] == ".":
    #     b[boukensha[0]][boukensha[1]] = "S"
    # if b[ti][tj] == ".":
    #     b[ti][tj] = "G"
    # print_2d(b)

    print(len(torrent), end=" ", flush=True)
    for ii, jj in torrent:
        print(ii, jj, end=" ", flush=True)

    print("\n" + "-1", flush=True)


if __name__ == "__main__":
    main()
*/

#include <algorithm>
#include <array>
#include <chrono>
#include <deque>
#include <iostream>
#include <random>
#include <string>
#include <tuple>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

struct UnionFind {
    struct Node {
        int parent;
        bool connected;
    };

    int n;
    vector<Node> data;

    UnionFind() : n(0) {}

    explicit UnionFind(int n_) : n(n_), data(n_, {-1, false}) {}

    int find(int x) {
        if (data[x].parent < 0) {
            return x;
        }
        data[x].parent = find(data[x].parent);
        return data[x].parent;
    }

    bool connect_kabe(int x) {
        int root = find(x);
        data[root].connected = true;
        return data[root].connected;
    }

    bool is_connected_kabe(int x) {
        int root = find(x);
        return data[root].connected;
    }

    void unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) {
            return;
        }
        if (data[x].parent > data[y].parent) {
            swap(x, y);
        }
        data[x].parent += data[y].parent;
        data[x].connected = data[x].connected || data[y].connected;
        data[y].parent = x;
        data[y].connected = false;
    }

    int size(int x) {
        return -data[find(x)].parent;
    }

    bool same(int x, int y) {
        return find(x) == find(y);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    using Clock = chrono::steady_clock;
    auto start = Clock::now();

    int N, ti, tj;
    if (!(cin >> N >> ti >> tj)) {
        return 0;
    }

    vector<string> b(N);
    vector<pair<int, int>> tree_masu;
    unordered_set<int> enpty_masu;
    vector<pair<int, int>> all_masu;

    for (int i = 0; i < N; ++i) {
        cin >> b[i];
        for (int j = 0; j < N; ++j) {
            all_masu.emplace_back(i, j);
            if (b[i][j] == 'T') {
                tree_masu.emplace_back(i, j);
            } else {
                enpty_masu.insert(i * N + j);
            }
        }
    }

    pair<int, int> boukensha = {0, N / 2};

    enpty_masu.erase(boukensha.first * N + boukensha.second);
    enpty_masu.erase(ti * N + tj);

    const vector<pair<int, int>> direction = {
        {0, -1}, {0, 1}, {-1, 0}, {1, 0}, {-1, -1}, {1, -1}, {-1, 1}, {1, 1}};
    constexpr int NONE_DIR = 4;
    const vector<pair<int, int>> tateyoko_direction = {
        {0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    const vector<pair<int, int>> naname_direction = {
        {-1, -1}, {1, -1}, {-1, 1}, {1, 1}};

    auto is_out_of_range = [&](int ii, int jj) {
        return ii < 0 || jj < 0 || ii >= N || jj >= N;
    };

    auto is_hasi = [&](int ii, int jj) {
        return ii == 0 || jj == 0 || ii == N - 1 || jj == N - 1;
    };

    auto ij_to_num = [&](int ii, int jj) {
        return ii * N + jj;
    };

    UnionFind base_uf(N * N);
    for (auto [i, j] : tree_masu) {
        if (is_hasi(i, j)) {
            base_uf.connect_kabe(ij_to_num(i, j));
        }
        for (auto [di, dj] : direction) {
            int ni = i + di;
            int nj = j + dj;
            if (!is_out_of_range(ni, nj) && b[ni][nj] == 'T') {
                base_uf.unite(ij_to_num(i, j), ij_to_num(ni, nj));
            }
        }
    }

    unordered_set<int> best_torrent;
    int path_len = 0;

    mt19937 rng(random_device{}());

    while (chrono::duration<double>(Clock::now() - start).count() < 1.9) {
        unordered_set<int> torrent_t;
        unordered_set<int> enpty_masu_t = enpty_masu;
        UnionFind uf = base_uf;

        auto kabenobashi = [&](const vector<pair<int, int>>& masu_lst) {
            vector<pair<int, int>> order = masu_lst;
            shuffle(order.begin(), order.end(), rng);
            for (auto [i, j] : order) {
                vector<pair<int, int>> rand_direction = naname_direction;
                shuffle(rand_direction.begin(), rand_direction.end(), rng);

                int idx = ij_to_num(i, j);
                if (enpty_masu_t.count(idx)) {
                    int kabe_cnt = 0;
                    bool breaked = false;
                    bool kabe_is_hasi = false;
                    unordered_set<int> root_lst;
                    vector<pair<int, int>> kabe_lst;
                    for (auto [di, dj] : direction) {
                        int ni = i + di;
                        int nj = j + dj;
                        if (!is_out_of_range(ni, nj)) {
                            int nidx = ij_to_num(ni, nj);
                            if (!enpty_masu_t.count(nidx)) {
                                int root_node = uf.find(nidx);
                                if (root_lst.count(root_node)) {
                                    breaked = true;
                                    break;
                                }
                                if (uf.is_connected_kabe(nidx)) {
                                    kabe_cnt += 1;
                                }
                                kabe_lst.emplace_back(ni, nj);
                                root_lst.insert(root_node);
                            }
                        } else {
                            kabe_is_hasi = true;
                        }
                    }
                    if (kabe_cnt + (kabe_is_hasi ? 1 : 0) > 1 || breaked) {
                        continue;
                    }
                    torrent_t.insert(idx);
                    enpty_masu_t.erase(idx);
                    if (is_hasi(i, j)) {
                        uf.connect_kabe(idx);
                    }
                    if (!kabe_lst.empty()) {
                        for (auto [tni, tnj] : kabe_lst) {
                            uf.unite(idx, ij_to_num(tni, tnj));
                        }
                    }
                }

                int now_i = i;
                int now_j = j;
                bool is_united = false;
                while (true) {
                    for (size_t nd_idx = 0; nd_idx < rand_direction.size(); ++nd_idx) {
                        int di = rand_direction[nd_idx].first;
                        int dj = rand_direction[nd_idx].second;
                        int ni = now_i + di;
                        int nj = now_j + dj;
                        if (is_out_of_range(ni, nj)) {
                            continue;
                        }
                        int nidx = ij_to_num(ni, nj);
                        if (!enpty_masu_t.count(nidx)) {
                            continue;
                        }
                        if (ni == boukensha.first && nj == boukensha.second) {
                            continue;
                        }
                        if (ni == ti && nj == tj) {
                            continue;
                        }
                        if (uf.is_connected_kabe(ij_to_num(now_i, now_j)) &&
                            is_hasi(ni, nj)) {
                            continue;
                        }
                        bool ok = true;
                        for (auto [ddi, ddj] : direction) {
                            int nni = ni + ddi;
                            int nnj = nj + ddj;
                            if (!is_out_of_range(nni, nnj) &&
                                !(nni == now_i && nnj == now_j)) {
                                if (uf.same(ij_to_num(now_i, now_j), ij_to_num(nni, nnj))) {
                                    ok = false;
                                    break;
                                }
                                if (uf.is_connected_kabe(ij_to_num(now_i, now_j)) &&
                                    uf.is_connected_kabe(ij_to_num(nni, nnj))) {
                                    ok = false;
                                    break;
                                }
                            }
                        }
                        if (ok) {
                            torrent_t.insert(nidx);
                            enpty_masu_t.erase(nidx);
                            uf.unite(ij_to_num(now_i, now_j), nidx);
                            for (auto [ddi, ddj] : direction) {
                                int nni = ni + ddi;
                                int nnj = nj + ddj;
                                if (!is_out_of_range(nni, nnj)) {
                                    int nnidx = ij_to_num(nni, nnj);
                                    if (b[nni][nnj] == 'T' || torrent_t.count(nnidx)) {
                                        uf.unite(nidx, nnidx);
                                        is_united = false;
                                    }
                                }
                            }
                            now_i = ni;
                            now_j = nj;
                            break;
                        }
                    }
                    if (is_united) {
                        break;
                    } else {
                        break;
                    }
                }
            }
        };

        kabenobashi(all_masu);

    enpty_masu_t.insert(ij_to_num(ti, tj));
    const int INF = 1'000'000'000;
    constexpr int DIR_STATES = NONE_DIR + 1;
    vector<vector<array<int, DIR_STATES>>> dist(N, vector<array<int, DIR_STATES>>(N));
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                dist[i][j].fill(INF);
            }
        }

        int si = boukensha.first;
        int sj = boukensha.second;
        dist[si][sj][NONE_DIR] = 0;
        deque<tuple<int, int, int>> dq;
        dq.emplace_back(si, sj, NONE_DIR);

        while (!dq.empty()) {
            auto [i, j, dir_idx] = dq.front();
            dq.pop_front();
            int current_dist = dist[i][j][dir_idx];

            for (int nd_idx = 0; nd_idx < NONE_DIR; ++nd_idx) {
                int di = tateyoko_direction[nd_idx].first;
                int dj = tateyoko_direction[nd_idx].second;
                int ni = i + di;
                int nj = j + dj;
                if (is_out_of_range(ni, nj)) {
                    continue;
                }
                int nidx = ij_to_num(ni, nj);
                if (!enpty_masu_t.count(nidx)) {
                    continue;
                }
                int add_cost;
                if (dir_idx == NONE_DIR) {
                    add_cost = 1;
                } else if (dir_idx == nd_idx) {
                    add_cost = 0;
                } else {
                    add_cost = 1;
                }
                int ndist = current_dist + add_cost;
                if (ndist < dist[ni][nj][nd_idx]) {
                    dist[ni][nj][nd_idx] = ndist;
                    if (add_cost == 0) {
                        dq.emplace_front(ni, nj, nd_idx);
                    } else {
                        dq.emplace_back(ni, nj, nd_idx);
                    }
                }
            }
        }

        int path_len_t = INF;
        for (int idx = 0; idx < NONE_DIR; ++idx) {
            path_len_t = min(path_len_t, dist[ti][tj][idx]);
        }
        if (path_len_t == INF) {
            path_len_t = -1;
        }
        if (path_len < path_len_t) {
            path_len = path_len_t;
            best_torrent = torrent_t;
        }
    }

    cout << best_torrent.size() << ' ';
    for (int idx : best_torrent) {
        int ii = idx / N;
        int jj = idx % N;
        cout << ii << ' ' << jj << ' ';
    }
    cout << "\n-1\n";
    return 0;
}
